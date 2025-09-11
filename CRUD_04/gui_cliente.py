#!/usr/bin/env python3
# GUI Tkinter para CRUD XML-RPC

import tkinter as tk
from tkinter import messagebox
import xmlrpc.client

class CRUDGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cliente CRUD RPC")
        self.geometry("520x280")

        self.host_var = tk.StringVar(value="127.0.0.1")
        self.port_var = tk.StringVar(value="9203")
        self.item_var = tk.StringVar()
        self.idx_var = tk.StringVar()

        tk.Label(self, text="Host:").grid(row=0, column=0, padx=8, pady=6, sticky="e")
        tk.Entry(self, textvariable=self.host_var, width=16).grid(row=0, column=1, padx=8, pady=6)
        tk.Label(self, text="Puerto:").grid(row=0, column=2, padx=8, pady=6, sticky="e")
        tk.Entry(self, textvariable=self.port_var, width=8).grid(row=0, column=3, padx=8, pady=6)

        tk.Label(self, text="Índice:").grid(row=1, column=0, padx=8, pady=6, sticky="e")
        tk.Entry(self, textvariable=self.idx_var, width=10).grid(row=1, column=1, padx=8, pady=6)
        tk.Label(self, text="Item:").grid(row=1, column=2, padx=8, pady=6, sticky="e")
        tk.Entry(self, textvariable=self.item_var, width=22).grid(row=1, column=3, padx=8, pady=6)

        tk.Button(self, text="Create", command=self.create).grid(row=2, column=0, padx=8, pady=10)
        tk.Button(self, text="Read", command=self.read).grid(row=2, column=1, padx=8, pady=10)
        tk.Button(self, text="Update", command=self.update).grid(row=2, column=2, padx=8, pady=10)
        tk.Button(self, text="Delete", command=self.delete).grid(row=2, column=3, padx=8, pady=10)
        tk.Button(self, text="Read All", command=self.read_all).grid(row=3, column=0, columnspan=4, pady=6)

        self.out = tk.Text(self, height=8, width=58)
        self.out.grid(row=4, column=0, columnspan=4, padx=8, pady=8)

    def proxy(self):
        host = self.host_var.get().strip()
        port = int(self.port_var.get())
        url = f"http://{host}:{port}/RPC2"
        return xmlrpc.client.ServerProxy(url, allow_none=True)

    def create(self):
        try:
            idx = self.proxy().create(self.item_var.get())
            messagebox.showinfo("Create", f"Creado en índice {idx}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def read(self):
        try:
            val = self.proxy().read(int(self.idx_var.get()))
            self.out.delete("1.0", tk.END)
            self.out.insert(tk.END, f"{val}\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update(self):
        try:
            ok = self.proxy().update(int(self.idx_var.get()), self.item_var.get())
            messagebox.showinfo("Update", f"Actualizado: {ok}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete(self):
        try:
            ok = self.proxy().delete(int(self.idx_var.get()))
            messagebox.showinfo("Delete", f"Eliminado: {ok}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def read_all(self):
        try:
            vals = self.proxy().read_all()
            self.out.delete("1.0", tk.END)
            for i, v in enumerate(vals):
                self.out.insert(tk.END, f"[{i}] {v}\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    CRUDGUI().mainloop()
