from sqlalchemy import text, insert
from src.database import sync_engine, async_engine
from src.models import metadata_obj, workers_table, WorkersOrm


def get_123_sync():
    with sync_engine.connect() as conn:
        ress = conn.execute(text("SELECT VERSION()"))
        print(f"{ress.all()=}")


async def get_123_async():
    async with async_engine.connect() as conn:
        ress = await conn.execute(text("SELECT VERSION()"))
        print(f"{ress.all()=}")


def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True


def insert_data():
    with sync_engine.connect() as conn:
        # stmt = """INSERT INTO workers (username) VALUES 
        #         ('Bobr'),
        #         ('Volk');"""

        stmt = insert(workers_table).values(
            [
                {"username": "bobr"},
                {"username": "volk"},
            ]
        )
        conn.execute(stmt)
        conn.commit()