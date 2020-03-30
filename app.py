from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route("/helloworld")
def helloworld():
	return "hello world"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/data", methods=("POST",))
def data():
	with open("comments.json", "r") as f:
		x = json.load(f)
		x.append({"name": request.form["username"], "comment": request.form["comment"]})
		print(x)
	with open("comments.json", "w") as f:
		json.dump(x, f)
	return "nice"

@app.route("/getComments", methods=("GET",))
def getComments():
	with open("comments.json", "r") as f:
		data = json.load(f)
	return jsonify(data)

app.run(debug=True, host='0.0.0.0')