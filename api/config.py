from dotenv import load_dotenv
import os

load_dotenv()

FMCSA_BASE_URL = "https://mobile.fmcsa.dot.gov/qc/services"
FMCSA_WEB_KEY = os.getenv("FMCSA_WEB_KEY")

if not FMCSA_WEB_KEY:
    raise RuntimeError("FMCSA_WEB_KEY is not set")
