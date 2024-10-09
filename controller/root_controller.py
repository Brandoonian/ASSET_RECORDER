from view.root_view import RootView

from controller.transcript_controller import TranscriptController
from controller.holdings_controller import HoldingsController

from repository.holdings_repository import HoldingsRepository

class RootController:
    def __init__(self):
        self.view = RootView(self)
        self.holdings_repository = HoldingsRepository()

    def run(self):
        self.view.mainloop()

    def transcript_controller(self):
        TranscriptController(self)

    def holdings_controller(self):
        HoldingsController(self)
