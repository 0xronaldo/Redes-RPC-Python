#!/usr/bin/env python3
# Servidor XML-RPC para multiplicación de matrices

from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler

def matmul(A, B):
    # Validación básica
    if not A or not B:
        return []
    n = len(A)
    m = len(A[0])
    p = len(B)
    q = len(B[0]) if B else 0
    if m != p:
        raise ValueError("Dimensiones incompatibles: cols(A) != rows(B)")
    # Multiplicación
    C = [[0 for _ in range(q)] for _ in range(n)]
    for i in range(n):
        for k in range(m):
            aik = float(A[i][k])
            for j in range(q):
                C[i][j] += aik * float(B[k][j])
    return C

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/RPC2",)

def main():
    host = "127.0.0.1"
    port = 9204
    with SimpleXMLRPCServer((host, port), requestHandler=RequestHandler, allow_none=True, logRequests=True) as server:
        server.register_introspection_functions()
        server.register_function(matmul, "matmul")
        print(f"[SERVIDOR] Matrices en http://{host}:{port}/RPC2")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nDetenido.")

if __name__ == "__main__":
    main()
