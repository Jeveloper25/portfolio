import re
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
import csv

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/<string:page_name>', methods=['POST', 'GET'])
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
     with open('./database.txt', 'a') as db:
            db.write(f"[\nEmail:\n{data['email']}\nName:\n{data['name']}\nMessage:\n{data['message']}\n]\n")

def write_to_csv(data):
     with open('./database.csv', 'a', newline='') as db:
            email = data['email']
            name = data['name']
            message = data['message']
            csv_writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email, name, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thank_you.html')
        except:
            return 'Database Error occured'
    else:
        return 'Request Error occured'

# @app.route('/index.html')
# def home_page():
#     return render_template('index.html')

# @app.route('/left-sidebar.html')
# def left_bar():
#     return render_template('left-sidebar.html')

# @app.route('/right-sidebar.html')
# def right_bar():
#     return render_template('right-sidebar.html')

# @app.route('/no-sidebar.html')
# def no_bar():
#     return render_template('no-sidebar.html')


# @app.route('/elements.html')
# def elements():
#     return render_template('elements.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')



