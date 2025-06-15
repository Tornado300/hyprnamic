from fabric.widgets.box import Box
from fabric.widgets.button import Button
from fabric.widgets.entry import Entry


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


class EVWlan(Box):
    def __init__(self):
        super().__init__(
            name="wlan-box",
            style_classes=["extendedview-box"],
            orientation="h"
        )

        self.device_list = Box(
            name="device-list-box"
        )

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
            h_expand=True,
            children=[
                self.device_info_header,
                Box(name="h_devider", style_classes=["v_divider"]),
                self.device_info_body
            ]
        )
        self.add(self.device_list)
        self.add(self.device_info)
