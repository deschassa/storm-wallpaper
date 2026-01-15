import gi 
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class StormWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app, title="Storm Wallpaper")
        self.set_default_size(1000, 800)

