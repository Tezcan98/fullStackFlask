from flask_appbuilder import Model
from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, Date
# before pip install flask_appbuilder, run this command ->>  pip install setuptools --upgrade
from datetime import datetime 
from flask_appbuilder.models.mixins import ImageColumn


class isler(db.Model):
    __tablename__ = 'isler'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Baslik = Column(String(75), nullable=False)
    is_turu = Column(String(32), nullable=False)
    istenen_tecrube = Column(String(32), nullable=False)
    il   = Column(String(32), nullable=True)
    ilce = Column(String(32), nullable=True)
    gorunen_aciklama = Column(String(256), nullable=False)
    maas_bilgisi = Column(String(32), nullable=True)
    detayli_aciklama = Column(String(1024), nullable=False) 
 
    
    def __init__(self, Baslik, is_turu, istenen_tecrube, il, ilce, gorunen_aciklama, maas_bilgisi, detayli_aciklama): 
        self.Baslik = Baslik
        self.is_turu = is_turu
        self.istenen_tecrube = istenen_tecrube
        self.il   =  il
        self.ilce =  ilce
        self.gorunen_aciklama =  gorunen_aciklama
        self.maas_bilgisi = maas_bilgisi
        self.detayli_aciklama = detayli_aciklama 

    # def listele(self, filtre, siralama, sayfa): # sayfada 12 tane olucak şekilde
    #   return 1

    def liste(self):
        return [self.Baslik, self.detayli_aciklama]
    def __str__(self):
        return "Baslik : "+self.Baslik + "Detay : " + self.detayli_aciklama

class cvs(db.Model):
    __tablename__  = 'cvs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    isim_soyisim = Column(String(75))
    d_tarihi = Column(String(32))
    yetenekler = Column(String(32))
    egitim_bilgisi   = Column(String(32))
    Kariyer_gecmisi = Column(String(32))
    kariyer_hedefleri = Column(String(256))

    # kullanici = db.relationship("kullanici", backref="kullanici")

class kullanici(db.Model):
    __tablename__ = 'kullanici'
    id = Column(Integer, primary_key=True, autoincrement=True)
    kullanici_adi = Column(String(100), unique = True, nullable=False)
    # cv fk
    cv = Column(Integer, ForeignKey('cvs.id'))  
    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    

class sirket(db.Model):
    __tablename__ = 'sirket'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sirket_ismi = Column(String(75), unique = True, nullable=False)
    Tarihce = Column(String(512), nullable=True) 

    def __init__(self,sirket_ismi, Tarihce): 
        self.sirket_ismi = sirket_ismi
        self.Tarihce = Tarihce 

class is_basvurulari(db.Model):
    __tablename__ = 'is_basvurulari'
    id = Column(Integer, primary_key=True, autoincrement=True)
    #basvurular fk
    bas_is = Column(Integer, ForeignKey('isler.id'))  
    bas_kisi = Column(Integer, ForeignKey('kullanici.id'))  
    tarih = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class sirket_ilanlari(db.Model):
    __tablename__ = 'sirket_ilanlari'
    id = Column(Integer, primary_key=True, autoincrement=True)
    yayinlanan_is = Column(Integer, ForeignKey('isler.id'))  
    yayinlayan_sirket = Column(Integer, ForeignKey('sirket.id'))  
    tarih = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __init__(self, yayinlanan_is, yayinlayan_sirket,):
        self.yayinlanan_is = yayinlanan_is
        self.yayinlayan_sirket = yayinlayan_sirket 
        self.tarih = datetime.now()

db.create_all()

 