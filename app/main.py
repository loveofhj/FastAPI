from fastapi import FastAPI, UploadFile, File
from .model_utils import predict

app = FastAPI()

@app.get("/")
def root():
    return {"message": "🚀 FastAPI + Docker AI 서버 동작 중"}

@app.post("/predict")
async def predict_api(file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = predict(image_bytes)
    return {"result": result}
