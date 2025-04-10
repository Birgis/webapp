from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def hello():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/flask')
def flask():
    return render_template('flask.html')

if __name__ == '__main__':
    app.run(debug=True)
    
