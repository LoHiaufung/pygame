# -*- coding: utf-8 -*-
from field import CBaseField

class CAutoSerObj(object):

	def __init__(self, parent=None):
		super(CAutoSerObj, self).__init__()
		self.__fieldDict__ = {}
		self._parent = parent

		for attrName, field in vars(self.__class__).iteritems():
			if isinstance(field, CBaseField) or isinstance(field, CAutoSerObj):
				self.__fieldDict__[attrName] = field

	def GetParent(self):
		return self._parent

	def serialize(self):
		res = {}
		for name in self.__fieldDict__.iterkeys():
			res[name] = self.__fieldDict__[name].serialize()
		return res

	def deserialize(self, data):
		for key in data.iterkeys():
			self.__fieldDict__[key].deserialize(data[key])

	def __getattr__(self, key):
		return self.__fieldDict__[key].getValue()

	def __setattr__(self, key, value):
		if self.__dict__.has_key('__fieldDict__') and self.__fieldDict__.has_key(key):
			self.__fieldDict__[key].setValue(value)
			
		super(CAutoSerObj, self).__setattr__(key, value)