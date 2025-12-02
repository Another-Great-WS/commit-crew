# from-lab-to-hub

A simple data processing application for workshop demonstration purposes.

## Project Status

![Status](https://img.shields.io/badge/status-active-brightgreen)

This project is actively maintained for workshop demonstration purposes.

## Technology Stack

- **Language:** Python 3.x
- **Database:** PostgreSQL
- **Cloud Services:** AWS (S3, EC2)
- **AI Integration:** OpenAI API

## Dependencies

No external dependencies required - uses only Python standard library.

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd from-lab-to-hub
```

2. Configure environment variables (optional):
```bash
cp .env.example .env

# On Windows (PowerShell), use "copy .env.example .env"

# Edit .env with your actual credentials
```

3. Run the application:
```bash
python app.py
```

## Architecture Diagrams

![Architecture Diagram](docs/architecture.png)

## Known Issues

- This is a demonstration project; database connections are simulated
- API calls are mocked and do not make real requests

## License

MIT License

## Documentation and Resources

- [Python os.environ documentation](https://docs.python.org/3/library/os.html#os.environ)
- [12-Factor App - Config](https://12factor.net/config)

## Credits and Acknowledgments

- INESC TEC - Center for Power and Energy Systems (CPES)
- Workshop participants and contributors
