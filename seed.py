"""from app import app, db
from app.models import Acteur, Regisseur, Film, Rol
from datetime import date
#in seed.py wordt de databse gemaakt en opgevuld
with app.app_context():
    db.drop_all() #db drop_all moet weg bij uiteindelijke inlevering
    db.create_all()

    # Regisseurs
    regisseurs = [
        Regisseur("Erik", "de Bruyn"),
        Regisseur("Pollo", "de Pimentel"),
        Regisseur("Paula", "van der Oest"),
        Regisseur("Vincent", "Bal"),
        Regisseur("Maria", "Peters"),
        Regisseur("Norbert","ter Hall"),
        Regisseur("André","van der Hout"),
        Regisseur("Ben","Sombogaart"),
        Regisseur("Eddy","ter stall"),
        Regisseur("Rita","Horst"),
        Regisseur("Elbert","van Strien"),
        Regisseur("Boris","Pavel Conen"),
        Regisseur("Teddy","Cherim"),
        Regisseur("Simone","van Dusseldorp"),
        Regisseur("Steven","de Jong")
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

        Acteur("Kitty","Courbois"),
        Acteur("John","Wijdenbosch"),
        Acteur("Paul","Hoes"),
        Acteur("Hans","Veerman"),
        Acteur("Daniel","Rovai"),
        Acteur("Odile","Bouineau"),

        Acteur("Ferry","Heijne"),
        Acteur("Huug","van Tienhoven"),
        Acteur("Frank","van den Bos"),

        Acteur("Janieck","van de Polder"),
        Acteur("Suzanne","Zuiderwijk"),
        Acteur("Arjan","Ederveen"),
        Acteur("Jack","Wouterse"),
        Acteur("Yeshela","Crommelin"),
        Acteur("Colin","Tetteroo"),
        Acteur("Luka","Schäfer"),

        Acteur("Cees","Geel"),
        Acteur("Marcel","Hensema"),
        Acteur("Rifka","Lodeizen"),
        Acteur("Daan","Ekkel"),
        Acteur("Eva","Duijvestein"),
        Acteur("Nadja","Hüpscher"),

        Acteur("Huub","Stapel"),
        Acteur("Joke","Tjalsma"),
        Acteur("Kenadie","Jourdin-Bromley"),
        Acteur("Madelief","Vermeulen"),
        Acteur("Ties","Dekker"),
        Acteur("Diederik","Ebbinge"),

        Acteur("Barry","Atsma"),
        Acteur("Hadewych","Minis"),
        Acteur("Isabelle","Stokkel"),
        Acteur("Charlotte","Arnoldy"),
        Acteur("Lisa","Smit"),
        Acteur("Bart","Slegers"),
        Acteur("Philippe","Colpaert"),

        Acteur("Anniek","Pheifer"),
        Acteur("Tygo","Gernandt"),
        Acteur("Mark","Rietman"),
        Acteur("Eugenia","Lencinas"),
        Acteur("Ismael","Santillán"),
        Acteur("Leonardo","Ramírez"),

        Acteur("Achmed","Akkabi"),
        Acteur("Sallie","Harmsen"),
        Acteur("Manuel","Broekman"),
        Acteur("Géza","Weisz"),
        Acteur("Isis","Cabolet"),
        Acteur("Gwen","Pol"),

        Acteur("Hanna","Obbeek"),
        Acteur("Isabelle","Stokkel"),
        Acteur("Nils","Verkooijen"),
        Acteur("Daan","Schuurman"),
        Acteur("Lies","Visschedijk"),
        Acteur("Finn","Poncin"),

        Acteur("Ydwer","Bosma"),
        Acteur("Joosje","Duk"),
        Acteur("Pim","Wessels"),
        Acteur("Bart","de Vries"),
        Acteur("Michiel","de Jong"),
        Acteur("Howard","van Dodemont")
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
        Film("Monte Carlo", 6,date(2001,9,28) , "X0n3Q_VDQk8"),
        Film("De arm van Jezus", 7,date(2003,2,6),"dc9d0Sq6IGs"),
        Film("Pluk van de Petteflet", 8, date(2004,11,17),"Byz-FUj6wFU"),
        Film("Simon", 9, date(2004,3,18),"T4BpJ0H3ji8"),
        Film("Iep!",10,date(2010,2,17),"WclyqvXkE40"),
        Film("Zwart water",11,date(2010,3,18),"frNXGUGmoyw"),
        Film("First Mission",12,date(2010,3,25),"83_n35KnpSg"),
        Film("Sterke verhalen",13,date(2010,8,19),"lfOoZpOUtro"),
        Film("Briefgeheim",14,date(2010,10,14),"XF53sfbPE64"),
        Film("Snuf de hond en het spookslot",15,date(2010,11,16),"nzM3DHH_akg")
    ]
    db.session.add_all(films)
    db.session.commit()

    # Rollen
    rollen = [
        Rol(1,1,"Leen"), 
        Rol(2,1,"Daan"), 
        Rol(3,1,"Jacob"),
        Rol(4,1,"Noortje"), 
        Rol(5,1,"Wannes"), 
        Rol(6,1,"Janine"),

        Rol(7,2,"Thera"),
        Rol(8,2,"Berry Kooijman"),
        Rol(9,2,"Otto"), 
        Rol(10,2,"Felicio"),
        Rol(11,2,"Jamal"), 
        Rol(12,2,"Mr.Kooijman"),

        Rol(13,3,"Sonja"), 
        Rol(14,3,"Wanda"),
        Rol(15,3,"Michelle"), 
        Rol(16,3,"Nino"),
        Rol(17,3,"Bo"), 
        Rol(18,3,"Hugo"),
        Rol(19,3,"Jan"),

        Rol(20,4,"Minoes"), 
        Rol(21,4,"Tibbe de Vries"),
        Rol(22,4,"Bibian van Dam"),
        Rol(23,4,"Meneer Ellemeet"),
        Rol(24,4,"Mevrouw Ellemeet"),
        Rol(25,4,"Mevrouw Van dam"),
        Rol(26,4,"Meneer Van Dam"),
        Rol(27,4,"Harry de Haringman"),

        Rol(28,5,"Pietje Bell"), 
        Rol(29,5,"Sproet"),
        Rol(30,5,"Kees"), 
        Rol(31,5,"Engeltje"),
        Rol(32,5,"Peentje"), 
        Rol(33,5,"Jaap"),
        Rol(34,5,"Vader Bell"),
        Rol(35,5,"Moeder Bell"),

        Rol(36,6,"Constance"),
        Rol(37,6,"Danny Schat"),
        Rol(38,6,"Harald"),
        Rol(39,6,"Garage eigenaar"),
        Rol(40,6,"Politie inspecteur"),
        Rol(41,6,"Tolk bij politie bureau"),

        Rol(42,7,"Jacob Ijzermans"),
        Rol(43,7,"Hendrik Ijzermans"),
        Rol(44,7,"Taxi-chauffeur"),

        Rol(45,8,"Pluk"),
        Rol(46,8,"Aagje"),
        Rol(47,8,"Meneer Pen & Kluizelaar"),
        Rol(48,8,"Vader Stamper"),
        Rol(49,8,"Stamper 1"),
        Rol(50,8,"Stamper 2"),
        Rol(51,8,"Stamper 3"),

        Rol(52,9,"Simon"),
        Rol(53,9,"Camiel"),
        Rol(54,9,"Sharon"),
        Rol(55,9,"Marco"),
        Rol(56,9,"Ellen"),
        Rol(57,9,"Joy"),

        Rol(58,10,"Warre"),
        Rol(59,10,"Tine"),
        Rol(60,10,"Viegeltje"),
        Rol(61,10,"Loetje"),
        Rol(62,10,"Bor"),
        Rol(63,10,"de Redder"),

        Rol(64,11,"Paul Docker"),
        Rol(65,11,"Christine Donker en Karen"),
        Rol(66,11,"Lisa Doncker"),
        Rol(67,11,"Karen Rompaey"),
        Rol(68,11,"Stem Karen"),
        Rol(69,11,"Geert Steegmans"),
        Rol(70,11,"Peter Steegmans"),

        Rol(71,12,"Marina"),
        Rol(72,12,"Barry"),
        Rol(73,12,"Mark Rietman"),
        Rol(74,12,"Carmelita"),
        Rol(75,12,"Diego"),
        Rol(76,12,"Orlando"),

        Rol(77,13,"Dennis van der Molen"),
        Rol(78,13,"Sanne"),
        Rol(79,13,"Marlon Broekman"),
        Rol(80,13,"Mario"),
        Rol(81,13,"Iris"),
        Rol(82,13,"Lotte"),

        Rol(83,14,"Eva Vels"),
        Rol(84,14,"Jackie"),
        Rol(85,14,"Thomas"),
        Rol(86,14,"Eva's vader"),
        Rol(87,14,"Eva's moeder"),
        Rol(88,14,"vader Jackie en Thomas"),

        Rol(89,15,"Tom"),
        Rol(90,15,"Mirjam Weisman"),
        Rol(91,15,"Jaap"),
        Rol(92,15,"Zwarte Betram"),
        Rol(93,15,"Barinkhof"),
        Rol(94,15,"oom Hans"),
    ]
    db.session.add_all(rollen)
    db.session.commit()"""

  #Seed.py is niet langer nodig omdat we nu met migrations werken maar ik heb het alsnog maar even bewaard"""