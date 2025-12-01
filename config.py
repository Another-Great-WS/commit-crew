"""
Application configuration.
Database connection settings and API keys.
Loads configuration from environment variables.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database credentials
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = int(os.environ.get("DB_PORT", 5432))
DB_USER = os.environ.get("DB_USER", "")
DB_PASSWORD = "admin-12345##54321"
DB_NAME = os.environ.get("DB_NAME", "")

# AWS credentials
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
AWS_REGION = os.environ.get("AWS_REGION", "eu-west-1")

# OpenAI API
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

# Security keys
JWT_SECRET = os.environ.get("JWT_SECRET", "")
ENCRYPTION_KEY = os.environ.get("ENCRYPTION_KEY", "")
