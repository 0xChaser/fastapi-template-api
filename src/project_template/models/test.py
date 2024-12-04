import uuid 

from sqlalchemy import UUID, String, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from project_template.models.base import Base

class Test(Base):
    
    __tablename__ = "tests"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), unique=True, default=uuid.uuid4, nullable=False, primary_key=True
    )

    name: Mapped[str] = mapped_column(String(), nullable=False)
    age: Mapped[int] = mapped_column(Integer(), nullable=False)
    comment: Mapped[str] = mapped_column(Text(), nullable=True)

    