import random
import numpy as np
import pickle
import json
import nltk
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
from disease_predict import df, predict

lemmatizer = WordNetLemmatizer()

model = load_model("chatbot_model.h5")
intents = json.loads(open("intents.json").read())
words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))

symptoms = [0 for i in range(len(df.columns[1:-2]))]

def chatbot_response():
    isInit = False
    isRunning = True

    while(isRunning):
        if(not isInit):
            ints = predict_class("", model)
            (res, is_diagnosis) = getResponse(ints, intents)
            print(res)
            isInit = True

        else:
            msg = input("")
            ints = predict_class(msg, model)
            (res, is_diagnosis) = getResponse(ints, intents)

            if(is_diagnosis):
                print("ssssssss")
                print(symptoms)

                print(predict(symptoms))
                isRunning = False
            else:
                print(res)

def yousri(msg):
    ints = predict_class(msg, model)
    (res, is_diagnosis) = getResponse(ints, intents)
    if(is_diagnosis):
        print("======================bb======================")
        return predict(symptoms)
    else:
        return ({"resultat":res})
# chat functionalities
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return np.array(bag)


def predict_class(sentence, model):
    # filter out predictions below a threshold
    print(type(sentence))
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def getResponse(ints, intents_json):
    name = ints[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["name"] == name:
            if not(name == "Unknown" or name == "greetings" or name == "Goodbye" or name == "Diagnosis"):
                arr = df.columns[1:-2].to_numpy()
                arr = [element.lower() for element in arr]

                index = list(arr).index(name.lower())
                symptoms[index] = 1

            result = random.choice(i["responses"])
            break
    return (result, (name == "Diagnosis"))

chatbot_response()