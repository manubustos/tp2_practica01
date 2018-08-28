from database import Database
from models import Samples

import random
import time
import sys

def main(sample, session):
  while(1):
    sample.temperature += random.randint(-1,1)
    sample.humidity += random.randint(-5,5)
    sample.pressure += random.randint(-1,1)
    sample.windspeed += random.randint(-1,1)
    session.add(sample)
    session.commit()
    time.sleep(1)


if __name__ == '__main__':
  if (len(sys.argv) != 2):
    sys.exit("Usage: python process.py id_sample")
  id_sample = int(sys.argv[1])
  db = Database()
  session = db.get_session()
  sample = session.query(Samples).filter_by(id=id_sample).first()
  main(sample, session)
  