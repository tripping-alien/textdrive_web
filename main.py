from flask import Flask, render_template, send_from_directory, jsonify, Response
from flask_compress import Compress
import json
import os

# Serve files from the 'static' directory at the root URL
app = Flask(__name__, static_url_path='')
Compress(app) # Enable Gzip compression

@app.route('/')
def home():
    return render_template('index.html')

# --- Explicit Icon Routes for Maximum Compatibility ---
@app.route('/favicon.svg')
def favicon_svg():
    return send_from_directory(app.static_folder, 'favicon.svg', mimetype='image/svg+xml')

@app.route('/icon.png')
def icon_png():
    return send_from_directory(app.static_folder, 'icon.png', mimetype='image/png')

@app.route('/favicon.ico')
def favicon_ico():
    return send_from_directory(app.static_folder, 'icon.png', mimetype='image/png')
# --- End of Icon Routes ---

# Dynamically generate the robots.txt file
@app.route('/robots.txt')
def robots_txt():
    content = (
        "User-agent: *\n"
        "Allow: /\n\n"
        "User-agent: Googlebot\n"
        "Allow: /\n\n"
        "User-agent: Yandex\n"
        "Allow: /\n\n"
        "User-agent: bingbot\n"
        "Allow: /\n"
    )
    return Response(content, mimetype='text/plain')

# Add a specific route for Digital Asset Links that reads the file directly
@app.route('/.well-known/assetlinks.json')
def asset_links():
    try:
        json_path = os.path.join('.well-known', 'assetlinks.json')
        with open(json_path) as json_file:
            data = json.load(json_file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "assetlinks.json not found at the expected path."}), 404

if __name__ == '__main__':
    app.run(debug=True)
