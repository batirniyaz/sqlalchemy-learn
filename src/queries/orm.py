from sqlalchemy import text, insert
from src.database import sync_engine, async_engine, session_factory, async_session_factory, Base
from src.models import metadata_obj, WorkersOrm


def create_tables():
    Base.metadata.drop_all(sync_engine)
    sync_engine.echo = True
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True


def insert_data():
    with session_factory() as session:
        worker_bobr = WorkersOrm(username="Bobr")
        worker_volk = WorkersOrm(username="Volk")
        session.add_all([worker_bobr, worker_volk])
        session.commit()


async def insert_data():
    async with async_session_factory() as session:
        worker_bobr = WorkersOrm(username="Bobr")
        worker_volk = WorkersOrm(username="Volk")
        session.add_all([worker_bobr, worker_volk])
        await session.commit()