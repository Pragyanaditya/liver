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
        gender = request.form.get('gender')
        tb = request.form.get('tb')
        db = request.form.get('db')
        aap = request.form.get('aap')
        sgpt = request.form.get('sgpt')
        sgot = request.form.get('sgot')
        tp = request.form.get('tp')
        alb = request.form.get('alb')
        ratio = request.form.get('ratio')
        res = request.form.get('result')

        result = predict(age, gender, tb, db, aap, sgpt, sgot, tb, alb, ratio, res)
        if result == 0:
            flash('result is 0', 'success')
        else:
            flash('result is 1', 'success')
    return render_template('predict.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
 