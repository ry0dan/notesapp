from flask import Flask , render_template, request , session
app = Flask(__name__)

notes = []
if len(notes) == 5:
	notes.pop()
@app.route('/',methods=["POST","GET"])
def home():
	message = request.form.get("tn")
	notes.append(message)
	return render_template("index.html",notes=notes)
@app.route("/about")
def about():
	return render_template("about.html")
if __name__== "__main__":
	app.secret_key = 'super secret key'
	app.run(debug=True)
