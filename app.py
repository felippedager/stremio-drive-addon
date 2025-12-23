from flask import Flask, jsonify
import os

app = Flask(__name__)

# Manifesto do addon
MANIFEST = {
    "id": "org.stremio.gdrive.personal",
    "version": "1.0.0",
    "name": "Google Drive Personal",
    "description": "Addon pessoal para reproduzir vídeos do Google Drive",
    "logo": "https://stremio.com/website/static/img/stremio-logo-small.png",

    "resources": [
        "stream"
    ],

    "types": [
        "movie",
        "series"
    ],

    "catalogs": [],

    "idPrefixes": [
        "gdrive:"
    ],

    "behaviorHints": {
        "configurable": False
    }
}


# Rota para fornecer o manifest
@app.route('/manifest.json')
def manifest():
    return jsonify(MANIFEST)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
