import datetime
from typing import Annotated
from sqlalchemy import Column, Integer, String, Table, MetaData, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
from database import Base, str_256
import enum

# Custom type for primary key
intpk = Annotated[int, mapped_column(primary_key=True)]

# Custom type for created_at and updated_at
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.datetime.now(datetime.UTC))]


class WorkersOrm(Base):
    __tablename__ = "workers"

    id: Mapped[intpk]
    username: Mapped[str]


class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"


class ResumesOrm(Base):
    __tablename__ = "resumes"

    id: Mapped[intpk]
    title: Mapped[str_256] # Custom type for string with max length 256 from database.py
    compisation: Mapped[int] = mapped_column(nullable=True) # or Mapped[Optional[int]] or Mapped[int | None]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]





























metadata_obj = MetaData()

workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)