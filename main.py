import os
import requests
from dotenv import load_dotenv

# Laad de variabelen uit het .env bestand
load_dotenv()

# Haal SECRET_KEY op uit de omgevingsvariabelen
SECRET_KEY = os.getenv("SECRET_KEY")

def greet():
    print("Hello, World!") # hi

def fetch_data():
    response = requests.get("https://example.com")
    print(f"Status Code: {response.status_code}")

def main():
    greet()
    fetch_data()
    user_input = "hello"
    print(f"Hello, {user_input}")

if __name__ == "__main__":
    main()
