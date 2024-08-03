from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.getenv('DB_CONNECTION'))

def load_jobs():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs")).fetchall()
        return [row._asdict() for row in result]

def load_job(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :id"), {"id": id}).fetchone()
        return result._asdict() if result else None

def get_applications():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM applications")).fetchall()
        return [row._asdict() for row in result]

def add_application(data, id):
    try:
        insert_stmt = text("""
        INSERT INTO applications (full_name, email, linkedin, phone_number, experience, resume_link, job_id)
        VALUES (:full_name, :email, :linkedin, :phone_number, :experience, :resume_link, :job_id)
        """)
        with engine.connect() as conn:
            conn.execute(insert_stmt, {
                'full_name': data['full_name'],
                'email': data['email'],
                'linkedin': data['linkedin'],
                'phone_number': data['phone_number'],
                'experience': data['experience'],
                'resume_link': data['resume_link'],
                'job_id': id,
            })
            conn.commit()
            return {"status": True}
    except Exception as e:
        print(f"Error adding application: {e}")
        return {"status": False, "error": str(e)}
