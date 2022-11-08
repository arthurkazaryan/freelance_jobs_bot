from dotenv import load_dotenv
import os

load_dotenv()

DJANGO_SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
