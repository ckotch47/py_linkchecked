import time
from tkinter import Tk, ttk, NO, CENTER, StringVar, N, E, YES
from threading import Thread

from gui_config import guiServie, m_btn
from service import service


class my_gui:
    def __init__(self):
        self.table_values = None
        self.th_check_link = None
        self.input_host = None
        self.table = None
        self.tk = Tk()
        self.tk.rowconfigure(1, weight=2)
        self.tk.columnconfigure(1, weight=2)
        self.host_ent = StringVar()

    def gui(self):
        self.input_host = ttk.Entry(self.tk, width=100, textvariable=self.host_ent)
        self.input_host.grid(row=0, column=0, sticky='nwe', padx=5, pady=5)

        printBtn = ttk.Button(self.tk, text='start', command=self.start)
        printBtn.grid(row=0, column=1, sticky='ne', columnspan=1, pady=5, padx=5)

        printBtn = ttk.Button(self.tk, text='stop', command=self.stop)
        printBtn.grid(row=0, column=2, sticky='ne', columnspan=1, pady=5, padx=5)

        self.table = guiServie.table_settings(self.tk)
        self.table.bind(f'<{m_btn.left}>', self.double_click_row)
        self.table.grid(row=1, column=0, padx=(5, 20), pady=5, sticky="nsew", columnspan=3)

        self.table_values = guiServie.table_values_settings(self.tk)
        self.table_values.grid(row=2, column=0, padx=(5, 20), pady=5, sticky="nsew", columnspan=3)
        self.tk.mainloop()

    def start(self):
        tmp_host = self.host_ent.get()
        self.th_check_link = Thread(target=service.start,
                                    args=(self.table, tmp_host))
        self.th_check_link.start()

    def stop(self):
        service.while_true = False
        self.th_check_link.join(timeout=0)
        self.th_check_link = None

    def double_click_row(self, event):
        self.table_values.delete(*self.table_values.get_children())
        iid = self.table.focus()
        val = service.get_values_by_id(int(float(iid)))
        self.table_values.insert(parent='', index='end', values=('title', val.title))
        self.table_values.insert(parent='', index='end', values=('description', val.title))

gui = my_gui()


