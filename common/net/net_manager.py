# -*- coding: utf-8 -*-
import socket
import select
from net_client import CBaseNetClient

class CBaseNetManager(object):

	def __init__(self):
		super(CBaseNetManager, self).__init__()
		self._AddrAndPort = None # (strAddr, nPort)
		self._mySocket = None

		self._rdSocketSet = set([])
		self._socket2NetClient = {}

	def GetNetClientCls(self):
		return CBaseNetClient


	def StartListen(self, strAddrAndnPort):
		print 'start listen', strAddrAndnPort
		self._AddrAndPort = strAddrAndnPort
		self._mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._mySocket.bind(strAddrAndnPort)
		self._mySocket.listen(10)

	def OnFrameUpdate(self):
		socketLst = list(self._rdSocketSet)
		r_list, w_list, e_list = select.select(socketLst+[self._mySocket], [], socketLst, 0)
		# readable
		for soc in r_list:
			if soc is self._mySocket:
				self.OnNewClient()
			else:
				self.OnRecvFromClient(soc)
		# writable
		for soc in w_list:
			self.OnClientWritable(soc)

		# exception
		for soc in e_list:
			self.OnClientExcept(soc)


	def OnNewClient(self):
		pSock, strAddrAndnPort = self._mySocket.accept()
		pNetClient = self.GetNetClientCls()(strAddrAndnPort, pSock, self)

		self._rdSocketSet.add(pSock)
		self._socket2NetClient[pSock] = pNetClient

		print 'new connect from:', strAddrAndnPort

	def OnRecvFromClient(self, soc):
		netClient = self._socket2NetClient.get(soc)
		if netClient:
			netClient._CoreReadMsg()

	def OnClientWritable(self, soc):
		netClient = self._socket2NetClient.get(soc)
		if netClient:
			netClient._CoreSendMsg()

	def OnClientExcept(self, soc):
		pass
