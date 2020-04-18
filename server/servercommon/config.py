# -*- coding: utf-8 -*-


SERVER_FRAME = 30
SOCKET_MAX_READ_LEN = 1024

serverAddrDict = {
	"center_control":{
		"for_game": ("127.0.0.1", 6000),
		"for_gtw": ("127.0.0.1", 6001),
	},
	"gateway": {
		"for_client": ('127.0.0.1', 3000),
	},
	"game": {
		"for_gateway": ('127.0.0.1', 4001),
	}
}