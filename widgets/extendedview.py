from fabric.widgets.box import Box
from fabric.widgets.button import Button
from fabric.widgets.scrolledwindow import ScrolledWindow
from fabric.widgets.entry import Entry


class EV(Box):
    def __init__(self, name, buttonfactory, ):
        super().__init__(
            name=f"{name}-box",
            style_classes=["extendedview-box"],
            orientation="h"
        )

        self.device_list = Box(
            name="device-list-outer-box",
            children=[
                ScrolledWindow(
                    kinetic_scroll=True,
                    child=Box(
                        name="device-list-inner-box",
                        orientation="v",
                        children=[
                            Button(label="test1"),
                            Button(label="test2"),
                            Button(label="test3"),
                            Button(label="test4"),
                            Button(label="test5")
                        ]
                    )
                )
            ]
        )
        self.button_list = self.device_list.children[0].child_get().children[0]
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
            h_expand=True,
            children=[
                self.device_info_header,
                Box(name="dih_dib_divider", style_classes=["h_divider"]),
                self.device_info_body
            ]

        )

        self.add(self.device_list)
        self.add(Box(name="dl_di_divider", style_classes=["v_divider"]))
        self.add(self.device_info)
