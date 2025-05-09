from flask import Flask, request, Response, render_template
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
    else:
        github_url = f"https://github.com/{username}"
        response = requests.get(github_url)
        text = response.text[:80000]
        return text

@app.route('/svgtest')
def svg():
    name = request.args.get('username')
    if not name:
        pass
    login = request.args.get('login')
    if not login:
        pass
    public_repos = request.args.get('prepos')
    if not pubic_repos:
        pass
    following = request.args.get('following')
    if not following:
        pass
    followers = request.args.get('followers')
    if not followers:
        pass
    avatar_url = request.args.get('avturl')
    if not avatar_url:
        pass
    return Response(
        render_template("card.svg", 
                        name,
                        login,
                        public_repos,
                        followers,
                        following,
                        avatar_url,
        mimetype="image/svg+xml"
    )
    

@app.route('/api/github-stats')
def github_stats():
    username = request.args.get('username')
    if not username:
        return {"error": "Please provide a username"}, 400

    github_api_url = f"https://api.github.com/users/{username}"
    response = requests.get(github_api_url)
    
    return response.text[:1000]
