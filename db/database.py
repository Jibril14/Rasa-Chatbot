# import os
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv



# load_dotenv(".env")
# DATABASE_URL = os.getenv("DATABASE_URL"),
# DATABASE_URL = DATABASE_URL[0]

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# load_dotenv(os.path.join(BASE_DIR, ".env"))
# DATABASE_URL = os.environ["DATABASE_URL"]

# DATABASE_URL = "sqlite:///./laptopxpress-rasa.db"
# DATABASE_URL=postgresql://postgres:postgres14@db:5432/my_db

# DATABASE_URL = "postgresql://postgres:postgres14@db:5432/my_db"

# engine = create_engine(
#     DATABASE_URL,
#     connect_args = {"check_same_thread": False}
# )

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db 
#     finally:
#         db.close()
