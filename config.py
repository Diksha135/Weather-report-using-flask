import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OWM_API_KEY = os.getenv("OWM_API_KEY")
    CACHE_TIMEOUT = int(os.getenv("CACHE_TIMEOUT", 600))
    RATELIMIT_DEFAULT = "60 per minute"
