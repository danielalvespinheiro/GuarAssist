from fastapi import APIRouter, UploadFile, File, HTTPException
from models.detector import detect_disease
from database.database import save_analysis
from PIL import Image
from io import BytesIO
import uuid, time

router = APIRouter()

MAX_SIZE = 10 * 1024 * 1024
ALLOWED_FORMATS = ["JPEG", "PNG", "WEBP"]

@router.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    """
    Recebe uma imagem da planta de guaraná e retorna o diagnóstico.

    Retorno:
    - status: "saudavel" | "praga_detectada"
    - disease: nome da praga (ou None)
    - confidence: porcentagem de confiança (0.0 a 1.0)
    - analysis_id: ID para consulta no histórico
    """

    if not file:
        raise HTTPException(status_code=400, detail="Nenhum arquivo foi enviado.")
    
    image_bytes = await file.read()

    if len(image_bytes) > MAX_SIZE:
        raise HTTPException(status_code=400, detail="A imagem passou do tamanho maximo de 10MB")

    try:
        image = Image.open(BytesIO(image_bytes))
        image.verify()
        image = Image.open(BytesIO(image_bytes))

    except  Exception:
        raise HTTPException(status_code=400, detail="O arquivo enviado não é uma imagem válida!")
    
    if image.format not in ALLOWED_FORMATS:
        raise HTTPException(status_code=400, detail="O formato do arquivo não é permitido. Use somente JPEG, PNG e WEBP")

    try:
        result = detect_disease(image_bytes)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro no modelo de IA: {str(e)}")

    analysis_id = str(uuid.uuid4())
    timestamp = int(time.time())

    save_analysis({
        "id": analysis_id,
        "timestamp": timestamp,
        "filename": file.filename,
        "status": result["status"],
        "disease": result["disease"],
        "confidence": result["confidence"],
    })

    return {
        "analysis_id": analysis_id,
        "timestamp": timestamp,
        **result
    }
 
