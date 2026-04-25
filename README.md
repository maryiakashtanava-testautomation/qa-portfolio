QA Automation Portfolio
Test automation project for automationexercise.com built with Python and Playwright.

Tech Stack
Python 3.12
Pytest
Playwright
GitHub Actions
Project Structure

qa-portfolio/
├── tests/
│   ├── e2e/          # UI tests
│   ├── api/          # API tests
│   └── ui/pages/     # Page Object Model
├── conftest.py       # shared fixtures
├── pytest.ini        # configuration
└── requirements.txt  # dependencies
What is tested
User login and registration
Home page and navigation
Product catalog and search
REST API (products, brands, search)
How to run

# Install dependencies
pip install -r requirements.txt
playwright install chromium

# Run all tests
pytest

# Run smoke tests only
pytest -m smoke

# Run API tests only
pytest -m api
CI/CD
Tests run automatically via GitHub Actions on every push to main.
