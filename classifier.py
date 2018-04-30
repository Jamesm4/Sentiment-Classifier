import json
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

class Classifier:

  def __init__(self):
    fp = open("./data/train.csv")
    self.cl = NaiveBayesClassifier(fp, format="csv")
    fp.close()

  def test(self):
    return self.cl.classify("This is a test sentence")

  def classify(self, text):
    return self.cl.classify(text)

  def n_classify(self, text):
    dist = self.cl.prob_classify(text)

    probs = {"sentiments": []}
    for s in dist.samples():
      if dist.prob(s) >= .10:
        probs["sentiments"].append({s: dist.prob(s)})

    return json.dumps(probs)

  def accuracy(self):
    fp = open('./data/test.csv')
    test_accuracy = self.cl.accuracy(fp, format="csv")
    fp.close()
    return test_accuracy

def main():
  cl = Classifier()
  print(cl.test())

if __name__ == "__main__":
    main()

