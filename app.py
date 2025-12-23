from flask import Flask, jsonify

app = Flask(__name__)

# Manifesto do addon
MANIFEST = {
    "id": "org.stremio.driveaddon",
    "version": "1.0.0",
    "name": "Google Drive Addon",
    "description": "Addon para reproduzir vídeos do Google Drive no Stremio",
    "types": ["movie", "series"],
    "idPrefixes": ["gdrive:"]
}

# Rota para fornecer o manifest
@app.route('/manifest.json')
def manifest():
    return jsonify(MANIFEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
