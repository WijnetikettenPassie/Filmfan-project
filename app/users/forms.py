from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,EqualTo
from wtforms import EmailField, PasswordField, StringField, SubmitField, DateField

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

class PasswordChangeForm(FlaskForm):
    old_password = PasswordField("Huidig wachtwoord", validators=[DataRequired()],render_kw={"placeholder": "Oud wachtwoord"})
    new_password = PasswordField("Nieuw wachtwoord", validators=[DataRequired()], render_kw={"placeholder": "Nieuw wachtwoord"})
    new_password_repeat = PasswordField("Herhaal nieuw wachtwoord", validators=[DataRequired(), EqualTo('new_password', message='Wachtwoorden komen niet overeen.')], render_kw={"placeholder": "Herhaal nieuw wachtwoord"})
    submit = SubmitField("Wachtwoord wijzigen", render_kw={"class": "btn login-button"})