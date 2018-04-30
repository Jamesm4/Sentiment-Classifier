import sys

TRAIN_N = 5000
TEST_N = 1000

def cleanContent(content):

  cleaned = content.replace('"', "")
  cleaned = cleaned.replace('[', "")
  cleaned = cleaned.replace(']', "")
  cleaned = cleaned.replace(',', " ")
  cleaned = cleaned.replace('\n', "")
  cleaned = cleaned.lstrip()
  cleaned = ' '.join(cleaned.split())

  return cleaned

class Data:

  def __init__(self, row):

    row = row.rstrip()

    self.sentiment = ""
    self.content = ""

    dashes = 0
    for c in row:
      if c == "-": dashes += 1
      elif dashes >= 3 and dashes < 6: self.sentiment += c
      elif dashes >= 6: self.content += c

    self.content = cleanContent(self.content)

  def write(self, fp):
    fp.write(self.content + "," + self.sentiment + "\n")

dirty = open("./data/isear.txt")
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

