# -*- coding: utf-8 -*-
import time
from server.servercommon.config import SERVER_FRAME

def frame_sleep(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		before = time.time()
		f(*args, **kwargs)
		after = time.time()
		delta = after - before
		if delta > 0:
			time.sleep(1.0/30 - delta)


class CBaseStarter(object):
	
	def __init__(self):
		super(CBaseStarter, self).__init__()

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
		self.ProcessNet()
		self.OnFrameUpdate()

	def Prepare(self):
		pass

	def StartNet(self):
		pass

	def ProcessNet(self):
		pass

	def OnFrameUpdate(self):
		pass

	def OnEnd(self):
		pass