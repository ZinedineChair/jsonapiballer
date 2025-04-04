from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Data laden uit JSON-bestand
with open('db.json', encoding='utf-8') as f:
    data = json.load(f)

@app.route('/')
def index():
    spelers = data.get("voetbal spelers", [])
    teams = data.get("teams", [])
    return render_template('index.html', spelers=spelers, teams=teams)

@app.route('/api/spelers')
def api_spelers():
    return jsonify(data.get("voetbal spelers", []))

@app.route('/api/teams')
def api_teams():
    return jsonify(data.get("teams", []))

if __name__ == '__main__':
    app.run(debug=True)

# Bronnen:
#Flask documentatie (officieel)
# ➤ https://flask.palletsprojects.com
# Uitleg over Flask-routes, templates, renderen van data en debuggen.

# Python requests library documentatie
# ➤ https://docs.python-requests.org
# Voor het ophalen van data uit een RESTful API.

# Jinja2 templates (officiële handleiding)
# ➤ https://jinja.palletsprojects.com
# Hoe je HTML combineert met Python-data in Flask.

# my-json-server (voor het hosten van je JSON als API)
# ➤ https://my-json-server.typicode.com
# Simuleert een RESTful API vanaf een JSON-bestand op GitHub.

# JSON structuur uitleg
# ➤ https://www.json.org/json-en.html
# Basisregels en syntax van JSON-bestanden.

# ChatGPT