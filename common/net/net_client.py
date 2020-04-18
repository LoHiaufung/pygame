# -*- coding: utf-8 -*-
import server.servercommon.config as ModConfig

class CBaseNetClient(object):

	def __init__(self, _strAddrAndnPort, socket, netClientMgr):
		super(CBaseNetClient, self).__init__()
		self._strAddrAndnPort = _strAddrAndnPort
		self._socket = socket
		self._netClientMgr = netClientMgr

		self._toSendBuf = []

	def SendMsg(self, strMsg):
		self._toSendBuf += strMsg

	def _CoreSendMsg(self):
		len = self._socket.send(self._toSendBuf)
		self._toSendBuf = self._toSendBuf[len:]

	def _CoreReadMsg(self):
		bEnd = False
		res = ''
		while not bEnd:
			data = self._socket.recv(ModConfig.SOCKET_MAX_READ_LEN)
			res += data
			bEnd = (len(data) < ModConfig.SOCKET_MAX_READ_LEN)
		print 'recv from', self._strAddrAndnPort, res