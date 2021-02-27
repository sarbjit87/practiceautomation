from flask import render_template, request, Blueprint
from app import db

automation_bp = Blueprint('automation_bp', __name__, template_folder='templates')

@automation_bp.route("/automation/signup", methods=["GET", "POST"])
def signupform():
    if request.method == "POST":
        returndict = {}
        email = request.form['email']
        password = request.form['password']
        country = request.form['country']
        sports = request.form.getlist('sports')
        about = request.form['about']
        coupon = request.form['coupon']

        if request.form.get('general_newsletter'):
            returndict['general_newsletter'] = True

        if request.form.get('technical_newsletter'):
            returndict['technical_newsletter'] = True

        returndict['email'] = email
        returndict['password'] = password
        returndict['country'] = country
        returndict['sports'] = sports
        returndict['about'] = about
        returndict['coupon'] = coupon



        print(returndict)

        return render_template('automation/signupresults.html', title='Signup', results=returndict)



    return render_template('automation/signup.html', title='Signup')
