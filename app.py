from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return "<h2>This is the homepage</h2>"

@app.route('/users')
def raw_code():
    username = request.args.get('user')
    if not username:
        return "error: no username provided"
    github_url = f"https://github.com/{username}"
    response = requests.get(github_url)
    return response.text[:5000]

@app.route('/api/github-stats')
def github_stats():
    username = request.args.get('username')
    if not username:
        return {"error": "Please provide a username"}, 400

    github_api_url = f"https://api.github.com/users/{username}"
    response = requests.get(github_api_url)
    
    return response.text[:5000]
