from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dinesh_p")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "mysql+pymysql://cheenu:1234@localhost/airbnb_clone_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_jwt_secret_key")
    GOOGLE_API_KEY = os.getenv("AIzaSyDQAkeKPsvnkXn8QjmtGlmIW569PNyvCl4")
    GOOGLE_CX = os.getenv("GOOGLE_CX")
