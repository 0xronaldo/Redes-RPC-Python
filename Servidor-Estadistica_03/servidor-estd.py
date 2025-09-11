#!/usr/bin/env python3
# Servidor XML-RPC para estadísticas: mean, median, stdev

from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import statistics as stats

def mean(values):
	return float(stats.mean(list(map(float, values))))

def median(values):
	return float(stats.median(list(map(float, values))))

def stdev(values):
	vals = list(map(float, values))
	# Para stdev se requiere n>=2
	return float(stats.stdev(vals)) if len(vals) >= 2 else 0.0

class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ("/RPC2",)

def main():
	host = "127.0.0.1"
	port = 9202
	with SimpleXMLRPCServer((host, port), requestHandler=RequestHandler, allow_none=True, logRequests=True) as server:
		server.register_introspection_functions()
		server.register_function(mean, "mean")
		server.register_function(median, "median")
		server.register_function(stdev, "stdev")
		print(f"[SERVIDOR] Estadística en http://{host}:{port}/RPC2")
		try:
			server.serve_forever()
		except KeyboardInterrupt:
			print("\nDetenido.")

if __name__ == "__main__":
	main()