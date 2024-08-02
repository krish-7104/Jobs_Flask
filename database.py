from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
load_dotenv()
engine = create_engine(os.getenv('DB_CONNECTION'))

def load_jobs():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs")).all()
        jobs = []
        for row in result:
            jobs.append(row._asdict())
        return jobs
    