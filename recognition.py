import pickle
import json
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem.wordnet import WordNetLemmatizer

wnl = WordNetLemmatizer()

nltk.download('omw-1.4')
nltk.download("punkt")
nltk.download("wordnet")

words = []
classes = []
documents = []
ignore_words = ["?", "!", ","]
data_file = open("intents.json").read()
intents = json.loads(data_file)

for intent in intents["intents"]:
    for pattern in intent["patterns"]:

        # take each word and tokenize it
        w = nltk.word_tokenize(pattern)
        words.extend(w)

        # adding documents
        documents.append((w, intent["name"]))

        # adding classes to our class list
        if intent["name"] not in classes:
            classes.append(intent["name"])

words = [wnl.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

classes = sorted(list(set(classes)))

print(len(documents), "documents")

print(len(classes), "classes", classes)

print(len(words), "unique lemmatized words", words)


pickle.dump(words, open("words.pkl", "wb"))
pickle.dump(classes, open("classes.pkl", "wb"))