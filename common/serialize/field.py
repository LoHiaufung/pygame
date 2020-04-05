# -*- coding: utf-8 -*-


class CBaseFiele(object):
	NEED_TYPE = None

	def __init__(self, val):
		super(CBaseFiele, self).__init__()
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

class CIntField(CBaseFiele):
	NEED_TYPE = int

	def __init__(self, val=0):
		super(CIntField, self).__init__(val)
