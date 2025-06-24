from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.revealer import Revealer
from notch.dashboard.quickview import QuickView
from widgets.extendedview import EV
from services.audio import Audio


class Dashboard(Box):
    def __init__(self):
        super().__init__(
            name="dashboard-box",
            orientation="v"
        )
        self.audio_service = Audio(200, "fabric audio control")
        self.registered_audio_devices = set()

        self.current_ev = None
        self.quickview = QuickView(
            wlan_callback=lambda: self.extend("wlan"),
            bluetooth_callback=lambda: self.extend("bluetooth"),
            audio_input_callback=lambda: self.extend("audio"),
            audio_output_callback=lambda: self.extend("audio")
        )
        self.revealer = Revealer(
            name="revealer",
            transition_type="slide-down",
            transition_duration=400,
        )

        self.add(self.quickview)
        self.add(self.revealer)
        self.extend("wlan")

    def extend(self, variant):
        match variant:
            case "wlan":
                self.revealer.set_property("child", EV("wlan", Label("test1!")))
            case "audio":
                pass
                # self.audio_service.connect("changed", self.speakers_changed)
                # self.audio_service.connect("stream-added", self.on_stream_added)
                # self.audio_service.connect("stream-removed", self.test)
                # self.audio_service.connect("microphone_changed", self.microphone_changed)
        self.revealer.reveal()

    def contract(self):
        self.revealer.unreveal()

    def on_stream_added(self, audio, stream):
        stream_type = str(stream.stream.__class__).replace("<class 'gi.repository.Cvc.", "").replace("'>", "")
        if "SourceOutput" in stream_type or "SinkInput" in stream_type:
            return

        if stream_type in self.registered_audio_devices:
            return

        

        # print((stream.stream.get_channel_map().get_mapping())) # get mono/stereo/5.1
        # print(stream.stream.get_id())
        # print(stream.stream.get_card_index())
        # print(dir(stream.stream))
        print(stream_type, "->", stream.name)
