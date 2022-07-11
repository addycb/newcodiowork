from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

@app.route("/second_page")
def second_page():
    return render_template('second_page.html', subtitle='Second Page', text='This is the second page')
