#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Main(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.vbox = Gtk.VBox()
        self.set_default_size(300, 300)
        self.add(self.vbox)


        self.button1 = Gtk.Button(label="Click Here")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.vbox.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Goodbye")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.vbox.pack_start(self.button2, True, True, 0)

        self.button3 = Gtk.Button(label="This is my GitHub Address...")
        self.button3.connect("clicked", self.on_button3_clicked)
        self.vbox.pack_start(self.button3, True, True, 0)

        self.button4 = Gtk.Button(label="How to get fedora")
        self.button4.connect("clicked", self.on_button4_clicked)
        self.vbox.pack_start(self.button4, True, True, 0)


    def on_button1_clicked(self, widget):
        print("Hello World")
        print("This is my first GUI app!")

    def on_button2_clicked(self, widget):
        print("I can't believe you did that!")

    def on_button3_clicked(self, widget):
        print("https://github.com/johnhession/mycode")

    def on_button4_clicked(self, widget):
        print("https://getfedora.org/")


win = Main()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
