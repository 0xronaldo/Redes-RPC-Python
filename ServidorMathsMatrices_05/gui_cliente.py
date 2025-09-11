#!/usr/bin/env python3
# GUI Tkinter para multiplicación de matrices

import tkinter as tk
from tkinter import messagebox
import xmlrpc.client

class MatmulGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cliente Matrices RPC")
        self.geometry("620x360")

        self.host_var = tk.StringVar(value="127.0.0.1")
        self.port_var = tk.StringVar(value="9204")
        tk.Label(self, text="Host:").grid(row=0, column=0, padx=8, pady=6, sticky="e")
        tk.Entry(self, textvariable=self.host_var, width=16).grid(row=0, column=1, padx=8, pady=6)
        tk.Label(self, text="Puerto:").grid(row=0, column=2, padx=8, pady=6, sticky="e")
        tk.Entry(self, textvariable=self.port_var, width=8).grid(row=0, column=3, padx=8, pady=6)

        tk.Label(self, text="Matriz A (filas con ';'):").grid(row=1, column=0, columnspan=4, padx=8, pady=4, sticky="w")
        self.txtA = tk.Text(self, height=5, width=70)
        self.txtA.grid(row=2, column=0, columnspan=4, padx=8)

        tk.Label(self, text="Matriz B (filas con ';'):").grid(row=3, column=0, columnspan=4, padx=8, pady=4, sticky="w")
        self.txtB = tk.Text(self, height=5, width=70)
        self.txtB.grid(row=4, column=0, columnspan=4, padx=8)

        tk.Button(self, text="Multiplicar", command=self.matmul).grid(row=5, column=0, columnspan=4, pady=10)

        self.txtC = tk.Text(self, height=6, width=70)
        self.txtC.grid(row=6, column=0, columnspan=4, padx=8, pady=6)

    def parse_matrix(self, s: str):
        rows = [r.strip() for r in s.replace('\n', ' ').split(';') if r.strip()]
        return [[float(x) for x in r.replace(',', ' ').split()] for r in rows]

    def matmul(self):
        try:
            host = self.host_var.get().strip()
            port = int(self.port_var.get())
            url = f"http://{host}:{port}/RPC2"
            proxy = xmlrpc.client.ServerProxy(url, allow_none=True)
            A = self.parse_matrix(self.txtA.get("1.0", tk.END))
            B = self.parse_matrix(self.txtB.get("1.0", tk.END))
            C = proxy.matmul(A, B)
            self.txtC.delete("1.0", tk.END)
            for row in C:
                self.txtC.insert(tk.END, ' '.join(f"{v:.2f}" for v in row) + "\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    MatmulGUI().mainloop()
