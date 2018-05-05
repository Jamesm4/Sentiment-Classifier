# Sentiment-Classifier

This is a sentiment classification API, created for as a term project for RPI Natural Language Processing Spring 2018.

There are seven possible emotions: guilt, anger, sadness, joy, shame, fear, and disgust.

| Test Set | Accuracy |
| -------- | -------- |
| Train | 83.46% |
| Test | 51% |

* Note: Windows users should change `python3` to `python` in `start.sh`

## Requirements
- [Python 3.6](https://www.python.org/)
- [Flask](http://flask.pocoo.org/)
- [Textblob](http://textblob.readthedocs.io/en/dev/)
  
## Scripts

- Create the train and test files (already done): `python clean.py`
- Test the classifier without running the server `python classifier.py`
- Start the server `python sentiment.py`
- Interactively classify sentences `./start.sh`

## API Routes

| Route | HTTP Method | Return Type | Description | Example Return |
| ----- | ----------- | ----------- | ----------- | -------------- |
| / | GET | String | Classifies "This is a test sentence." | "joy" |
| /sentiment | POST | String | Classifies the sentence in the "text" for field. | "sadness" |
| /sentiments | POST | JSON | Returns the probabiltiy of each emotion over a minimum threshold over 10%. | {'sentiments': [{'disgust': 0.41}, {'sadness': 0.20}, {'shame': 0.18}]} |
| /accuracy | GET | JSON | Tests the accuracy of the classifier on the train and test datasets. | {"train_accuracy": 0.8346, "test_accuracy": 0.51}
| /labels | GET | JSON | Returns the set of all possible classifications. | {"labels": ["guilt", "anger", "sadness", "joy", "shame", "fear", "disgust"]}


Dataset courtesy of [Emotion Research](http://emotion-research.net/toolbox/toolboxdatabase.2006-10-13.2581092615)

