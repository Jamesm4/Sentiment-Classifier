import sys

TRAIN_N = 5000
TEST_N = 1000

def removeEntities(text):

  def clean(word):
    if "@" in word: return "NAME"
    elif "http:" in word: return "LINK"
    elif "#" in word: return "HASHTAG"
    else: return word

  return ' '.join(map(clean, text.split()))

class Data:

  def __init__(self, row):

    split = row.split(",")

    self.tweet_id = split[0]
    self.sentiment = split[1].replace('"', '')
    self.author = split[2].replace('"', '')
    self.content = ' '.join(split[3:]).replace('"', '').replace("\n", "").lower()
    self.content = removeEntities(self.content)

  def write(self, fp):
    fp.write(self.content + "," + self.sentiment + "\n")

dirty = open("./data/text_emotion.csv")
next(dirty)
train = open("./data/train.csv", "w")
test = open("./data/test.csv", "w")

for i, line in enumerate(dirty):
  if i == TRAIN_N + TEST_N: break

  d = Data(line)
  out = train if i < TRAIN_N else test
  d.write(out)

print("Cleaned " + str(TRAIN_N + TEST_N) + " rows of data.")

dirty.close()
train.close()
test.close()

