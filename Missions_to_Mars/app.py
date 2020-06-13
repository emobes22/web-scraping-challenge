# 1. import Flask
from flask import Flask
from flask_pymongo import PyMongo

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

#2.5
#connects to your database where database name is missiontomars
app.config["MONGO_URI"]='mongodb://localhost:27017/missiontomars'
#connects db to app
mongod=PyMongo(app)

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"


# 4. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


if __name__ == "__main__":
    app.run(debug=True)
