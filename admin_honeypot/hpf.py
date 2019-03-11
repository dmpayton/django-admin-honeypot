import socket
import datetime
import json


class hpflogger:
	def __init__(self, hpfserver, hpfport, hpfident, hpfsecret, hpfchannel, serverid):
		self.hpfserver = hpfserver
		self.hpfport = hpfport
		self.hpfident = hpfident
		self.hpfsecret = hpfsecret
		self.hpfchannel = hpfchannel
		self.serverid = serverid
		self.hpc = None
		if (self.hpfserver and self.hpfport and self.hpfident and self.hpfport and self.hpfchannel and self.serverid):
			import logging
			logging.basicConfig()
			import hpfeeds
			try:
				self.hpc = hpfeeds.new(self.hpfserver, self.hpfport, self.hpfident, self.hpfsecret)
				self.status = "Logging to hpfeeds using server: {0}, channel {1}.".format(self.hpfserver, self.hpfchannel)
			except (hpfeeds.FeedException, socket.error, hpfeeds.Disconnect):
				self.status = "hpfeeds connection not successful"
	def log(self, message):
		if self.hpc:
			message['serverid'] = self.serverid
			self.hpc.publish(self.hpfchannel, json.dumps(message))
