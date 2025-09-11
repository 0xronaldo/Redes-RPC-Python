#!/usr/bin/env python3
# Autor: Equipo de práctica
# Fecha: 10/09/25
# Servidor RPC (XML-RPC) para calcular factorial

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Cálculo iterativo para evitar límites de recursión
def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("n debe ser entero")
    if n < 0:
        raise ValueError("n debe ser no negativo")
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/RPC2",)

def main():
    host = "127.0.0.1"
    port = 9200
    with SimpleXMLRPCServer((host, port), requestHandler=RequestHandler, allow_none=True, logRequests=True) as server:
        server.register_introspection_functions()
        server.register_function(factorial, "factorial")
        print(f"[SERVIDOR] XML-RPC escuchando en http://{host}:{port}/RPC2")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\n[SERVIDOR] Detenido por usuario")

if __name__ == "__main__":
    main()


    

