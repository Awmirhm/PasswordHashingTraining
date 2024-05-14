# Create a Page class with ttkbootstrap that inheritance from the Window class
from ttkbootstrap import Window


class Page(Window):
    def __init__(self, weight=1000, height=800):
        super().__init__(themename="darkly", title="Password Hashing")

        # For Responsive
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Application Size
        self.geometry(f"{weight}x{height}")
        self.minsize(width=800, height=600)

    def show(self):
        self.mainloop()
