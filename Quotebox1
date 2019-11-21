import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Aarrons_Inspirational_Quotes(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Quote Central")

        self.buttonbox = Gtk.ButtonBox(spacing=6)
        self.add(self.buttonbox)

        button1 = Gtk.Button("Inspiration")
        button1.connect("clicked", self.on_info_clicked)
        self.buttonbox.add(button1)

        button2 = Gtk.Button("Motivation")
        button2.connect("clicked", self.on_error_clicked)
        self.buttonbox.add(button2)

        button3 = Gtk.Button("Dark Humor")
        button3.connect("clicked", self.on_warn_clicked)
        self.buttonbox.add(button3)

        button4 = Gtk.Button("Aaron said these")
        button4.connect("clicked", self.on_question_clicked)
        self.buttonbox.add(button4)

    def on_info_clicked(self, widget):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "Your Inspiration For The Day")
        dialog.format_secondary_text("")
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()

    def on_error_clicked(self, widget):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "Time to get motivated")
        dialog.format_secondary_text(
            "And this is the secondary text that explains things.")
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()

    def on_warn_clicked(self, widget):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "Give in to the dark side")
        dialog.format_secondary_text(
            "And this is the secondary text that explains things.")
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()


    def on_question_clicked(self, widget):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "If you hate comptia you've come to the right place")
        dialog.format_secondary_text(
            "And this is the secondary text that explains things.")
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()

Inspiration_quote = "testing"
Motivation_quote = "testing"
Dark_Humor_quote = "testing"
Aarrons_Inspirational_quote = "testing"

win = Aarrons_Inspirational_Quotes()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
