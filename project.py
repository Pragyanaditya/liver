from flask import Flask, render_template,request, flash, redirect, url_for, session, logging
app = Flask(__name__)
app.secret_key = "liverdisease"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET'])
def patient_detail_form():
    return render_template('form.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        sex = request.form.get('sex')
        trest = request.form.get('trest')
        trestbps = request.form.get('trestbps')
        chol = request.form.get('chol')
        c = request.form.get('c')
        ch = request.form.get('ch')
        thalach = request.form.get('thalach')
        exang = request.form.get('exang')
        exa = request.form.get('exa')
        ratio = request.form.get('ratio')

        result = predict(age, sex, trest, trestbps, chol, c, ch, thalach, exang, exa, ratio)
        if result == 0:
            flash('result is 0', 'success')
        else:
            flash('result is 1', 'success')
    return render_template('predict.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
 