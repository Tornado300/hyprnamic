from fabric.widgets.box import Box
from fabric.widgets.button import Button
from fabric.widgets.scale import Scale
from fabric.widgets.entry import Entry


class QVAudio(Box):
    def __init__(self):
        super().__init__(
            name="audio-box",
            orientation="v"
        )

        self.button = Button(
            name="audio-button",
            label="kein Gerät",
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


class EVAudio(Box):
    def __init__(self, variant):
        super().__init__(
            name="audio-box",
            style_classes=["extendedview-box"],
            orientation="h"
        )

        self.device_list = None

        self.device_info_header = Box(
            name="device-info-header-box",
            orientation="h",
            children=[
                Entry(
                    name="device-info-header-entry",
                )
            ]
        )
        self.device_info_body = Box(
            name="device-info-body-box",
        )
        self.device_info = Box(
            name="device-info-box",
            orientation="v",
            children=[
                self.device_info_header,
                Box(name="h_devider", style_classes=["h_divider"]),
                self.device_info_body
            ]

        )
        self.add(self.device_list)
        self.add(self.device_info)
