from app import app, db
from model import Acteur, Regisseur, Film, Rol
from datetime import date

with app.app_context():
    db.drop_all()
    db.create_all()

    # Regisseurs
    regisseurs = [
        Regisseur("Erik", "de Bruyn"),
        Regisseur("Pollo", "de Pimentel"),
        Regisseur("Paula", "van der Oest"),
        Regisseur("Vincent", "Bal"),
        Regisseur("Maria", "Peters")
    ]
    db.session.add_all(regisseurs)
    db.session.commit()

    # Acteurs
    acteurs = [
        Acteur("Fedja","van Huêt"),
        Acteur("Frank","Lammers"),
        Acteur("Frederik","Brom"),
        Acteur("Will","van Kralingen"),
        Acteur("Josse","De Pauw"),
        Acteur("Angelique","de Bruijne"),
        Acteur("Katja","Schuurman"),
        Acteur("Egbert-Jan","Weeber"),
        Acteur("Johnny","de Mol"),
        Acteur("Edwin","Jonker"),
        Acteur("Mohammed","Chaara"),
        Acteur("Hans","Dagalet"),
        Acteur("Monic","Hendrickx"),
        Acteur("Anneke","Blok"),
        Acteur("Sylvia","Poorta"),
        Acteur("Jacob","Derwig"),
        Acteur("Halina","Reijn"),
        Acteur("Theau","Boermans"),
        Acteur("Jaap","Spijkers"),
        Acteur("Carice","van Houten"),
        Acteur("Theo","Maassen"),
        Acteur("Sarah","Bannier"),
        Acteur("Pierre","Bokma"),
        Acteur("Marisa","van Eyle"),
        Acteur("Olga","Zuiderhoek"),
        Acteur("Kees","Hulst"),
        Acteur("Hans","Kesting"),
        Acteur("Quinten","Schram"),
        Acteur("Frensch","de Groot"),
        Acteur("Serge","Price"),
        Acteur("Jordy","Mul"),
        Acteur("Sjoerd","Metz"),
        Acteur("Nicky","Burgers"),
        Acteur("Felix","Strategier"),
        Acteur("Angela","Groothuizen"),
    ]
    db.session.add_all(acteurs)
    db.session.commit()

    # Film
    films = [
        Film("Wilde Mossels", 1, date(2000,9,28), "UEekTd4pEyA"),
        Film("Oesters van Nam Kee", 2, date(2002,9,5), "cwakOKzm4Gc"),
        Film("Zus & Zo", 3, date(2002,5,8), "IId0TqQJHtQ"),
        Film("Minoes", 4, date(2001,12,6), "aa7VwIzBjkE"),
        Film("Pietje Bell", 5, date(2002,11,17), "Hh_t2plwh3k"),
    ]
    db.session.add_all(films)
    db.session.commit()

    # Rollen
    rollen = [
        Rol(1,1,"Leen"), Rol(2,1,"Daan"), Rol(3,1,"Jacob"),
        Rol(4,1,"Noortje"), Rol(5,1,"Wannes"), Rol(6,1,"Janine"),
        Rol(7,2,"Thera"), Rol(8,2,"Berry Kooijman"),
        Rol(9,2,"Otto"), Rol(10,2,"Felicio"),
        Rol(11,2,"Jamal"), Rol(12,2,"Mr.Kooijman"),
        Rol(13,3,"Sonja"), Rol(14,3,"Wanda"),
        Rol(15,3,"Michelle"), Rol(16,3,"Nino"),
        Rol(17,3,"Bo"), Rol(18,3,"Hugo"),
        Rol(19,3,"Jan"),
        Rol(20,4,"Minoes"), Rol(21,4,"Tibbe de Vries"),
        Rol(22,4,"Bibian van Dam"),
        Rol(23,4,"Meneer Ellemeet"),
        Rol(24,4,"Mevrouw Ellemeet"),
        Rol(25,4,"Mevrouw Van dam"),
        Rol(26,4,"Meneer Van Dam"),
        Rol(27,4,"Harry de Haringman"),
        Rol(28,5,"Pietje Bell"), Rol(29,5,"Sproet"),
        Rol(30,5,"Kees"), Rol(31,5,"Engeltje"),
        Rol(32,5,"Peentje"), Rol(33,5,"Jaap"),
        Rol(34,5,"Vader Bell"),
        Rol(35,5,"Moeder Bell"),
    ]
    db.session.add_all(rollen)
    db.session.commit()

  