# Imports
from aux_pro import Process
from database import Database
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from models import Samples

app = Flask(__name__)
db = Database()
pro = Process()

@app.route('/')
def index():
  samples = db.init_sample()
  #data = request.form
  #periodo_muestreo = data["periodo"]
  pro.start_process()
  #return render_template('index.html', temperatura=samples["temperatura"], humedad=samples["humedad"], presion=samples["presion"], viento=samples["viento"], periodo=periodo_muestreo)
  return render_template('index.html', temperatura=samples["temperatura"], humedad=samples["humedad"], presion=samples["presion"], viento=samples["viento"])
  #return render_template('index.html')

@app.route('/samples/last/', methods = ["GET"])
def get_last_sample():
  last_sample = db.get_last_sample()
  return jsonify(last_sample)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8888)

