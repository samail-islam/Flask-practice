from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/api/github-stats')
def github_stats():
    username = request.args.get('username')
    if not username:
        return {"error": "Please provide a username"}, 400

    github_api_url = f"https://api.github.com/users/{username}"
    response = requests.get(github_api_url)
    
    return response.text[:500]
