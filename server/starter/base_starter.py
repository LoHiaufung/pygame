# -*- coding: utf-8 -*-
import time
import server.servercommon.config as ModConfig
from common.net.net_manager import CBaseNetManager

def frame_sleep(f):
	def decorated(*args, **kwargs):
		before = time.time()
		f(*args, **kwargs)
		after = time.time()
		delta = after - before
		if delta > 0:
			time.sleep(1.0/30 - delta)

	return decorated

class CBaseStarter(object):
	
	def __init__(self):
		super(CBaseStarter, self).__init__()

		self._netMgr = CBaseNetManager()

	def Go(self):
		# 做些准备？
		self.Prepare()
		# 开网?
		self.StartNet()
		while True:
			self.Loop()
		self.OnEnd()

	@frame_sleep
	def Loop(self):
		self.OnFrameUpdate()

	def Prepare(self):
		print 'starter Prepare!'
		pass

	def StartNet(self):
		print 'start net!'
		self._netMgr.StartListen(ModConfig.serverAddrDict["center_control"]["for_game"])


	def OnFrameUpdate(self):
		self._netMgr.OnFrameUpdate()

	def OnEnd(self):
		pass