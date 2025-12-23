from flask import Flask, jsonify
import os

app = Flask(__name__)

MANIFEST = {
    "id": "org.stremio.gdrive.personal",
    "version": "1.0.0",
    "name": "Google Drive Personal",
    "description": "Addon pessoal para vídeos do Google Drive",
    "logo": "https://stremio.com/website/static/img/stremio-logo-small.png",
    "resources": ["stream"],
    "types": ["movie", "series"],
    "catalogs": [],
    "behaviorHints": {"configurable": False}
}

@app.route('/manifest.json')
def manifest():
    return jsonify(MANIFEST)

@app.route('/stream/<type>/<id>.json')
def stream(type, id):
    return jsonify({"streams": []})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
