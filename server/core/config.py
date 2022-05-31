# core/config.py

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
	
    DB_USERNAME : str = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST : str = os.getenv("DB_HOST")
    DB_PORT : str = os.getenv("DB_PORT")
    DB_DATABASE : str = os.getenv("DB_DATABASE")
	
    DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}?charset=utf8"

settings = Settings()


# user_name = "min"
# user_pwd = "fksak12@@K"
# db_host = "130.162.159.163"
# db_name = "testdb"

# DATABASE = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (
#     user_name,
#     user_pwd,
#     db_host,
#     db_name,
# )