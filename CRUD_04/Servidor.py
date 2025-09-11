#!/usr/bin/env python3
# Servidor XML-RPC CRUD en memoria

from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler

class Store:
	def __init__(self):
		self.data = []

	def create(self, item: str) -> int:
		self.data.append(str(item))
		return len(self.data) - 1

	def read_all(self):
		return list(self.data)

	def read(self, idx: int):
		return self.data[idx]

	def update(self, idx: int, item: str) -> bool:
		self.data[idx] = str(item)
		return True

	def delete(self, idx: int) -> bool:
		del self.data[idx]
		return True

class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ("/RPC2",)

def main():
	host = "127.0.0.1"
	port = 9203
	store = Store()
	with SimpleXMLRPCServer((host, port), requestHandler=RequestHandler, allow_none=True, logRequests=True) as server:
		server.register_introspection_functions()
		server.register_instance(store, allow_dotted_names=True)
		print(f"[SERVIDOR] CRUD en http://{host}:{port}/RPC2")
		try:
			server.serve_forever()
		except KeyboardInterrupt:
			print("\nDetenido.")

if __name__ == "__main__":
	main()