from flask import Flask
from flask import render_template

# Create Flask App
app = Flask(__name__)

# Create Index.html Route
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/scott')
def scott():
    return render_template('scott.html')

@app.route('/sam')
def sam():
    return render_template('sam.html')

@app.route('/calvin')
def calvin():
    return render_template('calvin.html')

@app.route('/tiffany')
def tiffany():
    return render_template('tiffany.html')

# Run App
if __name__ == "__main__":
    app.run(debug=True)