from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import listeler
import os
from flask import json 
from flask_migrate import Migrate
import urllib 
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

app = Flask(__name__, static_url_path='',
            static_folder='static') 
file_path = os.path.abspath(os.getcwd())+"\database.db" 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models


@app.route("/")
@app.route("/index")
def home():
	return render_template("index.html")


@app.route("/ilanlar")
def ilanlar():

	# dummy	
	# sirk = models.sirket(sirket_ismi = "apple",Tarihce= "uzunyazi")
	# db.session.add(sirk)
	# db.session.commit()

	# db.session.query(models.isler).delete()
	# db.session.commit()
	return render_template("ilanlar.html")


@app.route('/sirketBilgileri', methods=['GET', 'POST'])
def sirketBilgileri():
	sirketBilgileri = models.sirket.query.get(1)  # id verilecek
	
	response = app.response_class(
		response=json.dumps(
			{
				"responseText": render_template("sirketBilgileri.html", bilgiler=sirketBilgileri),
				"status": "success",
				"code": 0
			}),
		status=200,
		mimetype='application/json'
	)
	return response


app_root = os.path.dirname(os.path.abspath(__file__))


@app.route('/sirketBilgileriGuncelle', methods=['GET', 'POST'])
def sirketguncelle(): 
	if request.method == "POST":
		pp_file=request.files.get('file') 
		sirketismi = request.form.get('sirketismi','')
		uzunyazi =request.form.get('uzunyazi','') 
		 
		mimetype = pp_file.mimetype
		filename = secure_filename(pp_file.filename)
		Img = models.resimler(img = pp_file.read(), mimetype= mimetype, filename= filename)
	  
		sirket = models.sirket.query.get(1)  ## sirket id yapilacak 
		
		sirket.update(sirketismi, uzunyazi) 

		# yeni_resim = models.resimler(m_file)	 
		db.session.add(Img) 
		db.session.flush()
		sirket.profil = Img.id  
		db.session.merge(sirket) 
		db.session.commit()


		# print("3df*",yeni_resim.id)


		response = app.response_class(
			response=json.dumps({"status":"success","code":0}),
			status=200,
			mimetype='application/json'
		) 
		return response  

 

@app.route('/ilanlistele', methods=['GET', 'POST'])
def ilanlari_listele():
	# if request.method == "POST":  
	ilanlar = models.isler.query.filter_by(yay_sirket = 1).all()  #id verilecek
  
	response = app.response_class(
            response=json.dumps(
				{	
					"responseText": render_template("ilanlariListele.html", ilanlar = ilanlar ) , 
					"status":"success", 
					"code":0 
				}),
            status=200,
            mimetype='application/json'
		)

	return response 

@app.route('/olusturmaEkrani', methods=['GET', 'POST'])
def olusturmaEkrani():  
	response = app.response_class(
		response=json.dumps(
			{	
				"responseText": render_template("ilanolustur.html", ilanlar = ilanlar ) , 
				"status":"success", 
				"code":0 
			}),
		status=200,
		mimetype='application/json'
	)

	return response  

@app.route('/ilanolustur', methods=['GET', 'POST'])
def ilanolustur(): 
	if request.method == "POST":
		yeni_is = models.isler(
			# ajax ile istek oluşturulacak
			yay_sirket = 1,
			Baslik = request.form.get('Baslik',''),
			is_turu =request.form.get('is_turu',''),
		    istenen_tecrube =  request.form.get('istenen_tecrube','')  ,
		    il   =  request.form.get('il',''),
		    ilce =  request.form.get('ilce','') ,
		    gorunen_aciklama =  request.form.get('gorunen_aciklama','')  ,
		    maas_bilgisi =  request.form.get('maas_bilgisi','')  ,
		    detayli_aciklama = request.form.get('detayli_aciklama','')  
			
			)
		db.session.add(yeni_is) 
		db.session.commit()
	 

		response = app.response_class(
            response=json.dumps({"status":"success","code":0}),
            status=200,
            mimetype='application/json'
		)
		return response

		# return str(models.isler.query.all()[0])
		# return Listeler.tecrube[int(request.form["tecrube"])]
	
		# return render_template('index.html')
	
if __name__ == "__main__":
	app.run()
	
