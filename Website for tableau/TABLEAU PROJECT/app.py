from flask import Flask, render_template

# Use double underscores: __name__
app = Flask(__name__)

@app.route('/')
def home():
    # Ensure index.html is inside a folder named 'templates'
    return render_template('index.html')

# Use double underscores: __name__ and __main__
if __name__ == '__main__':
    app.run(debug=True, port=5000)