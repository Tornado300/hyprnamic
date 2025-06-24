from fabric.widgets.box import Box
from fabric.widgets.button import Button
from fabric.widgets.scale import Scale


class QVAudio(Box):
    def __init__(self, callback):
        super().__init__(
            name="audio-box",
            orientation="v"
        )
        self.callback = callback
        self.button = Button(
            name="audio-button",
            label="kein Gerät",
            on_clicked=self.callback
        )

        self.slider = Scale(
            name="audio-slider",
            min_value=0,
            max_value=200,
            value=50,
            draw_value=True,
            h_expand=True,
            all_visible=True,
            value_position="right",
            digits=0
        )

        self.add(self.button)
        self.add(self.slider)

