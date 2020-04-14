# -*- coding: utf-8 -*-

import heapq
import time

class Tick(object):
	def __init__(self, nextTime = None, interVal = None,times = None, func = None, *args):
		super(Tick, self).__init__()
		self._nextTime = nextTime
		self._interVal = interVal
		self._func = func
		self.args = args
		self.times = times

	def SetData(self, func, nextTime, interval, times, *args):
		self._nextTime = nextTime
		self._interVal = interval
		self._func = func
		self.args = args
		self.times = times

	def Trigger(self):
		if self.IsStop():
			return

		self._func(*args)
		if self.times != -1:
			# 除非是无限触发，否则次数减一
			self.times -= 1


	def Stop(self):
		self.times = 0

	def IsStop(self):
		return self.times == 0

	def SetNextTime(self, nxtTime):
		self._nextTime = nxtTime

	def GetNextTime(self):
		return self._nextTime

	def GetInterval(self):
		return self._interVal

	def GetCb(self):
		return self._func

	def __lt__(self, other):
		return self._nextTime <= other._nextTime

class TickPool(object):
	def __init__(self):
		super(TickPool, self).__init__()
		self.TickQueue = []

	def PopTick(self):
		return Tick() if len(self.TickQueue) <= 0 else self.TickQueue.pop()

	def PushTick(self, tickObj):
		self.TickQueue.push(tickObj)

class Timer(object):
	def __init__(self):
		super(Timer, self).__init__()
		self.heap = []
		self.key2Tick = {}

		self.tickPool = TickPool()

	def Process(self, curTime):
		while len(self.heap) > 0:
			tick = heapq.heappop()
			if tick.GetNextTime() > curTime:
				break
			else:
				tick.Trigger()
				if tick.IsStop():
					self.key2Tick.pop(tick.GetCb(), None)
					self.tickPool.PushTick(tick)
				else:
					tick.SetNextTime(curTime + tick.GetInterval())
					heapq.heappush(self.heap, tick)


	def RegTick(self, cb, interval, times, *args):
		tick = self.key2Tick.get(cb)
		if tick and (not tick.IsStop()):
			# 覆盖已有的tick
			tick.SetData(cb, time.time() + interval, interval, times, *args)
		else:
			# 新tick
			tick = self.tickPool.PopTick()
			tick.SetData(cb, time.time() + interval, interval, times, *args)

			heapq.heappush(self.heap, tick)
			self.key2Tick[cb] = tick

	def DelTick(self, cb):
		tick = self.key2Tick.pop(cb, None)
		if tick:
			# 对于删除都是Stop掉，然后等process中再加入到池里
			tick.Stop()


