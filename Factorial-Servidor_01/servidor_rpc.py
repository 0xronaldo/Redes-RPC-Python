#!/usr/bin/env python3
# Autor: Equipo de práctica
# Fecha: 10/09/25
# Servidor RPC (XML-RPC) para calcular factorial

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler



IP_SERVIDOR = "192.168.100.37"
PORT = 9200

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


def run_srv():
    with SimpleXMLRPCServer((IP_SERVIDOR, PORT), allow_none=True, logRequests=True) as server:
        server.register_introspection_functions()
        server.register_function(factorial, "factorial")
        print(f"[SERVIDOR] XML-RPC escuchando en http://{IP_SERVIDOR}:{PORT}/")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\n[SERVIDOR] Detenido por usuario")

if __name__ == "__main__":
    run_srv()


    

