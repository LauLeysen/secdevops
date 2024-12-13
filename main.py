import os
import requests # version 2.20 vulnerable

# Hard-coded SECRET_KEY (Security Risk)
SECRET_KEY = "s3cr3tK3y!@#"

def greet():
    print("Hello, World!")

def fetch_data():
    response = requests.get("https://example.com")
    print(f"Status Code: {response.status_code}")

def main():
    greet()
    fetch_data()

    # Logging the secret key (Security Risk)
    print(f"SECRET_KEY is {SECRET_KEY}")

if __name__ == "__main__":
    main()
