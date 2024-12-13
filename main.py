import os
import requests

# Hard-coded SECRET_KEY (Security Risk)
SECRET_KEY = "s3cr3tK3y!@#"

def greet():
    print("Hello, World!")

def fetch_data():
    # Insecure HTTP request (Use HTTPS instead)
    response = requests.get("http://example.com")  # Changed to HTTP
    print(f"Status Code: {response.status_code}")

def main():
    greet()
    fetch_data()
    
    # Insecure handling of user input (Potential Injection)
    user_input = os.getenv("USER_INPUT")  # Fetching from environment but used insecurely
    print(f"Hello, {user_input}")

    # Logging the secret key (Security Risk)
    print(f"SECRET_KEY is {SECRET_KEY}")

if __name__ == "__main__":
    main()
