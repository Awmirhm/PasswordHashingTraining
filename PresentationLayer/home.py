# Create Home Frame

from ttkbootstrap import Frame, Label


class HomeFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.view = view

        self.current_user = None

        # Add Label
        self.header = Label(self, text="Wellcome")
        self.header.pack(pady=150)

    # Setting the current user from the login page
    def set_current_user(self, current_user):
        self.current_user = current_user

        self.header.config(text=f"Wellcome, {self.current_user.firstname} {self.current_user.lastname}")
