from flask import Flask, render_template

menu = ['apple', 'banana', 'ananas']

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', title='Hello ME!', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
