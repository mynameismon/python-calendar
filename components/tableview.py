try:
    import Tkinter as tk
    import tkFont
    import ttk
except ImportError:  # Python 3
    import tkinter as tk
    import tkinter.font as tkFont
    import tkinter.ttk as ttk

class MultiColumnListbox():
    """use a ttk.TreeView as a multicolumn ListBox"""

    columns = None
    rows = None
    window = None
    def __init__(self, window, columns, rows):
        self.tree = None
        self.columns = columns
        self.window = window
        self.rows = rows
        self._setup_widgets()
        self._build_tree()
        

    def _setup_widgets(self):
        s = """Click on header to sort by that column
        to change width of column drag boundary"""

        msg = ttk.Label(self.window, wraplength="4i", justify="left", anchor="n",
            padding=(10, 2, 10, 6), text=s)
        
        msg.grid(column=3, row = 10)
        container = ttk.Frame(self.window)
        container.grid(column=1, row=10)
        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(container, columns=self.columns, show="headings")
        vsb = ttk.Scrollbar(container, orient="vertical",
            command=self.tree.yview)
        hsb = ttk.Scrollbar(container, orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in self.columns:
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: sortby(self.tree, c, 0))
            # adjust the column's width to the header string
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))

        for item in self.rows:
            item = [[x,] for x in item] # gets around tkinter trying to be smart: https://stackoverflow.com/a/66769723/9496502
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(self.columns[ix],width=None)<col_w:
                    self.tree.column(self.columns[ix], width=col_w)

def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, col), child) \
        for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    #data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col, \
        int(not descending)))

