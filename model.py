import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Text, Date, ForeignKey
from flask_migrate import Migrate
db = SQLAlchemy()
migrate = Migrate()

class Acteur(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    voornaam: Mapped[str] = mapped_column(Text)
    achternaam: Mapped[str] = mapped_column(Text)

    def __init__(self, voornaam: str, achternaam: str):
        self.voornaam = voornaam
        self.achternaam = achternaam


class Regisseur(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    voornaam: Mapped[str] = mapped_column(Text)
    achternaam: Mapped[str] = mapped_column(Text)

    def __init__(self, voornaam: str, achternaam: str):
        self.voornaam = voornaam
        self.achternaam = achternaam


class Rol(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    acteur_id: Mapped[int] = mapped_column(ForeignKey("acteur.id"))
    film_id: Mapped[int] = mapped_column(ForeignKey("film.id"))
    personage: Mapped[str] = mapped_column(Text)


class Film(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(Text)
    regisseur_id: Mapped[int] = mapped_column(ForeignKey("regisseur.id"))
    release_datum: Mapped[Date] = mapped_column(Date)
    trailer_url: Mapped[str] = mapped_column(Text)


#User class voor loginfunctionaliteit
class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(Text, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(Text, unique=True, nullable=False)
    wachtwoord: Mapped[str] = mapped_column(Text, nullable=False)
    geboortedatum: Mapped[str] = mapped_column(Text)

    def __init__(self, username, email, wachtwoord, geboortedatum):
        self.username = username
        self.email = email
        self.wachtwoord = wachtwoord
        self.geboortedatum = geboortedatum