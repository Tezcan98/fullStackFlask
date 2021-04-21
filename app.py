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


@app.route('/ilanlistele', methods=['GET', 'POST'])
def ilanlari_listele():
	# if request.method == "POST": 
	
	# sirket = models.sirket_ilanlari.query.filter_by(yayinlayan_sirket= 0)
	


	ilanlar = models.isler.query.filter_by(id = 1).all()  #id verilecek
	
	ilanList = []
	for st in ilanlar:
		ilanList.append(st.liste())
	
	response = app.response_class(
            response=json.dumps(
				{	
					"html": render_template("ilanlariListele.html") , 
					"status":"success",
					'ilanlar' : ilanList,
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
		sirket_ilanlari = models.sirket_ilanlari( 
			yayinlanan_is = yeni_is.id,
			yayinlayan_sirket = models.sirket.query.get(0).id # id verilecek
		)
		
		db.session.add(sirket_ilanlari)
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
	