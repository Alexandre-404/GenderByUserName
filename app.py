from flask_cors import CORS,cross_origin
from flask import Flask,render_template, redirect, url_for, request
import pandas as pd
import numpy as np
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle
import joblib

#----Titulo---> O o codigo em estado de comentario é relativo ao treinamento dos modelos, remove os "#" caso queira treinar com outra dataset ou mudar o modelo


#-------> Preparacao do dataset a ser usado
# data = pd.read_csv("nomes.csv")
# data.drop("group_name",axis=1, inplace=True)
# data['frequency_female'] = data['frequency_female'].fillna(0)
# data['frequency_male'] = data['frequency_male'].fillna(0)
# x_train,x_test,y_train,y_test = train_test_split(data['alternative_names'],data['classification'],test_size=0.25,random_state=7,shuffle=True)

#-------> Transformando todos os dados na tabela em um vector by* demencional
# tfidf_vectorizer = TfidfVectorizer(stop_words='english',max_df=0.75)

vectorizer = joblib.load("./trainedModels/tfidf_vectorizer.pickle")

#-------> Transformando os dados tipo string em int.
# vec_train = tfidf_vectorizer.fit_transform(x_train.values.astype('U'))
# vec_test = tfidf_vectorizer.transform(x_test.values.astype('U'))
#-------> Salvar o classificador
# pickle.dump(tfidf_vectorizer, open("./trainedModels/tfidf_vectorizer.pickle", "wb"))

#-------> Treinando o modelo com os dados já transformados e salvando eles
# pac = PassiveAggressiveClassifier(max_iter=50)
vectorizerPac = joblib.load("./trainedModels/passiveAgressive.pickle")
# pac.fit(vec_train,y_train)
# pickle.dump(pac, open("./trainedModels/passiveAgressive.pickle", "wb"))

#-------> A acuracia actual 
# 70.53%

#-------> calculando a acuracia em porcentagens
# y_pred = pac.predict(vec_test)
# score = accuracy_score(y_test,y_pred)

# print(f'Pac Accuracy :{round(score*100,2)}%')

#-------> funcao INPUT para classificar um nome
def findlabel(newtext):
    vec_newstest = vectorizer.transform([newtext])
    y_pred1 = vectorizerPac.predict(vec_newstest)
    return y_pred1[0]

print(findlabel("Marina Santeago Francisco"))

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/api/v0.1/',methods = ['POST', 'GET'])
def api():
    if request.method == 'POST':
      user = request.form['username']
      return findlabel(user)
    else:
       user = request.args.get('username')
       return findlabel(user)

