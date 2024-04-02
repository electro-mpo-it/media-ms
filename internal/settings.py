import os

from dotenv import load_dotenv

load_dotenv()


# S3 connection
SERVICE_NAME: str = os.getenv("SERVICE_NAME")
REGION_NAME: str = os.getenv("REGION_NAME")
ENDPOINT_URL: str = os.getenv("ENDPOINT_URL")
AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME: str = os.getenv("BUCKET_NAME")
