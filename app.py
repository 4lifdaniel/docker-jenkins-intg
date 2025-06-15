from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>This page is deployed using Jenkins,,,,</h1>"

if __name__ == "__main__":
    # Set host to 0.0.0.0 to make the server externally visible if needed
    app.run(host="0.0.0.0", port=5000, debug=True)
