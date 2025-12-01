"""
Simple data processing application.
Connects to database and external APIs to process data.
"""

import config


def connect_to_database():
    """Connect to the production database."""
    print(f"Connecting to database at {config.DB_HOST}:{config.DB_PORT}")
    print(f"Database: {config.DB_NAME}")
    print(f"User: {config.DB_USER}")
    # In a real app, we would use psycopg2 here
    # connection = psycopg2.connect(
    #     host=config.DB_HOST,
    #     port=config.DB_PORT,
    #     user=config.DB_USER,
    #     password=config.DB_PASSWORD,
    #     database=config.DB_NAME
    # )
    return {"status": "connected", "host": config.DB_HOST}


def fetch_data_from_api():
    """Fetch data from external API using OpenAI."""
    print(f"Using OpenAI API key: {config.OPENAI_API_KEY[:10]}...")
    print(f"AWS Region: {config.AWS_REGION}")
    # In a real app, we would call the OpenAI API
    # client = openai.OpenAI(api_key=config.OPENAI_API_KEY)
    return {"data": "sample_data", "source": "api"}


def process_data(data):
    """Process the fetched data."""
    print(f"Processing data: {data}")
    print(f"Using encryption key for secure processing...")
    # Simulate data processing
    processed = {
        "original": data,
        "processed": True,
        "encrypted": True
    }
    return processed


def main():
    """Main application entry point."""
    print("=" * 50)
    print("Starting data processing application...")
    print("=" * 50)

    # Connect to database
    db_connection = connect_to_database()
    print(f"Database connection: {db_connection}")

    # Fetch data from API
    api_data = fetch_data_from_api()
    print(f"API data received: {api_data}")

    # Process the data
    result = process_data(api_data)
    print(f"Processing result: {result}")

    print("=" * 50)
    print("Application finished successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()
