#!/usr/bin/env python3
import gi
import random
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Aarrons_Inspirational_Quotes(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Quote Central")

        grid = Gtk.Grid()
        self.add(grid)

        button1 = Gtk.Button.new_with_label(label="Inspiration")
        button1.connect("clicked", self.on_info_clicked)


        button2 = Gtk.Button.new_with_label(label="Motivation")
        button2.connect("clicked", self.on_error_clicked)


        button3 = Gtk.Button.new_with_label(label="Dark Humor")
        button3.connect("clicked", self.on_warn_clicked)


        button4 = Gtk.Button.new_with_label(label="Aaron said these")
        button4.connect("clicked", self.on_question_clicked)

        grid.attach(button1, 0, 0, 1, 1)
        grid.attach(button2, 1, 0, 1, 1)
        grid.attach(button3, 0, 1, 1, 1)
        grid.attach(button4, 1, 1, 1, 1)

        self.show_all()


    def on_info_clicked(self, widget):
        dialog = Gtk.MessageDialog(self, 1, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "Your Inspiration For The Day")
        keymatch_value = "IN"
        quote_file = open("quotes.txt", "r")
        lines = quote_file.readlines()
        key_match = [s for s in lines if keymatch_value in s]
        quote = random.choice(key_match)
        dialog.format_secondary_text(quote)
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()

    def on_error_clicked(self, widget):
        dialog = Gtk.MessageDialog(self, 1, Gtk.MessageType.INFO,
            Gtk.ButtonsType(1), "Time to get motivated")
        keymatch_value = "MO"
        quote_file = open("quotes.txt", "r")
        lines = quote_file.readlines()
        key_match = [s for s in lines if keymatch_value in s]
        quote = random.choice(key_match)
        dialog.format_secondary_text(quote)
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()

    def on_warn_clicked(self, widget):
        dialog = Gtk.MessageDialog(self, 1, Gtk.MessageType.INFO,
            Gtk.ButtonsType(1), "Give in to the dark side")
        keymatch_value = "HU"
        quote_file = open("quotes.txt", "r")
        lines = quote_file.readlines()
        key_match = [s for s in lines if keymatch_value in s]
        quote = random.choice(key_match)
        dialog.format_secondary_text(quote)
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()


    def on_question_clicked(self, widget):
        dialog = Gtk.MessageDialog(self, 1, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "If you hate comptia you've come to the right place")
        keymatch_value = "AA"
        quote_file = open("quotes.txt", "r")
        lines = quote_file.readlines()
        key_match = [s for s in lines if keymatch_value in s]
        quote = random.choice(key_match)
        dialog.format_secondary_text(quote)
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()



win = Aarrons_Inspirational_Quotes()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
