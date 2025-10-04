from flask import Flask, render_template, send_from_directory, jsonify
from flask_compress import Compress
import json
import os

# Serve files from the 'static' directory at the root URL
app = Flask(__name__, static_url_path='')
Compress(app) # Enable Gzip compression

@app.route('/')
def home():
    return render_template('index.html')

# Add a route for favicon.ico to serve the emoji SVG
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.svg', mimetype='image/svg+xml')

# Add a specific route for Digital Asset Links that reads the file directly
@app.route('/.well-known/assetlinks.json')
def asset_links():
    try:
        json_path = os.path.join(app.static_folder, '.well-known', 'assetlinks.json')
        with open(json_path) as json_file:
            data = json.load(json_file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "assetlinks.json not found at the expected path."}), 404

# Add a debugging route to check file paths
@app.route('/debug-path')
def debug_path():
    json_path = os.path.join(app.static_folder, '.well-known', 'assetlinks.json')
    file_exists = os.path.exists(json_path)
    return jsonify({
        "calculated_path": json_path,
        "file_exists_at_path": file_exists,
        "static_folder_path": app.static_folder,
        "current_working_directory": os.getcwd()
    })

if __name__ == '__main__':
    app.run(debug=True)
