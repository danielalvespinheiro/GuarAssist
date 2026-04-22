from fastapi import APIRouter
from database.database import resumo_dashboard

router = APIRouter()

@router.get("/stats")
def get_stats():
    """
    Retorna um resumo geral para o dashboard: 
    total de análises realizadas, quantas foram saudável vs. praga detectada, e qual praga apareceu mais vezes. 
    O banco já tem a função resumo_talhao() que pode ser usada como base.
    """
    
    return resumo_dashboard()