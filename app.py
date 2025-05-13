from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/codes')
def codes():
    codename = request.args.get('code')
    if codename == 'calculator':
        return """
        num1 = input('Enter num1 ')
        num2 = input('Enter num2 ')
        print(num1+num2)
        
        """
@app.route('/api/github-stats')
def github_stats():
    username = request.args.get('username')
    if not username:
        return {"error": "Please provide a username"}, 400

    github_api_url = f"https://api.github.com/users/{username}"
    response = requests.get(github_api_url)
    
    if response.status_code != 200:
        return {"error": "User not found"}, 404

    data = response.json()
    html_card = f"""
    <div style="border:1px solid #ccc;padding:10px;font-family:sans-serif;width:300px;">
        <h2>{data['name']} ({data['login']})</h2>
        <p>Public Repos: {data['public_repos']}</p>
        <p>Followers: {data['followers']}</p>
        <p>Following: {data['following']}</p>
    </div>
    """
    return Response(html_card, mimetype='text/html')
