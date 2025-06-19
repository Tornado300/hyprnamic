from fabric.widgets.box import Box
from fabric.widgets.button import Button
from fabric.widgets.scrolledwindow import ScrolledWindow
from fabric.widgets.entry import Entry


class EV(Box):
    def __init__(self, name):
        super().__init__(
            name=f"{name}-box",
            style_classes=["extendedview-box"],
            orientation="h"
        )

        self.device_list = Box(
            name="device-list-outer-box",
            children=[
                ScrolledWindow(
                    name="device-list-scrolledwindow",
                    kinetic_scroll=True,
                    spacing=10,
                    min_content_size=(250, 105),
                    max_content_size=(250, 105),
                    v_scrollbar_policy="allways",
                    child=Box(
                        name="device-list-inner-box",
                        orientation="v",
                        children=[
                            Button(style_classes=["device-list-button"], label="test--"),
                            Button(style_classes=["device-list-button"], label="test"),
                            Button(style_classes=["device-list-button"], label="test"),
                            Button(style_classes=["device-list-button"], label="test"),
                            Button(style_classes=["device-list-button"], label="test"),
                            Button(style_classes=["device-list-button"], label="test"),
                            Button(style_classes=["device-list-button"], label="test"),
                            Button(style_classes=["device-list-button"], label="test"),
                            Button(style_classes=["device-list-button"], label="test"),
                            Button(style_classes=["device-list-button"], label="test"),
                            Button(style_classes=["device-list-button"], label="test"),
                            Button(style_classes=["device-list-button"], label="test"),
                            Button(style_classes=["device-list-button"], label="test"),
                            Button(style_classes=["device-list-button"], label="test"),
                            Button(style_classes=["device-list-button"], label="test"),
                            Button(style_classes=["device-list-button"], label="test"),
                            Button(style_classes=["device-list-button"], label="test"),
                            Button(style_classes=["device-list-button"], label="test"),
                            Button(style_classes=["device-list-button"], label="test__"),
                        ]
                    )
                )
            ]
        )
        self.button_list = self.device_list.children[0].child_get(0)
        print(self.button_list)

        self.device_info_header = Box(
            name="device-info-header-box",
            orientation="h",
            children=[
                Entry(
                    name="device-info-header-entry",
                    text="Device Name"
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
                Box(name="dih_dib_divider", style_classes=["h_divider"]),
                self.device_info_body
            ]

        )

        self.add(self.device_list)
        self.add(Box(name="dl_di_divider", style_classes=["v_divider"]))
        self.add(self.device_info)
