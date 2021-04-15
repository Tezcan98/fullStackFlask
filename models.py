from flask_appbuilder import Model
from flask_appbuilder.models.mixins import ImageColumn

class kullanici(Model):
    id = Column(Integer, primary_key=True)
    kullanici_adi = Column(String(100), unique = True, nullable=False)
    # cv fk
    cv = db.Column(db.Integer, db.ForeignKey('cv.id'))
    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    #basvurular fk
    basvurulan_isler = db.Column(db.Integer, db.ForeignKey('is.id'))

class sirket(Model):
    id = Column(Integer, primary_key=True)
    sirket_ismi = Column(String(75), unique = True, nullable=False)
    Tarihce = Column(String(512) nullable=True)
    #ilan fk 
    ilanlar = db.Column(db.Integer, db.ForeignKey('is.id'))

class is(Model):
    id = Column(Integer, primary_key=True)
    Baslik = Column(String(75), nullable=False)
    is_turu = Column(String(32), nullable=False)
    istenen_tecrube = Column(String(32), nullable=False)
    il   = Column(String(32), nullable=True)
    ilce = Column(String(32), nullable=True)
    gorunen_aciklama = Column(String(256), nullable=False)
    maas_bilgisi = Column(String(32), nullable=True)
    detayli_aciklama = Column(String(1024), nullable=False)

class cv(Model):
    id = Column(Integer, primary_key=True)
    isim_soyisim = Column(String(75))
    d_tarihi = Column(String(32))
    yetenekler = Column(String(32))
    egitim_bilgisi   = Column(String(32))
    Kariyer_gecmisi = Column(String(32))
    kariyer_hedefleri = Column(String(256))