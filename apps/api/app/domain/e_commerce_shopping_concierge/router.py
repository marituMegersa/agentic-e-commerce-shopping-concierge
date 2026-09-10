from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.e_commerce_shopping_concierge.schemas import AgenticECommerceShoppingConciergeSessionCreate, AgenticECommerceShoppingConciergeSessionResponse
from app.domain.e_commerce_shopping_concierge.service import AgenticECommerceShoppingConciergeService

router = APIRouter(prefix="/api/v1/e_commerce_shopping_concierge", tags=["Agentic E Commerce Shopping Concierge Domain"])

@router.post("/sessions", response_model=AgenticECommerceShoppingConciergeSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticECommerceShoppingConciergeSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic E Commerce Shopping Concierge.
    """
    return AgenticECommerceShoppingConciergeService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticECommerceShoppingConciergeSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticECommerceShoppingConciergeService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
