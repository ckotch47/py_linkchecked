import sys
from tkinter import ttk


class gui_service:
    @staticmethod
    def table_settings(window):
        table = ttk.Treeview(window, selectmode='extended')
        table['columns'] = ['link', 'status', 'time']
        table.column("#0", width=0, stretch=False)
        table.column('link', anchor='w', width=600, stretch=True)
        table.column('status', anchor='center', width=60, stretch=False)
        table.column('time', width=60, anchor='center', stretch=False)

        table.heading("#0", text="", anchor='center')
        table.heading("link", text="link", anchor='center')
        table.heading("status", text="status", anchor='center')
        table.heading("time", text="time", anchor='center')

        yscrollbarTwo = ttk.Scrollbar(window, orient='vertical', command=table.yview)
        table.configure(yscrollcommand=yscrollbarTwo.set)

        yscrollbarTwo.grid(row=1, column=2, sticky='nse', rowspan=1)
        yscrollbarTwo.configure(command=table.yview)
        table.tag_configure('green', background='green')
        table.tag_configure('red', background='red')

        return table

    def table_values_settings(self, window):
        table = ttk.Treeview(window, selectmode='extended')
        table['columns'] = ['name', 'value']
        table.column("#0", width=0, stretch=False)
        table.column('name', anchor='w', width=200, stretch=False)
        table.column('value', anchor='w', width=100, stretch=True)

        table.heading("#0", text="", anchor='center')
        table.heading("name", text="name", anchor='center')
        table.heading("value", text="value", anchor='center')

        yscrollbarTwo = ttk.Scrollbar(window, orient='vertical', command=table.yview)
        table.configure(yscrollcommand=yscrollbarTwo.set)

        yscrollbarTwo.grid(row=2, column=2, sticky='nse', rowspan=1)
        yscrollbarTwo.configure(command=table.yview)

        return table


class mouse_button:
    left = 'Button-1'
    right = 'Button-3'
    center = 'Button-2'
    double_left = 'Double-1'
    double_right = 'Double-2'

    def __init__(self):
        if sys.platform == 'darwin':
            self.left = 'Button-0'
            self.right = 'Button-2'
            self.center = 'Button-1'
            self.double_left = 'Double-0'
            self.double_right = 'Double-1'


m_btn = mouse_button()
guiServie = gui_service()
