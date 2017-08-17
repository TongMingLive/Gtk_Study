from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,title = "我是标题")
        self.box = Gtk.Box(spacing = 10)#控件间的间距
        self.add(self.box)

        self.bacon_button = Gtk.Button(label = "Bacon")
        self.bacon_button.connect("clicked",self.bacon_clicked)
        self.box.pack_start(self.bacon_button,True,True,0)

        self.tuna_button = Gtk.Button(label="Tuna")
        self.tuna_button.connect("clicked", self.tuna_clicked)
        self.box.pack_start(self.tuna_button, True, True, 0)

    def bacon_clicked(self,widget):
        print("你点击了Bacon!")

    def tuna_clicked(self,widget):
        print("你点击了Tuna")


window = MainWindow()
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()