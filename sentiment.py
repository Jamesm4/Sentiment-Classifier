import classifier
from flask import Flask
from flask import request
from werkzeug.contrib.cache import SimpleCache

cache = SimpleCache()
cl = classifier.Classifier()

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
  acc = cache.get("accuracy")
  if acc is None:
    acc = cl.accuracy()
    cache.set("accuracy", acc)
  return acc

@app.route("/labels")
def labels():
  return cl.labels()

