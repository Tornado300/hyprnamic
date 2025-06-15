from fabric.widgets.box import Box
from fabric.widgets.button import Button


class QVWlan(Box):
    def __init__(self):
        super().__init__(
            name="wlan-box",
            h_expand=True
        )

        self.button = Button(
            name="wlan-button",
            label="Nicht Verbunden",
            h_expand=True
        )

        self.add(self.button)
