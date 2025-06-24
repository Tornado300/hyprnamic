from fabric.widgets.box import Box
from fabric.widgets.button import Button


class QVBluetooth(Box):
    def __init__(self, callback):
        super().__init__(
            name="bluetooth-box",
            h_expand=True
        )
        self.callback = callback
        self.button = Button(
            name="bluetooth-button",
            label="Nicht Verbunden",
            h_expand=True,
            on_clicked=self.callback
        )

        self.add(self.button)
