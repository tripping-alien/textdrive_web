from flask import Flask, render_template, send_from_directory

# Serve files from the 'static' directory at the root URL
app = Flask(__name__, static_url_path='')

@app.route('/')
def home():
    return render_template('index.html')

# Add a route for favicon.ico to serve the emoji SVG
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.svg', mimetype='image/svg+xml')

if __name__ == '__main__':
    app.run(debug=True)
