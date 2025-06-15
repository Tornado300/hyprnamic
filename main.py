# from modules.controller import Controller
import json
import os
from notch.notch import Notch
from fabric import Application
from fabric.notifications.service import Notifications
from fabric.utils import get_relative_path, monitor_file
import setproctitle
from gi.repository import Gray
import gi
gi.require_version('Gray', '0.1')


def list_all_files(root_dir):
    files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            files.append(os.path.join(dirpath, filename))
    return files


if __name__ == "__main__":

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with open("./data/data.json", "r") as file:
        try:
            data = json.load(file)
        except json.decoder.JSONDecodeError:
            data = {"username": None, "hostname": None, "home_dir": None, "wallpapers_dir": None, "cache_dir": None}

    with open("./data/project_manager.json") as file:
        try:
            manager_data = json.load(file)
        except json.decoder.JSONDecodeError:
            manager_data = {}

    with open("./data/audio.json") as file:
        try:
            audio_data = json.load(file)
        except json.decoder.JSONDecodeError:
            audio_data = {}

    with open("./data/launcher.json") as file:
        try:
            launcher_data = json.load(file)
        except json.decoder.JSONDecodeError:
            launcher_data = {}

    data["username"] = os.getlogin()
    data["hostname"] = os.uname().nodename
    data["home_dir"] = os.path.expanduser("~/")
    data["wallpapers_dir"] = os.path.expanduser("~/.backgrounds/")
    data["cache_dir"] = os.path.expanduser("~/.cache/desktop_ui/")

    with open("./data/data.json", "w") as file:
        json.dump(data, file, indent=2)

    with open("./data/audio.json", "w") as file:
        json.dump(audio_data, file, indent=2)

    with open("./data/launcher.json", "w") as file:
        json.dump(launcher_data, file, indent=2)

    with open("./data/project_manager.json", "w") as file:
        json.dump(manager_data, file, indent=2)

    setproctitle.setproctitle("dev-ui")
    notification_server = Notifications()
    sys_tray_server = Gray.Watcher()
    # bar0 = Bar(monitor_id=0, server=sys_tray_server)
    # bar1 = Bar(monitor_id=1, server=sys_tray_server)
    notch0 = Notch(monitor_id=0, server=notification_server)
    notch1 = Notch(monitor_id=1, server=notification_server)
    # controller = Controller()
    # app = Application("dev-ui", bar0, bar1, notch0, notch1, controller, open_inspector=True)
    app = Application("dev-ui", notch0, notch1, open_inspector=True)
    app.set_stylesheet_from_file(get_relative_path("./main.css"))
    css_files = []
    css_files.extend(list_all_files("./styles/"))
    css_files.append("./main.css")
    css_watcher = []

    for file in css_files:
        css_watcher.append(monitor_file(get_relative_path(file)))
        css_watcher[-1].connect("changed", lambda *_: app.set_stylesheet_from_file(get_relative_path("./main.css")))
    app.run()
