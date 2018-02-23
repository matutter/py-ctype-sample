
from samplelib import SampleObject
import os

testfile = os.path.join(os.path.dirname(__file__), 'file.txt')

if __name__ == '__main__':

  inst = SampleObject()
  print(SampleObject)
  print(inst)
  print(inst._ref)
  inst.doHello()

  inst.echo('xxx')

  with open(testfile, 'r') as fd:
    print('runtime >', fd.read().strip())

  print('native  >', inst.read(testfile).strip())


  del inst
