import gi 
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class StormWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app, title="Storm Wallpaper")
        self.set_default_size(1000, 800)
        self.area = Gtk.DrawingArea()
        self.area.set_draw_func(self.on_draw)
        self.set_child(self.area)
    def on_draw(self, area, context, width, height):
        context.set_source_rgb(0, 0, 0)
        context.paint()
    