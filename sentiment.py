import classifier
from flask import Flask
from flask import request

cl = classifier.Classifier(train=True)

app = Flask(__name__)

@app.route("/")
def test():
  return cl.test()

@app.route("/sentiment", methods=["POST"])
def sentiment():
  return cl.classify(request.form["text"])

@app.route("/sentiments", methods=["POST"])
def sentiments():
  return cl.n_classify(request.form["text"])

@app.route("/accuracy")
def accuracy():
  return str(round(cl.accuracy(), 3))
