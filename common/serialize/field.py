# -*- coding: utf-8 -*-


class CBaseField(object):
	NEED_TYPE = None

	def __init__(self, val):
		super(CBaseField, self).__init__()
		self._val = val

	def serialize(self):
		return self._val

	def deserialize(self, val):
		self._val = val

	def setValue(self, val):
		if self.NEED_TYPE is None or type(val) is not self.NEED_TYPE:
			raise Exception
		else:
			self._val = val

	def getValue(self):
		return self._val

class CIntField(CBaseField):
	NEED_TYPE = int

	def __init__(self, val=0):
		super(CIntField, self).__init__(val)

	def __sub__(self, other):
		return self._val - other

class CListField(CBaseField):
	NEED_TYPE = list

	def __init__(self, val = []):
		super(CListField, self).__init__(val)

class CAutoSerObjListField(CBaseField):
	NEED_TYPE = list
	
	def __init__(self, cls, val=[]):
		super(CAutoSerObjListField, self).__init__(val)
		self._cls = cls

	def serialize(self):
		res = []
		for autoSubObj in self._val:
			res.append(autoSubObj.serialize())
		return res

	def deserialize(self, seriaLst):
		self._val = []
		for seriaData in seriaLst:
			item = self._cls()
			item.deserialize(seriaData)
			self._val.append(item)

class CDictField(CBaseField):
	NEED_TYPE = dict

	def __init__(self, val= {}):
		super(CDictField, self).__init__(val)


class CAutoSerObjDictField(CBaseField):
	NEED_TYPE = dict

	def __init__(self, cls, val={}):
		super(CAutoSerObjDictField, self).__init__(val)
		self._cls = cls

	def serialize(self):
		res = {}
		for key, subSerObj in self._val.iteritems():
			res[key] = subSerObj.serialize()
		return res

	def deserialize(self, subObjDict):
		res = {}
		for key, subObjData in subObjDict.iteritems():
			item = self._cls()
			item.deserialize(subObjData)
			res[key] = item
		self._val = res


