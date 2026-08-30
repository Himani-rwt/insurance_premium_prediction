import pickle
import pandas as pd
#import ml model
with open('model/model.pkl','rb') as f:
    model= pickle.load(f)

#MLFlow
MODEL_VERSION='1.0.0'  

#Get class labels from model(important from matching probabilities to class names)
class_labels = model.classes_.tolist()

def predict_output(user_input:dict):
    df=pd.DataFrame([user_input])
    #predict the class
    predicted_class=model.predict(df)[0]
   
   #Get probabilities of all classes
    probabilities=model.predict_proba(df)[0]
    confidence= max(probabilities)

    #create mapping:{class_name:probabilities}
    class_prob= dict(zip(class_labels,map(lambda p :round(p,4),probabilities)))
  
    return{
        "predicted_category": predicted_class,
        "confidence":round(confidence,4),
        "class_probabilities":class_prob
    }