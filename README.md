# storm_wallpaper_Silverblue
Real-time lightning strike visualizer for Linux(GTK4/Cairo...) Designed for Fedora Silverblue

> **DISCLAIMER** This project is currently in **ALPHA**. It is a work in progress. Do not use for real meteorological safety


## Installation

This project uses **GTK4** via GObject Introspection. It relies on system-level packages, not just PyPI

### System Dependencies(Debian/Ubuntu)
You must install GTK4 bindings for Python :

```bash
sudo apt-get update
sudo apt-get install -y python3-gi python3-gi-cairo gir1.2-gtk-4.0

### Run the application

/usr/bin/python3 src/main.py

