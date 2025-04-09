from flask import Flask, request, render_template_string
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongo:27017/")
db = client["test"]
users = db["users"]

login_page = '''
<h2>Login</h2>
<form method="POST">
  Username: <input name="username"><br>
  Password: <input name="password"><br>
  <input type="submit" value="Login">
</form>
<p>{{ result }}</p>
'''

@app.route('/', methods=["GET", "POST"])
def login():
    result = ""
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        
        query = {"username": username, "password": password}
        user = users.find_one(query)
        
        if user:
            result = f"Welcome, {user['username']}!"
        else:
            result = "Login failed."

    return render_template_string(login_page, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
