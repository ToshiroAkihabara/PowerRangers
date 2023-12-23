from model import Model
from view import View


class Controller:
    def __init__(self) -> None:
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()

    def on_button_click(self):
        select = self.view.get_select()
        return self.model.button_action(select)
