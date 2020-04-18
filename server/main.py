# -*- coding: utf-8 -*-
import sys
import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print '***'
print 'path', path
print '***'
sys.path.append(path)

from starter.base_starter import CBaseStarter


if __name__ == '__main__':
	print 'server main!'

	serverApp = CBaseStarter()
	serverApp.Go()