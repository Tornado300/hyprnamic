from fabric.widgets.box import Box
from fabric.widgets.button import Button


class QVWlan(Box):
    def __init__(self, callback):
        super().__init__(
            name="wlan-box",
            h_expand=True
        )
        self.callback = callback
        self.button = Button(
            name="wlan-button",
            label="Nicht Verbunden",
            h_expand=True,
            on_clicked=self.callback
        )

        self.add(self.button)
