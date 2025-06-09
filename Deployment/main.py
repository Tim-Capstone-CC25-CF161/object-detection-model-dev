from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="TensorFlow Model API",
    description="API untuk prediksi menggunakan pre-loaded TensorFlow model",
    version="1.0.0"
)

app.include_router(router)

