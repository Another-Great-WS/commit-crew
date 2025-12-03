"""
Application configuration.
Database connection settings and API keys.

This file demonstrates how to use environment variables for sensitive data.
In production, NEVER hardcode credentials!
"""

import os

# Database credentials
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = int(os.environ.get("DB_PORT", 5432))
DB_USER = os.environ.get("DB_USER", "")
DB_NAME = os.environ.get("DB_NAME", "")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")

# AWS credentials (from environment)
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
AWS_REGION = os.environ.get("AWS_REGION", "eu-west-1")

# OpenAI API (from environment)
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

# Security keys (from environment)
JWT_SECRET = os.environ.get("JWT_SECRET", "")
ENCRYPTION_KEY = os.environ.get("ENCRYPTION_KEY", "")
