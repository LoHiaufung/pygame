# -*- coding: utf-8 -*-
import heapq

class Tick(object):
	def __init__(self, nextTime, func, *args, **kwargs):
		super(Tick, self).__init__()
		self._nextTime = nextTime
		self._func = func
		self.args = args
		self.kwargs = kwargs



class Timer(object):
	def __init__(self):
		super(Timer, self).__init__()
		self.heap = []

	def Process(self, curTime):
		pass

