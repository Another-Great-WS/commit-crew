"""
Simple data processing application.
Demonstrates configuration management with environment variables.

By: jose.r.andrade@inesctec.pt
Date: 2025-12-02
"""

import config


def connect_to_database():
    """
    Connection to the production database.
    
    """
    
    # Simulates an actual database connection using config values
    print(f"Connecting to database at {config.DB_HOST}:{config.DB_PORT}")
    print(f"Database: {config.DB_NAME}")
    print(f"User: {config.DB_USER}")
    return {"status": "connected", "host": config.DB_HOST}


def fetch_data_from_api():
    """
    Fetch data from external API.
    """
    # Simulates an API call using the API key from config
    api_key = config.OPENAI_API_KEY
    if api_key:
        print(f"Using API key: {api_key[:10]}...")
    else:
        print("No API key configured")
    # Simulate AWS region usage
    print(f"AWS Region: {config.AWS_REGION}") # Simulates AWS region usage
    return {"data": "sample_data", "source": "api"}


def process_data(data):
    """
    Process the fetched data.
    
    """
    print(f"Processing data: {data}")
    
    # Add extra processing layer
    quick_math = 10 # is this even possible?
    
    processed = {
        "original": data,
        "processed": True
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
