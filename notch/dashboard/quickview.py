from fabric.widgets.box import Box
from notch.dashboard.wlan import QVWlan
from notch.dashboard.bluetooth import QVBluetooth
from notch.dashboard.audio import QVAudio
from notch.dashboard.quickbuttons import QVQuickbutton


class QuickView(Box):
    def __init__(
            self,
            wlan_callback,
            bluetooth_callback,
            audio_input_callback,
            audio_output_callback
    ):
        super().__init__(
            name="quickview-box",
            orientation="h",
            h_expand=True,
            h_align="center",
            show=True,
            show_all=True
        )
        self.qv_wlan = QVWlan(wlan_callback)
        self.qv_bluetooth = QVBluetooth(bluetooth_callback)
        self.qv_audio_input = QVAudio(audio_input_callback)
        self.qv_audio_output = QVAudio(audio_output_callback)
        self.qb1 = QVQuickbutton("quickbuttons-button1")
        self.qb2 = QVQuickbutton("quickbuttons-button2")
        self.qb3 = QVQuickbutton("quickbuttons-button3")
        self.qb4 = QVQuickbutton("quickbuttons-button4")

        self.left_box = Box(
            name="left-box",
            orientation="v",
            children=[
                self.qv_wlan,
                Box(name="wl_ai_divider", style_classes=["h_divider"]),
                self.qv_audio_input
            ]
        )

        self.right_box = Box(
            name="right-box",
            orientation="v",
            children=[
                self.qv_bluetooth,
                Box(name="bt_ao_divider", style_classes=["h_divider"]),
                self.qv_audio_output
            ]
        )

        self.quickbuttons_box = Box(
            name="quickbuttons-box",
            orientation="h",
            children=[
                Box(
                    name="quickbuttons-box-left",
                    orientation="v",
                    v_expand=True,
                    h_expand=True,
                    children=[
                        self.qb1,
                        self.qb3
                    ]
                ),
                Box(
                    name="quickbuttons-box-right",
                    orientation="v",
                    v_expand=True,
                    h_expand=True,
                    children=[
                        self.qb2,
                        self.qb4
                    ]
                )
            ]
        )
        self.add(self.left_box)
        self.add(self.right_box)
        self.add(self.quickbuttons_box)
