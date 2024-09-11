
# DoS Attack Simulation on a Python Flask Web Server

## Contributions
- **Rendyta Moristadella :** Initial setup of the Flask web server and integration of the basic calculator functionality.
- **M. Chandra Agoeng P :** Developed the DoS attack simulation script and optimized the attack methods.
- **Nashrillah Khairu Daffa :** Enhanced server performance and implemented additional security measures for testing.
- **Asyraf Nur Ardliansyah :** Handling reports for DoS attack simulation on a python flask web server

This repository contains two Python scripts:
1. `webserver.py`: A simple Flask-based web server that provides a basic calculator.
2. `importrequests2.py`: A script designed to simulate a Denial of Service (DoS) attack on the web server.

## Prerequisites
- Python 3.x installed on your system
- Flask library for the web server
- `requests` library for the DoS attack script

You can install the required libraries using pip:
```bash
pip install flask requests
```

## 1. Deploying the Web Server

To deploy the web server, run the following command:

```bash
python webserver.py
```

The server will be accessible on your local network at `http://0.0.0.0:5000` or via your machine's IP address.

### Web Server Features
- Simple calculator functionality (Addition, Subtraction, Multiplication, Division).
- Handles basic HTTP GET and POST requests.

## 2. Simulating a DoS Attack

To simulate a DoS attack on the web server, execute the following command:

```bash
python importrequests2.py
```

This script will flood the server with HTTP requests, attempting to overwhelm it.

### Important Notice
**This script should only be used for educational purposes in a controlled environment. Unauthorized use of this script against third-party servers is illegal and unethical.**

## Repository Contents
- `webserver.py`: The Flask-based web server script.
- `importrequests2.py`: The DoS attack script.
- `README.md`: This documentation file.
