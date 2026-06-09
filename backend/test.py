import firebase_admin
from firebase_admin import auth, credentials
import requests
import json
from pathlib import Path
import sys

# Add parent directory to path to import app modules
sys.path.insert(0, str(Path(__file__).parent))

from app.core.config import settings

# Initialize Firebase Admin SDK with service account credentials
cred_path = Path(__file__).parent / settings.FIREBASE_CREDENTIALS
cred = credentials.Certificate(str(cred_path))

try:
    firebase_admin.initialize_app(cred)
except ValueError:
    # App already initialized
    pass

# Create a test user with email and password
email = "test@farmer.com"
password = "Test@123456"

try:
    # Try to get existing user
    user = auth.get_user_by_email(email)
    print(f"✓ User already exists: {user.uid}")
except auth.UserNotFoundError:
    # Create new user if doesn't exist
    user = auth.create_user(email=email, password=password)
    print(f"✓ User created: {user.uid}")

# Get project ID from credentials
cred_dict = json.load(open(str(cred_path)))
project_id = cred_dict["project_id"]

# Generate a custom token
custom_token = auth.create_custom_token(user.uid)
print(f"✓ Custom token generated")

# Exchange custom token for ID token using Firebase REST API
api_key = settings.FIREBASE_API_KEY
url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key={api_key}"

try:
    response = requests.post(
        url,
        json={"token": custom_token.decode('utf-8'), "returnSecureToken": True}
    )
    response.raise_for_status()
    id_token = response.json()["idToken"]
    
    print(f"\n✅ Firebase ID Token (valid for ~1 hour):")
    print(f"{id_token}")
    
    print(f"\n📧 User Email: {email}")
    print(f"🔑 Password: {password}")
    print(f"📱 User UID: {user.uid}")
    print(f"\n💡 Use this token in Authorization header:")
    print(f"   Authorization: Bearer {id_token}")
    print(f"\n📝 Test with cURL:")
    print(f'   curl -X POST http://localhost:8000/auth/verify \\')
    print(f'     -H "Content-Type: application/json" \\')
    print(f'     -d \'{{"firebase_token": "{id_token}"}}\'')
    
except Exception as e:
    print(f"❌ Error exchanging token: {e}")
    print(f"\nResponse: {response.text if 'response' in locals() else 'No response'}")
    sys.exit(1)