from flask import Flask, render_template, request
import models
from flask_sqlalchemy import SQLAlchemy
import listeler
import os
from flask import json


app = Flask(__name__,static_url_path='', 
            static_folder='static')

# db_path = os.path.join(os.path.dirname(__file__), 'app.db')
# db_uri = 'sqlite:///{}'.format(db_path)
# app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
# db = SQLAlchemy(app)

file_path = os.path.abspath(os.getcwd())+"\database.db"
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
db = SQLAlchemy(app)


@app.route("/") 
@app.route("/index")
def home():
	return render_template("index.html")

@app.route("/ilanlar")
def ilanlar():  

	# sirk = models.sirket(sirket_ismi = "apple",Tarihce= "uzunyazi")
	# db.session.add(sirk)
	# db.session.commit()

	# db.session.query(models.isler).delete()
	# db.session.commit()
	return render_template("ilanlar.html")

@app.route('/sirketBilgileri', methods=['GET', 'POST'])
def sirketBilgileri():
	sirketBilgileri = models.sirket.query.get(1)  #id verilecek
  
	response = app.response_class(
		response=json.dumps(
			{	
				"responseText": render_template("sirketBilgileri.html", bilgiler = sirketBilgileri) , 
				"status":"success", 
				"code":0 
			}),
		status=200,
		mimetype='application/json'
	) 
	return response  


@app.route('/sirketBilgileriGuncelle', methods=['GET', 'POST'])
def sirketguncelle():
	if request.method == "POST":

		sirketismi = request.form.get('sirketismi','')
		uzunyazi =request.form.get('uzunyazi','')
		resimBlob =request.form.get('resimBlob','')

		sirket = models.sirket.query.get(1)
		sirket.update(dict(sirket_ismi =sirketismi, Tarihce = uzunyazi))
		db.session.commit()




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
			#### ajax ile istek oluşturulacak
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
	
		#return render_template('index.html')
	
if __name__ == "__main__":
	app.run()
	