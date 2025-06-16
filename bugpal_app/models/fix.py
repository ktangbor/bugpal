from black import timezone
from sqlalchemy import Column, Integer, func, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship

from bugpal_app.db.session import Base

class Fix(Base):
    __tablename__ = "fixes"

    id = Column(Integer, primary_key=True, index=True)
    issue_id = Column(Integer, ForeignKey("issues.id",
                                          ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey("users.id",
                                         ondelete="SET NULL"),
                     nullable=True)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="fixes")
    issue = relationship("Issue", back_populates="fixes",
                         passive_deletes=True)
    votes = relationship("Vote", back_populates="fix",
                         cascade="all, delete")