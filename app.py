from flask import Flask, render_template, request
from models import isler
from flask_sqlalchemy import SQLAlchemy
import listeler


app = Flask(__name__,static_url_path='', 
            static_folder='static')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/database.db'
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
		yeni_is = isler(
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
		
		return request.form["maas"]
		# return Listeler.tecrube[int(request.form["tecrube"])]
	
		#return render_template('index.html')
	
if __name__ == "__main__":
	app.run()