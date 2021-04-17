from flask import Flask, render_template, request
import models
from flask_sqlalchemy import SQLAlchemy
import listeler
import os

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

@app.route("/create")
def create():
	return render_template("create.html")

 
@app.route('/ilanolustur', methods=['GET', 'POST'])
def ilanolustur(): 
	if request.method == "POST":
		yeni_is = models.isler(
			#### ajax ile istek oluşturulacak
			Baslik = request.form["ilanbasligi"],
			is_turu =  listeler.is_turu[int(request.form["isturu"])],
		    istenen_tecrube =  listeler.tecrube[int(request.form["tecrube"])],
		    il   =  request.form["il"],
		    ilce =  request.form["ilce"],
		    gorunen_aciklama =  request.form["gorunen"],
		    maas_bilgisi =  request.form["maas"],
		    detayli_aciklama = request.form["detayli"]
			)
			
		
		db.session.add(yeni_is) 
		db.session.commit()
		return 200

		# return str(models.isler.query.all()[0])
		# return Listeler.tecrube[int(request.form["tecrube"])]
	
		#return render_template('index.html')
	
if __name__ == "__main__":
	app.run()
	