# -*- coding: utf-8 -*-
import sys
import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print '***'
print 'path', path
print '***'
sys.path.append(path)

from common.player import CPlayer

if __name__ == '__main__':
	print 'client main!'

	A = CPlayer()
	B = CPlayer()

	print '__init__'
	print A.serialize()
	print B.serialize()

	print 'Hit'
	A.Hit(50)
	print A.serialize()

	print 'deserialize'
	B.deserialize(A.serialize())
	print B.serialize()