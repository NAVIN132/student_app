# app.py
from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# Configuration - change these as needed
EC2_SERVER_URL = 'http://your-other-ec2-server-url/api/students'

@app.route('/')
def index():
    try:
        # Make a request to the other EC2 server to fetch student data
        response = requests.get(EC2_SERVER_URL)
        
        # Check if request was successful
        if response.status_code == 200:
            students = response.json()
            return render_template('index.html', students=students)
        else:
            error_message = f"Failed to fetch data: HTTP {response.status_code}"
            return render_template('error.html', error=error_message)
    
    except requests.exceptions.RequestException as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    # Use environment variables or default values
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    app.run(host=host, port=port, debug=debug)
