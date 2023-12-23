from model import Model
from view import View


class Controller:
    def __init__(self) -> None:
        self.model = Model()
        self.view = View(self)

    def main(self) -> None:
        self.view.main()

    def on_button_click(self) -> None:
        select = self.view.get_select()
        self.model.button_action(select)
