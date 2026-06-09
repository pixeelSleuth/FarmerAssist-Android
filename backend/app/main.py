from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.farmers import (
    router as farmer_router
)
from app.api.crop_stage import (
    router as crop_stage_router
)
from app.api.weather import (
    router as weather_router
)
from app.advisory.router import (
    router as advisory_router
)
from app.disease_detection.router import (
    router as disease_router
)

from app.disease_recommendation.router import (
    router as recommendation_router
)
from app.ai_agronomist.router import (
    router as ai_router
)
from app.voice_assistant.router import (
    router as voice_router
)
from fastapi.staticfiles import StaticFiles
from app.admin.router import (
    router as admin_router
)


app = FastAPI(
    title="Farmer Advisory API",
    version="1.0.0"
)
app.include_router(
    admin_router
)

app.include_router(auth_router)
app.include_router(
    farmer_router
)
app.include_router(
    crop_stage_router
)
app.include_router(
    weather_router
)
app.include_router(
    disease_router
)

app.include_router(
    recommendation_router
)

app.include_router(
    advisory_router
)

app.include_router(
    ai_router
)
app.include_router(
    voice_router
)
app.mount(
    "/audio",
    StaticFiles(directory="generated_audio"),
    name="audio"
)

@app.get("/")
def root():

    return {
        "message": "Farmer Advisory Backend Running"
    }