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
    
def get_applicant_details(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM applications WHERE id = :id"), {"id": id}).fetchone()
        return result._asdict() if result else None

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
            conn.execute(text("COMMIT"))
            return {"status": True}
    except Exception as e:
        print(f"Error adding application: {e}")
        return {"status": False, "error": str(e)}

def get_user_by_username(username):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM users WHERE username = :username"), {"username": username}).fetchone()
        return result._asdict() if result else None

def get_user_by_id(user_id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM users WHERE id = :id"), {"id": user_id}).fetchone()
        return result._asdict() if result else None

def verify_user_credentials(username, password):
    user = get_user_by_username(username)
    if user and user['password'] == password:  
        return True
    return False
