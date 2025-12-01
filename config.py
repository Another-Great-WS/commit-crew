"""
Application configuration.
Database connection settings and API keys.
"""

# Database credentials
DB_HOST = "prod-db.company-internal.com"
DB_PORT = 5432
DB_USER = "admin"
DB_PASSWORD = "SuperSecret123!"
DB_NAME = "production_data"

# AWS credentials
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
AWS_REGION = "eu-west-1"

# OpenAI API
OPENAI_API_KEY = "sk-proj-abc123def456ghi789jkl012mno345pqr678stu901vwx234"

# Security keys
JWT_SECRET = "my-super-secret-jwt-key-dont-share"
ENCRYPTION_KEY = "aes256-encryption-key-very-secret"
