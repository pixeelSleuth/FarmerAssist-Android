# 🌾 Farmer Assist (AI-Powered Agricultural Advisory Platform)

An intelligent, full-stack agricultural support system designed to empower farmers with AI-driven crop diagnostics, dynamic weather advisories, and a voice-enabled AI agronomist. 

The project consists of a **FastAPI backend** handling AI, data, and voice services, coupled with a cross-platform **Flutter mobile app** for the client interface.

---

## 🚀 Key Features

* **🤖 AI Agronomist**: Integrated with Google Gemini API to provide real-time, context-aware advice on crop management, soil health, and pest control.
* **🔍 Disease Detection & Remedies**: Allows farmers to upload photos of diseased crops using their phone camera and receive instant AI diagnosis along with recommended treatments.
* **🎙️ Voice Assistant**: Uses Sarvam AI (Speech-to-Text and Text-to-Speech) to enable regional voice commands and replies, ensuring accessibility for all farmers.
* **🌤️ Hyper-Local Weather**: Fetches real-time weather metrics using the OpenWeather API to generate personalized daily agricultural advisories.
* **📅 Crop Stage Tracking**: Guides farmers throughout the lifecycle of their crops, giving timely updates and suggestions.
* **🔒 Secure Authentication**: Secure account registration and session management.

---

## 🛠️ Tech Stack

### Backend
* **Framework**: FastAPI (Python)
* **Databases**: 
  * **MySQL**: Relational storage for user, crop, and advisory metadata.
  * **MongoDB**: NoSQL storage for flexible chat history and disease records.
  * **Redis**: Fast caching for session management and weather responses.
* **AI & Voice Integration**: Google Gemini API, Sarvam AI (STT/TTS), and OpenWeather API.
* **Auth**: JWT-based session security via `python-jose` and `bcrypt`.

### Mobile Client
* **Framework**: Flutter (Dart)
* **State Management**: Provider
* **Storage**: Flutter Secure Storage (tokens) & Shared Preferences (user preferences)
* **Hardware Integrations**: Image Picker (for camera/gallery upload)

---

## 📁 Repository Structure

```
FarmerAssist/
├── backend/               # FastAPI Python application
│   ├── app/               # Main application package
│   │   ├── admin/         # Admin endpoints
│   │   ├── advisory/      # Weather/Advisory routers
│   │   ├── ai_agronomist/ # Gemini Chatbot logic
│   │   ├── api/           # Auth, crop stages, weather routes
│   │   ├── core/          # App config and security keys
│   │   ├── disease_.../   # Image upload and detection APIs
│   │   └── voice_.../     # Sarvam STT/TTS routing
│   ├── main.py            # Backend entry point
│   ├── requirements.txt   # Python dependency list
│   └── .env.example       # Environment variables template
├── mobile/                # Flutter mobile application
│   ├── lib/               # Dart source code
│   ├── pubspec.yaml       # Flutter packages configuration
│   └── .gitignore         # Flutter-specific ignore configurations
└── .gitignore             # Root gitignore (excludes secrets & builds)
```

---

## ⚙️ Getting Started (Local Development)

Follow these steps to set up the project on your machine:

### 1. Backend Setup (Python FastAPI)

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   # On Windows (PowerShell):
   .\venv\Scripts\Activate.ps1
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```
4. Configure environment variables:
   * Copy the template `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   * Open the `.env` file and input your actual API keys (Gemini, Sarvam, OpenWeather) and local database credentials.
5. Place your Firebase Admin SDK **`serviceAccount.json`** credential file in the `backend/app/firebase/` directory (needed for Firebase integrations).
6. Start local databases (MySQL, MongoDB, and Redis).
7. Run the FastAPI development server:
   ```bash
   python main.py
   # Or run reload-enabled uvicorn directly
   uvicorn main:app --reload
   ```
   *The interactive API documentation will be available at `http://localhost:8000/docs`.*

---

### 2. Mobile App Setup (Flutter)

1. Ensure you have the Flutter SDK installed and configured.
2. Navigate to the mobile directory:
   ```bash
   cd ../mobile
   ```
3. Download and restore package dependencies:
   ```bash
   flutter pub get
   ```
4. Connect an Android/iOS emulator or physical device.
5. Run the application:
   ```bash
   flutter run
   ```

---

