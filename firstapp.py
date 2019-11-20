#!/usr/bin/#!/usr/bin/env python3


import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class LinkButtonWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Useful Site Information")
        self.set_border_width(10)


        button = Gtk.LinkButton("https://getfedora.org/", "Click Here for Fedora")
        self.add(button)


win = LinkButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
