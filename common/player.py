# -*- coding: utf-8 -*-
from common.serialize.auto_serialize_obj import CAutoSerObj
import common.serialize.field as ModField


class CPlayer(CAutoSerObj):
	HP = ModField.CIntField(666)
	MP = ModField.CIntField(233)

	def __init__(self):
		super(CPlayer, self).__init__()

	def Hit(self, val):
		self.HP -= val