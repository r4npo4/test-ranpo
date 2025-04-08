# app.py
from flask import Flask, request, render_template_string
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["webtest"]
users = db["users"]

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Vulnerability: No SQL Injection
        user = users.find_one({
            "username": username,
            "password": password
        })

        if user:
            return f"<h3>Login success! Hello {username}</h3>"
        else:
            return "Login failed."

    return render_template_string("""
        <form method="POST">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Login">
        </form>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
