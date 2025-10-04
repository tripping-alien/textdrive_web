from flask import Flask, render_template, send_from_directory
from flask_compress import Compress

# Serve files from the 'static' directory at the root URL
app = Flask(__name__, static_url_path='')
Compress(app) # Enable Gzip compression

@app.route('/')
def home():
    return render_template('index.html')

# This route is a fallback for older browsers that strictly request /favicon.ico.
# Modern browsers will use the <link> tags in index.html.
@app.route('/favicon.ico')
def favicon_ico():
    return send_from_directory(app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)
