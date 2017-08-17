from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,title = "我是标题")
        self.button = Gtk.Button(label = "click me!")
        self.button.connect("clicked",self.button_clicked)
        self.add(self.button)

    def button_clicked(self,widget):
        print("GameTime")


window = MainWindow()
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()

