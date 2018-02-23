from ctypes import cdll, c_char_p
import os
__lib_path__ = os.path.join(os.path.dirname(__file__), 'libsample.so')
__clib__ = cdll.LoadLibrary(__lib_path__)

__clib__.callRead.restype = c_char_p

class SampleObject(object):
  def __init__(self):
    self._ref = __clib__.newSampleObject()

  def __del__(self):
    __clib__.delSampleObject(self._ref)
    del self._ref

  def doHello(self):
    __clib__.callDoHello(self._ref)

  def echo(self, msg):
    __clib__.callEcho(self._ref, msg.encode())

  def read(self, filepath):
    return __clib__.callRead(self._ref, filepath.encode()).decode()
