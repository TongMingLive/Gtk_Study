from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,title = "我是标题")


window = MainWindow()

label = Gtk.Label()#初始化控件
label.set_label("这里面的字数越多，窗口就会越大哦～～～")#控件内容
label.set_angle(30)#旋转角度
label.set_halign(Gtk.Align.END)#对齐方式
window.add(label)#添加控件至窗口
print(label.get_properties("label"))#可以获取控件中的元素

window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()