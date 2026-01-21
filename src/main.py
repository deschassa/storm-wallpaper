from src.engine.generator import StrikeGenerator
from src.models.strike import LightningStrike
from src.ui.window import StormWindow
import sys
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
from gi.repository import GLib


class StormApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='org.storm.monitor',flags=0)
        self.engine = StrikeGenerator()
        self.stream = self.engine.stream()

    def do_activate(self):
        win = StormWindow(self)
        win.present()
        GLib.timeout_add(500, self.on_tick)


    def on_tick(self):
        strike = next(self.stream)
        print(strike)
        return True
    
if __name__ == "__main__":
    app = StormApp()
    app.exit_status = app.run(sys.argv)