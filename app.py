from flask import Flask, request, render_template
import json

app = Flask(__name__)

def analyse(text):
	if text == '1':
		return render_template('index.html', result = '😀')
	elif text == '2':
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
	
	
	
	
	