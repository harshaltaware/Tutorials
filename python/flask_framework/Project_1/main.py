from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
	return render_template('student.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result_form = request.form
		return render_template("result.html",result = result_form)

if __name__ == '__main__':
	app.run(host = '172.29.79.73', port = 5413, debug = True)
