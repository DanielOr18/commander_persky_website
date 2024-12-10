# Commander Persky Website

## Project Description
A Django-based website for the Commander Persky game, showcasing game information, statistics, and interactive features.

## Prerequisites
- Python 3.10.5
- Django 5.1.4
- pip

## Setup and Installation
1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Copy `.env.production` to `.env`
   - Update secret key and other sensitive information

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

## Deployment
Configured for PythonAnywhere with:
- Gunicorn
- WhiteNoise for static files
- SQLite database

## Features
- Game statistics tracking
- Responsive design
- Secure configuration

## Contributing
Please read the contribution guidelines before submitting pull requests.

## License
[Specify your license here]