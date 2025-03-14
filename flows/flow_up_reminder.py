import asyncio
from datetime import datetime
from typing import Any
from prefect import flow, get_run_logger, tags, task
from pydantic import BaseModel
from prefect_sqlalchemy import DatabaseCredentials
from prefect_sqlalchemy.database import sqlalchemy_query

sqlalchemy_credentials = DatabaseCredentials.load("postgres-db")


class Activity(BaseModel):
    id: int
    name: str
    created_at: datetime


@flow
async def flow_up_reminder():
    logger = get_run_logger()
    logger.info(f"flow_up_reminder start")
    activities = await get_activities()
    logger.info(f"Activities: {activities}")


@task
async def get_activities():
    q = """
    SELECT * FROM leads WHERE timestamp < NOW() - INTERVAL '5 days'
    """

    return await sqlalchemy_query(q, sqlalchemy_credentials)


if __name__ == "__main__":
    async def main():
        with tags("local"):
            await flow_up_reminder()

    asyncio.run(main())
