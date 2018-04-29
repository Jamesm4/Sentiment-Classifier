import json
import pickle
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob.classifiers import MaxEntClassifier

class Classifier:

  def __init__(self, train=True):
    if train:
      fp = open("./data/train.csv")
      self.cl = NaiveBayesClassifier(fp, format="csv")
      # self.cl = MaxEntClassifier(fp, format="csv")
      fp.close()

      # fp = open("./data/classifier.pickle", "wb")
      # pickle.dump(self.cl, fp, -1)
      # fp.close()
    else:
      fp = open("./data/classifier.pickle", "rb")
      self.cl = pickle.load(fp)
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
  cl = Classifier(train=True)
  print(cl.test())

if __name__ == "__main__":
    main()

