import os
import requests


# Haal SECRET_KEY op uit de omgevingsvariabelen
SECRET_KEY="TEST"

def greet():
    print("Hello, World!")

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
