"""
Entry point for the Farmer Advisory Backend API
Run with: python main.py
Or with uvicorn: uvicorn main:app --reload
"""

from app.main import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
