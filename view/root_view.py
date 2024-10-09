from tkinter import Tk, Label, Button

from view import transcript_view


class RootView(Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("Home")

        Label(self, text="Welcome to the asset Recorder").pack()
        Button(self, text="View Transcript", command=controller.transcript_controller).pack()
        Button(self, text="View Holdings", command=controller.holdings_controller).pack()


