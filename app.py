from flask import Flask, request, render_template
import json
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import pandas as pd

app = Flask(__name__)

def analyse_text(text) :
	df = pd.read_csv('df_sentiment_analysis.csv')
	tfidf_vect = TfidfVectorizer(max_features=5000)
	tfidf_vect.fit(df['text_final'])
	loaded_model = pickle.load(open('sentiment_analysis_model.sav', 'rb'))
	return loaded_model.predict(tfidf_vect.transform([text]))[0]


def analyse(text):
	
	sentiment = analyse_text(text)
	if sentiment == 1:
		return render_template('index.html', result = '😀')
	elif sentiment == 0:
		return render_template('index.html', result = '😐')
	else:
		return render_template('index.html', result = '☹️')
	

	
	
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		details = request.form
		return analyse(details['text-to-analyse'])

	return render_template('index.html', result = '')

if __name__ == '__main__':
	app.run(host='0.0.0.0')
	
	
	
	
	
