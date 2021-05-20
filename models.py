from flask_appbuilder import Model
from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, Date
# before pip install flask_appbuilder, run this command ->>  pip install setuptools --upgrade
from datetime import datetime 
from flask_appbuilder.models.mixins import ImageColumn

import base64


class kullanici(db.Model):
    __tablename__ = 'kullanici'
    id = Column(Integer, primary_key=True, autoincrement=True)
    kullanici_adi = Column(String(100), unique = True, nullable=False)
    # cv fk
    cv = Column(Integer, ForeignKey('cvs.id'))   
    profil = Column(Integer, ForeignKey('resimler.id'))  

    # join kullan
    #def get_image(self):
    #    return resimler.query.get(self.profil).decode()

    #def get_cv
    
  
class resimler(db.Model): 
    __tablename__ = 'resimler'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img = db.Column(db.Text, unique=True, nullable=False) 
    filename = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    def __init__(self, img, filename, mimetype):
        self.img = img  
        self.filename = filename
        self.mimetype = mimetype

class sirket(db.Model):
    __tablename__ = 'sirket'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sirket_ismi = Column(String(75), unique = True, nullable=False)
    Tarihce = Column(String(512), nullable=True) 
    profil = Column(Integer, ForeignKey('resimler.id')) 
    def __init__(self,sirket_ismi, Tarihce): 
        self.sirket_ismi = sirket_ismi
        self.Tarihce = Tarihce  
    def get_image(self):  ## join ile yapılacak
        resim = resimler.query.get(self.profil)
        if resim != None:  
            return base64.b64encode(resim.img).decode()
            
        else:
            return "image.png"
    def update(self, sirket_ismi, Tarihce):
        self.sirket_ismi = sirket_ismi
        self.Tarihce = Tarihce 
        ## will be check if image exist
        

        
      

class isler(db.Model):
    __tablename__ = 'isler'
    id = Column(Integer, primary_key=True, autoincrement=True)
    #yayinlayan fk
    yay_sirket = Column(Integer, ForeignKey('sirket.id')) 
    
    Baslik = Column(String(75), nullable=False)
    is_turu = Column(String(32), nullable=False)
    istenen_tecrube = Column(String(32), nullable=False)
    il   = Column(String(32), nullable=True)
    ilce = Column(String(32), nullable=True)
    gorunen_aciklama = Column(String(256), nullable=False)
    maas_bilgisi = Column(String(32), nullable=True)
    detayli_aciklama = Column(String(1024), nullable=False) 
    tarih = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  
    
    def __init__(self,yay_sirket, Baslik, is_turu, istenen_tecrube, il, ilce, gorunen_aciklama, maas_bilgisi, detayli_aciklama): 
        self.yay_sirket = yay_sirket
        self.Baslik = Baslik
        self.is_turu = is_turu
        self.istenen_tecrube = istenen_tecrube
        self.il   =  il
        self.ilce =  ilce
        self.gorunen_aciklama =  gorunen_aciklama
        self.maas_bilgisi = maas_bilgisi
        self.detayli_aciklama = detayli_aciklama 
        self.tarih = datetime.now()
    
    def gunFarki(self): 
        today = datetime.now()
        diff = (today - self.tarih).days 
        if diff == 0:
            return "Bugün"
        elif diff >30:
            return diff/30+" ay önce"
        return diff
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

class is_basvurulari(db.Model):
    __tablename__ = 'is_basvurulari'
    id = Column(Integer, primary_key=True, autoincrement=True)
    #basvurular fk
    bas_is = Column(Integer, ForeignKey('isler.id'))  
    bas_kisi = Column(Integer, ForeignKey('kullanici.id'))  
    tarih = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
db.create_all()

 