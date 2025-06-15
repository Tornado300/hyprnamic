from fabric.widgets.box import Box
from fabric.widgets.revealer import Revealer
from notch.dashboard.quickview import QuickView
from notch.dashboard.bluetooth import EVBluetooth


class Dashboard(Box):
    def __init__(self):
        super().__init__(
            name="dashboard-box",
            orientation="v"
        )

        self.quickview = QuickView()
        self.revealer = Revealer(
            name="revealer",
            # transition_type=None,
            transition_duration=10,
            child=EVBluetooth()
        )

        self.add(self.quickview)
        self.add(self.revealer)
        self.extend()

    def extend(self):
        self.revealer.reveal()
