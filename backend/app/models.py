from datetime import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

class TaskBase(SQLModel):
    title: str
    description: Optional[str] = None
    due_at: Optional[datetime] = None
    remind_minutes_before: Optional[int] = None

class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    is_completed: bool = Field(default=False)

    parent_id: Optional[int] = Field(default=None, foreign_key="task.id")
    children: List["Task"] = Relationship(back_populates="parent")
    parent: Optional["Task"] = Relationship(back_populates="children")

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime
    is_completed: bool
    parent_id: Optional[int] = None
