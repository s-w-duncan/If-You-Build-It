from flask import Flask
from flask import render_template

# Create Flask App
app = Flask(__name__)

# Create Index.html Route
@app.route("/")
def home():
    return render_template('index.html')

# Run App
if __name__ == "__main__":
    app.run(debug=True)