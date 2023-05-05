import pandas as pd
import joblib
import random

df = pd.read_csv("dataset.csv")

# Define a function to prompt the user for the severity and treatment of their symptoms
def prompt_user():
    #severity = input("What is the severity of your dog's symptoms? (Mild, Moderate, Severe): ")
    #treatment = input("What treatment has your dog received for these symptoms? (None, Antibiotics, Steroids): ")
    symptoms = [0 for i in range(len(df.columns[1:-2]))]
    
    for index, symptom in enumerate(df.columns[1:-2]):
        #symptoms.append(random.choice([0, 1]))

        response = input(f"Does your dog have {symptom.lower()}? (y/n): ")
        symptoms[index] = (1 if (response.lower() == 'y') else 0)

    predict(symptoms)

# Define a function to make predictions using the decision tree models
def predict(symptoms):
    #severity = input("What is the severity of your dog's symptoms? (Mild, Moderate, Severe): ")
    #disease = input("What do you think your dog has as a disease? (None, Antibiotics, Steroids): ")

    # Load the trained models from disk
    sev_tree = joblib.load("severity_model.joblib")
    dis_tree = joblib.load("Treatment_model.joblib")
    
    # Make a prediction for the disease of the symptoms
    dis_pred = dis_tree.predict([symptoms])[0]
    '''if dis_pred == disease.lower():
        dis_confidence = dis_tree.predict_proba([symptoms]).max()
        dis_msg = f"The disease of your dog's symptoms is {disease}."
    else:'''
    dis_msg = f"The disease of your dog's symptoms is more likely {dis_pred}."

    print(dis_msg)
    
    # Make a prediction for the severity of the symptoms
    sev_pred = sev_tree.predict([symptoms])[0]
    '''if sev_pred == severity.lower():
        sev_confidence = sev_tree.predict_proba([symptoms]).max()
        sev_msg = f"The severity of your dog's symptoms is {severity}."
    else:'''
    sev_msg = f"The severity of your dog's disease is more likely {sev_pred}."

    # return sev_msg
    print(sev_msg)
    return dis_msg+" "+sev_msg