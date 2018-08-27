# Imports
from aux_pro import Process
from database import Database
from flask import Flask
from flask import render_template

app = Flask(__name__)
db = Database()
pro = Process()

@app.route('/')
def index():
  samples = db.init_sample()
  pro.start_process()
  return render_template('index.html', temperatura=samples["temperatura"], humedad=samples["humedad"], presion=samples["presion"], viento=samples["viento"])

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8888)

