from models import Samples

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
import random

class Database(object):
  session = None
  db_user = os.getenv("DB_USER") if os.getenv("DB_USER") != None else "example"
  db_pass = os.getenv("DB_PASS") if os.getenv("DB_PASS") != None else "example"
  db_host = os.getenv("DB_HOST") if os.getenv("DB_HOST") != None else "db"
  db_name = os.getenv("DB_NAME") if os.getenv("DB_NAME") != None else "samples"
  db_port = os.getenv("DB_PORT") if os.getenv("DB_PORT") != None else "3306"
  Base = declarative_base()
  
  def get_session(self):
    """Singleton of db connection

    Returns:
        [db connection] -- [Singleton of db connection]
    """
    if self.session == None:
      connection = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (self.db_user,self.db_pass,self.db_host,self.db_port,self.db_name)
      engine = create_engine(connection,echo=True)
      connection = engine.connect()
      Session = sessionmaker(bind=engine)
      self.session = Session()
      self.Base.metadata.create_all(engine)
    return self.session

  def init_sample(self, dict_sample):
    session = self.get_session()
    sample = Samples(temperature=dict_sample["temperatura"], humidity=dict_sample["humedad"],
                      pressure=dict_sample["presion"], windspeed=dict_sample["viento"])
    session.add(sample)
    session.commit()
    sample_id = int(sample.id)
    session.close()
    return sample_id

  def get_sample(self, id_sample):
    session = self.get_session()
    sample = session.query(Samples).filter_by(id=id_sample).first()
    session.close()
    return sample

  def add_sample(self, sample):
    session = self.get_session()
    samples = {}
    samples["temperatura"] = sample.temperature + random.randint(-1,1)
    samples["humedad"] = sample.humidity + random.randint(-1,1)
    samples["presion"] = sample.pressure + random.randint(-1,1)
    samples["viento"] = sample.windspeed + random.randint(-1,1)
    newSample = Samples(temperature=samples["temperatura"], humidity=samples["humedad"],
                      pressure=samples["presion"], windspeed=samples["viento"])
    session.add(newSample)
    session.commit()
    session.close()
    return newSample
