"""FastAPI server for AgriMind."""
from fastapi import FastAPI, UploadFile, File
from app.agents.crop_expert import CropExpertAgent

def create_app():
    app = FastAPI(
        title="🌾 农智云 AgriMind",
        description="AI驱动的中国智慧种植知识平台",
        version="0.1.0",
    )

    expert = CropExpertAgent()

    @app.get("/")
    async def root():
        return {"name": "农智云 AgriMind", "version": "0.1.0", "status": "running"}

    @app.get("/api/crops")
    async def list_crops():
        return list(expert.knowledge.keys())

    @app.get("/api/crops/{crop_name}")
    async def get_crop(crop_name: str):
        return expert.get_crop_guide(crop_name)

    @app.get("/api/crops/{crop_name}/advice")
    async def get_advice(crop_name: str, month: int = 1, zone: str = "华东"):
        return expert.get_seasonal_advice(crop_name, month, zone)

    @app.get("/api/search")
    async def search(query: str):
        return expert.search(query)

    @app.post("/api/diagnose")
    async def diagnose(file: UploadFile = File(...)):
        """Upload plant photo for disease diagnosis."""
        # TODO: Implement image recognition
        return {"message": "图片识别功能开发中", "filename": file.filename}

    return app
