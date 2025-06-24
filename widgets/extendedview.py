from fabric.widgets.box import Box
from fabric.widgets.button import Button
from fabric.widgets.scrolledwindow import ScrolledWindow
from fabric.widgets.entry import Entry


class Device:
    def __init__(self, name, obj, volume=None, muted=None, status=None, signal_strength=None):
        self.name = name
        self.obj = obj
        self.volume = volume
        self.muted = muted
        self.status = status
        self.signal_strength = signal_strength


class EV(Box):
    def __init__(self, name, info_layout):
        super().__init__(
            name=f"{name}-box",
            style_classes=["extendedview-box"],
            orientation="h"
        )
        self.info_layout = info_layout
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
                        ]
                    )
                )
            ]
        )
        self.button_list = self.device_list.children[0].children[0].get_child().children
        print("#+#", self.button_list)

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
            children=[
                self.info_layout
            ]
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
        self.add_device("test123", None)

    def add_device(self, name, obj, volume=None, muted=None, status=None, signal_strength=None):
        # print(self.button_list)
        new_device = Device(name=name, obj=obj, volume=volume, muted=muted, status=status, signal_strength=signal_strength)
        btn = Button(
            name=f"device_list_button_{len(self.button_list)}",
            label=name,
            style_classes="device-list-button"
        )
        self.device_list.children[0].children[0].get_child().add(btn)
        # print(self.button_list)
        print(self.device_list.children[0].children[0].get_child().children)
        pass

    def load_device(self):
        pass
