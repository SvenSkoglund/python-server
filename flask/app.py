from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/<string:page>")
def page_route(page):
    return render_template(page)

@app.route("/")
def my_home():
    return render_template("./index.html")

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect("/thankyou.html")
    else:
        return "Something went wrong"

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')