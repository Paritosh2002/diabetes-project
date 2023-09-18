from flask import Flask,render_template,request,flash,redirect, url_for

app = Flask(__name__)
app.secret_key = '162'
@app.route('/')
def main():
    return render_template('login.html')
@app.route('/index')
def main_page():
    return render_template('index.html')

@app.route('/evaluation')
def evaluation():
    return render_template('evaluation.html')
@app.route('/index',methods=['POST'])
def collect_info():
    if request.method == 'POST':
        age = request.form["age"]
        bs_fast = request.form["bs_fast"]
        bs_pp = request.form["bs_pp"]
        plasma_r = request.form["plasma_r"]
        plasma_f = request.form["plasma_f"]
        hb1ac = request.form["hb1ac"]
        
        if not age or not bs_fast or not bs_pp or not plasma_r or not plasma_f or not hb1ac:
            flash('All fields are required')
            return redirect(url_for('main_page'))  # Redirect to the main page (index.html)
        else:
            return redirect(url_for('evaluation'))  # Redirect to the evaluation page
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)