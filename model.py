import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Acteur(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    voornaam = db.Column(db.Text)
    achternaam = db.Column(db.Text)

    def __init__(self, voornaam,achternaam):
        self.voornaam = voornaam
        self.achternaam = achternaam

class Regisseur(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    voornaam = db.Column(db.Text)
    achternaam = db.Column(db.Text)

    def __init__(self, voornaam,achternaam):
        self.voornaam = voornaam
        self.achternaam = achternaam

class Rol(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    acteur_id = db.Column(db.Integer, db.ForeignKey('acteur.id'))
    film_id = db.Column(db.Integer,db.ForeignKey('film.id'))
    personage = db.Column(db.Text)

class Film(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.Text)
    regisseur_id = db.Column(db.Integer,db.ForeignKey('regisseur.id'))
    release_datum = db.Column(db.Date)
    trailer_url = db.Column(db.Text)



