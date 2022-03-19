import vosk
import sounddevice as sd
import queue, sys, json
from .errors import *
q = queue.Queue()


class LiveListening():
  def __init__(self, model_path=None) -> None:
    self.device_info = sd.query_devices(None, 'input')
    self.samplerate = int(self.device_info['default_samplerate'])
    self.pause = False

    if model_path == None:
      raise ModelPathNotFound("Please specify the model path")
    else:
      self.model = vosk.Model(model_path)


  def __callback(self, indata, frames, time, status):
    q.put(bytes(indata))

  def __paused(self):
    self.pause = True

  def recognition(self, message):
      if message == self.message:
          self.trigger(True)
          self.__paused()

  def listening(self):
      with sd.RawInputStream(samplerate=self.samplerate, blocksize = 8000, device=None, dtype='int16', channels=1, callback=self.__callback):
          rec = vosk.KaldiRecognizer(self.model, self.samplerate)
          while True:
              data = q.get()
              if self.pause != True:
                if rec.AcceptWaveform(data):
                  rec.Result()
                else:
                    self.recognition(json.loads(rec.PartialResult())['partial'])
              else:
                  return None
  def start(self, message, func):
    self.message = message
    self.trigger = func
    self.listening()
