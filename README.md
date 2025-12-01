# from-lab-to-hub

A simple data processing application for workshop demonstration purposes.

## Description

This application demonstrates a typical Python project that:
- Connects to a PostgreSQL database
- Integrates with external APIs (AWS, OpenAI)
- Processes and encrypts data

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd from-lab-to-hub
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your actual credentials
```

## Configuration

Copy `.env.example` to `.env` and fill in your credentials:

- `DB_HOST`: Database host address
- `DB_PORT`: Database port (default: 5432)
- `DB_USER`: Database username
- `DB_PASSWORD`: Database password
- `DB_NAME`: Database name
- `AWS_ACCESS_KEY_ID`: AWS access key
- `AWS_SECRET_ACCESS_KEY`: AWS secret key
- `AWS_REGION`: AWS region (default: eu-west-1)
- `OPENAI_API_KEY`: OpenAI API key
- `JWT_SECRET`: Secret key for JWT tokens
- `ENCRYPTION_KEY`: Key for data encryption

## Usage

Run the application:
```bash
python app.py
```

## Project Structure

```
from-lab-to-hub/
├── app.py              # Main application
├── config.py           # Configuration management
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Security Note

Never commit sensitive credentials to version control. Always use environment variables for secrets and API keys.

## License

MIT License
