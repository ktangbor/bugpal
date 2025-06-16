from sqlalchemy import Column, ForeignKey, Integer, DateTime, UniqueConstraint, func
from sqlalchemy.orm import relationship
from bugpal_app.db.session import Base

class Vote(Base):
    __tablename__ = "votes"
    __table_args__ = (UniqueConstraint("user_id", "fix_id", name="user_fix_unique"),)

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    fix_id = Column(Integer, ForeignKey("fixes.id", ondelete="CASCADE"))
    value = Column(Integer, nullable=False)  # +1 for upvote, -1 for downvote
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="votes")
    fix = relationship("Fix", back_populates="votes")
