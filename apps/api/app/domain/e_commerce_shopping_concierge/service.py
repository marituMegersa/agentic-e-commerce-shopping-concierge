from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.e_commerce_shopping_concierge.models import AgenticECommerceShoppingConciergeSession, AgenticECommerceShoppingConciergeItem
from app.domain.e_commerce_shopping_concierge.schemas import AgenticECommerceShoppingConciergeSessionCreate, AgenticECommerceShoppingConciergeItemCreate

class AgenticECommerceShoppingConciergeService:
    @staticmethod
    def create_session(db: Session, data: AgenticECommerceShoppingConciergeSessionCreate) -> AgenticECommerceShoppingConciergeSession:
        db_obj = AgenticECommerceShoppingConciergeSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticECommerceShoppingConciergeSession:
        return db.query(AgenticECommerceShoppingConciergeSession).filter(AgenticECommerceShoppingConciergeSession.id == session_id).first()
