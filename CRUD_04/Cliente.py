#!/usr/bin/env python3
# Cliente CLI para CRUD XML-RPC

import argparse
import xmlrpc.client

def main():
	parser = argparse.ArgumentParser(description="Cliente CRUD")
	parser.add_argument("op", choices=["create", "read", "read_all", "update", "delete"])
	parser.add_argument("arg1", nargs="?")
	parser.add_argument("arg2", nargs="?")
	parser.add_argument("--host", default="127.0.0.1")
	parser.add_argument("--port", type=int, default=9203)
	args = parser.parse_args()

	url = f"http://{args.host}:{args.port}/RPC2"
	proxy = xmlrpc.client.ServerProxy(url, allow_none=True)

	if args.op == "create":
		idx = proxy.create(args.arg1 if args.arg1 is not None else input("Item: "))
		print(idx)
	elif args.op == "read":
		print(proxy.read(int(args.arg1)))
	elif args.op == "read_all":
		print(proxy.read_all())
	elif args.op == "update":
		print(proxy.update(int(args.arg1), args.arg2 if args.arg2 is not None else input("Nuevo valor: ")))
	elif args.op == "delete":
		print(proxy.delete(int(args.arg1)))

if __name__ == "__main__":
	main()