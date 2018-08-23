import os
import signal
import subprocess


class Process(object):
  process = None

  def start_process(self):
    if self.process == None:
      cmd = "python process.py"
      self.process = subprocess.Popen(cmd.split(), preexec_fn=os.setsid)
      return self.process.pid
    return None

  def is_running(self):
    return self.process != None