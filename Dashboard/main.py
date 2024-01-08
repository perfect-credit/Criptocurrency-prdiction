from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

data = pd.read_csv('data.csv')

@app.route('/')
def dashboard():
    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
