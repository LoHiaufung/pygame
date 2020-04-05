# -*- coding: utf-8 -*-
from field import CBaseFiele

class CAutoSerObj(object):

	def __init__(self, parent=None):
		super(CAutoSerObj, self).__init__()
		self.__fieldDict__ = {}
		self.__subObjDict__ = {}

		self._parent = parent

		for attrName, field in vars(self.__class__).iteritems():
			if isinstance(field, CBaseFiele):
				self.__fieldDict__[attrName] = field
				self.__dict__[attrName] = field.getValue()

	def SubAutoSerObj(self, name, objClass):
		subObj = objClass(self)
		self.__subObjDict__[name] = subObj
		self.__dict__[name] = subObj

	def GetParent(self):
		return self._parent

	def serialize(self):
		res = {}
		for name in self.__fieldDict__.iterkeys():
			res[name] = self.__dict__[name]

		for name, value in self.__subObjDict__.iteritems():
			res[name] = value.serialize()
		return res

	def deserialize(self, data):
		for name in self.__fieldDict__.iterkeys():
			self.__dict__[name] = data[name]

		for name, subObj in self.__subObjDict__.iteritems():
			subObj.deserialize(data[name])