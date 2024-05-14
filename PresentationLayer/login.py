# Create Login Frame
from ttkbootstrap import Frame, Labelframe, Label, Entry, END, Button, WARNING, OUTLINE, INFO, DANGER
from ttkbootstrap.dialogs import Messagebox
from BusinessLogicLayer.user_business import UserBusiness


class LoginFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.view = view

        self.user_business = UserBusiness()

        self.grid_columnconfigure(0, weight=1)

        # Label Frame
        self.header = Labelframe(self, text="Login Whit Your Account", bootstyle=WARNING)
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.header.grid_columnconfigure(1, weight=1)

        # Username
        self.username_label = Label(self.header, text="Username : ", foreground="gray")
        self.username_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.username_entry = Entry(self.header, bootstyle=INFO, foreground="white")
        self.username_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Password
        self.password_label = Label(self.header, text="Password : ", foreground="gray")
        self.password_label.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.password_entry = Entry(self.header, bootstyle=INFO, foreground="white", show="*")
        self.password_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Login Button
        self.login_button = Button(self.header, bootstyle=OUTLINE + INFO, text="Login",
                                   command=self.login_button_clicked)
        self.login_button.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

        # Sign in Button
        self.singing_button = Button(self.header, text="Sign in", command=self.singing_button_clicked,
                                     bootstyle=DANGER + OUTLINE)
        self.singing_button.grid(row=3, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

    def login_button_clicked(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        result = self.user_business.login(username, password)
        user = result[0]
        error_message = result[1]

        if error_message:
            Messagebox.show_error(error_message, title="Error", alert=True)
        else:

            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            home_frame = self.view.switch("home")
            home_frame.set_current_user(user)

    def singing_button_clicked(self):
        self.view.switch("sign_in")
