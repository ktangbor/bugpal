import os
from dotenv import load_dotenv

# Only load .env in development
ENV = os.getenv("ENV", "development")
if ENV == "development":
    load_dotenv()

class Settings:
    DB_URL = os.getenv("DATABASE_URL")
    DB_TEST_URL = os.getenv("DATABASE_TEST_URL")

settings = Settings()
