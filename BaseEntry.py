import tkinter as tk

class BaseEntry(tk.Entry):
    def __init__(self, root=None, placeholder="PlaceHolder", color="#bebfc1", **options):
        super().__init__(root, options)

        self.placeholder = placeholder
        self.placeholder_color = "#7d7f83"
        self.default_fg_color = color
        self['bg'] = '#484b51'

        self.bind("<FocusIn>", self.focus_in)
        self.bind("<FocusOut>", self.focus_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def focus_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def focus_out(self, *args):
        if not self.get():
            self.put_placeholder()
