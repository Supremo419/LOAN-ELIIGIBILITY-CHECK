from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/',methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try: 
            monthly_income = float(request.form.get('income'))
            current_debt = float(request.form.get('debt'))

            if monthly_income > current_debt *2:
                result = "Congratulations! You are eligible for a loan."
            else:
                result = "sorry, you do not meet the eligibility criteria at this time."
        except (ValueError, TypeError):
            result = "Please fill out all the fields with Valid numbers."
    return render_template('form.html', result=result)
if __name__ =='__main__':
    app.run(debug=True)