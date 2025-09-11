#!/usr/bin/env python3
# GUI Tkinter para estadísticas

import tkinter as tk
from tkinter import ttk, messagebox
import xmlrpc.client

class EstadisticaGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cliente Estadística RPC")
        self.geometry("520x220")

        self.host_var = tk.StringVar(value="127.0.0.1")
        self.port_var = tk.StringVar(value="9202")
        self.mode_var = tk.StringVar(value="mean")
        self.data_var = tk.StringVar()
        self.output_var = tk.StringVar(value="Resultado: —")

        row = 0
        tk.Label(self, text="Host:").grid(row=row, column=0, padx=8, pady=6, sticky="e")
        tk.Entry(self, textvariable=self.host_var, width=16).grid(row=row, column=1, padx=8, pady=6)
        tk.Label(self, text="Puerto:").grid(row=row, column=2, padx=8, pady=6, sticky="e")
        tk.Entry(self, textvariable=self.port_var, width=8).grid(row=row, column=3, padx=8, pady=6)

        row += 1
        ttk.Combobox(self, textvariable=self.mode_var, values=["mean", "median", "stdev"], width=12).grid(row=row, column=0, columnspan=2, padx=8, pady=6)
        tk.Entry(self, textvariable=self.data_var, width=34).grid(row=row, column=2, columnspan=2, padx=8, pady=6)
        tk.Label(self, text="(Separar por espacios o comas)").grid(row=row+1, column=2, columnspan=2)

        row += 2
        tk.Button(self, text="Calcular", command=self.calcular).grid(row=row, column=0, columnspan=4, pady=10)

        row += 1
        tk.Label(self, textvariable=self.output_var, font=("Segoe UI", 11, "bold")).grid(row=row, column=0, columnspan=4, pady=8)

    def calcular(self):
        try:
            host = self.host_var.get().strip()
            port = int(self.port_var.get())
            data_str = self.data_var.get()
            if not data_str.strip():
                raise ValueError("Debe ingresar datos numéricos")
            data = [float(x) for x in data_str.replace(",", " ").split()]
            url = f"http://{host}:{port}/RPC2"
            proxy = xmlrpc.client.ServerProxy(url, allow_none=True)
            op = self.mode_var.get()
            res = getattr(proxy, op)(data)
            self.output_var.set(f"Resultado: {res}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    EstadisticaGUI().mainloop()
