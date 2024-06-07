from flask import Flask, render_template, request, flash
from instagrapi import Client
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# SOCKS5 proxy configuration
PROXY = "http://kku0zhd78jcpb1l-country-il-state-hamerkaz-city-netanya-sid-70106545:3p8dSlqh51QZI0T@resi.rainproxy.io:9090"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    username = request.form['username']
    password = request.form['password']
    caption = request.form['caption']
    video_path = "/home/PostIT/mysite/videotest.mp4"
    thumbnail_path = "/home/PostIT/mysite/working.png"

    client = Client()

    # Test proxy configuration
    try:
        session = requests.Session()
        session.proxies = {
            "http": PROXY,
            "https": PROXY
        }
        test_response = session.get("http://www.google.com")
        if test_response.status_code == 200:
            print("Proxy configuration is working.")
        else:
            print("Failed to connect through proxy.")
            flash("Failed to connect through proxy.", "danger")
            return render_template('index.html')
    except Exception as e:
        flash(f"Proxy configuration error: {e}", "danger")
        print(f"Proxy configuration error: {e}")
        return render_template('index.html')

    client.private.requests = session

    try:
        print("Logging in to Instagram...")
        client.login(username, password)
        print("Login successful, uploading video...")

        client.clip_upload(
            video_path,
            caption=caption,
            thumbnail=thumbnail_path
        )
        flash("Video uploaded successfully!", "success")
    except Exception as e:
        flash(f"An error occurred: {e}", "danger")
        print(f"An error occurred: {e}")  # Additional logging for debugging

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
