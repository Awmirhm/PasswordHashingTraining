# Create Sign in Frame
from ttkbootstrap import Frame, Labelframe, Label, Entry, DARK, SUCCESS, Button, OUTLINE, WARNING
from ttkbootstrap.dialogs import Messagebox
from BusinessLogicLayer.user_business import UserBusiness


class SigninFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.view = view

        self.user_business = UserBusiness()

        self.grid_columnconfigure(0, weight=1)

        # Label Frame
        self.header = Labelframe(self, text="Create Your Account", bootstyle=SUCCESS)
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.header.grid_columnconfigure(1, weight=1)

        # First Name
        self.firstname_label = Label(self.header, text="First Name : ", foreground="gray")
        self.firstname_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.firstname_entry = Entry(self.header, bootstyle=DARK)
        self.firstname_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Last Name
        self.lastname_label = Label(self.header, text="Last Name : ", foreground="gray")
        self.lastname_label.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.lastname_entry = Entry(self.header, bootstyle=DARK)
        self.lastname_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Username
        self.username_label = Label(self.header, text="Username : ", foreground="gray")
        self.username_label.grid(row=2, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.username_entry = Entry(self.header, bootstyle=DARK)
        self.username_entry.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Password
        self.password_label = Label(self.header, text="Password : ", foreground="gray")
        self.password_label.grid(row=3, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.password_entry = Entry(self.header, bootstyle=DARK)
        self.password_entry.grid(row=3, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Save Button
        self.save_button = Button(self.header, text="Save", command=self.save_button_clicked,
                                  bootstyle=OUTLINE)
        self.save_button.grid(row=4, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

        # Back To Login Page
        self.back_to_login_page_button = Button(self, text="Back To Login Page", bootstyle=WARNING,
                                                command=self.back_to_login_page_button_clicked)
        self.back_to_login_page_button.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")

    def save_button_clicked(self):
        # Get Firstname,Lastname,Username,Password
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        result = self.user_business.sign_in(firstname, lastname, username, password)
        save_message = result[0]
        error_message = result[1]

        if error_message:
            Messagebox.show_error(title="Error", message=error_message, alert=True)
        else:
            Messagebox.show_info(title="Info", message=save_message, alert=True)

    def back_to_login_page_button_clicked(self):
        self.view.switch("login")
