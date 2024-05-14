# Coordinator to connect frames
from .window import Page
from .login import LoginFrame
from .sign_in import SigninFrame
from .home import HomeFrame


class Mainview:
    def __init__(self):
        # Instance
        self.window = Page()

        # For Create Frame with Dictionary
        self.frames = {}

        self.add_frame("home", HomeFrame(self, self.window))
        self.add_frame("sign_in", SigninFrame(self, self.window))
        self.add_frame("login", LoginFrame(self, self.window))

        self.window.show()

    # For Create Frame with Dictionary
    def add_frame(self, frame_name, name):
        self.frames[frame_name] = name
        # Position of the frame on the page
        self.frames[frame_name].grid(row=0, column=0, sticky="nsew")

    # Changing the frames with the switch function and returning the information inside that frame
    def switch(self, frame_name):
        self.frames[frame_name].tkraise()
        return self.frames[frame_name]
