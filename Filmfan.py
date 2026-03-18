from flask import Flask, render_template,redirect
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,EqualTo
from wtforms import EmailField, PasswordField, StringField, SubmitField, DateField
app = Flask(__name__)
app.config["SECRET_KEY"] = "123"      #Acceptabel voor dit project maar normaal niet verstandig

#Homepage
@app.route("/")
def home():
    return render_template("filmfan1.html")

#Loginformulier velden
class LoginForm(FlaskForm):
    email = EmailField(validators=[DataRequired()],render_kw={"placeholder":"Email"})
    wachtwoord = PasswordField(validators =[DataRequired()],render_kw={"placeholder":"Wachtwoord"})
    submit = SubmitField("Inloggen",render_kw={"class": "btn login-button"})

class RegistrationForm(FlaskForm):
    username = StringField(validators=[DataRequired()],render_kw={"placeholder":"Gebruikersnaam"})
    email = EmailField(validators=[DataRequired()],render_kw={"placeholder":"Email"})
    wachtwoord = PasswordField(validators =[DataRequired()],render_kw={"placeholder":"Wachtwoord"})
    wachtwoordherhalen = PasswordField(validators = [DataRequired(),EqualTo("wachtwoord", message="Wachtwoorden komen niet overeen")],render_kw = {"placeholder":"Wachtwoord herhalen"})
    geboortedatum = DateField(validators = [DataRequired()],render_kw={"placeholder":"Dy/Mth/Year"})
    submit = SubmitField("Registreren",render_kw={"class": "btn login-button"})

#Loginfunctionaliteit
@app.route("/login", methods= ["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template("login.html",form=form)

@app.route("/register", methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect("/")
    return render_template("registreren.html",form=form)
        

if __name__ == "__main__":
    app.run(debug=True)






