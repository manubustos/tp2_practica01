import os
import signal
import subprocess

class Process(object):
  process = None
  def start_process(self, id_sample):
    if self.process == None:
      cmd = "python3 process.py %s" % (id_sample)
      self.process = subprocess.Popen(cmd.split(), preexec_fn=os.setsid)
      return 200
    return 500

  def stop_process(self):
    if self.process != None:
      os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
      self.process = None
    return 200
      
  def is_running(self):
    return self.process != None