#!/bin/python3
import sys

if len(sys.argv) < 2:
  print('wyzeback_motion')
  print('Usage: ' + sys.argv[0] + ' <new mac>')
  print('e.g. ' + sys.argv[0] + ' 77A5DBDD')
else:
  newmac = sys.argv[1].upper()
  f=open('wyzesense_motion_77A5DBDD.bin','rb')
  patched=f.read().replace(b'77A5DBDD',bytes(newmac, 'utf-8'))
  f.close()
  filename='patched_' + newmac + '.bin'
  f = open(filename,'wb')
  print('Writing: ' + filename) 
  f.write(patched)
  f.close()
