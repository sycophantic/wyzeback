#!/bin/python3
import sys

if len(sys.argv) < 2:
  print('wyzeback_door')
  print('Usage: ' + sys.argv[0] + ' <new mac>')
  print('e.g. ' + sys.argv[0] + ' AABBCCDD')
else:
  newmac = sys.argv[1].upper()
  f=open('wyzesense_door_AABBCCDD.bin','rb')
  patched=f.read().replace(b'AABBCCDD',bytes(newmac, 'utf-8'))
  f.close()
  filename='patched_' + newmac + '.bin'
  f = open(filename,'wb')
  print('Writing: ' + filename) 
  f.write(patched)
  f.close()
