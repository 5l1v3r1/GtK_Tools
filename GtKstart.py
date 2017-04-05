import gi
gi.require_version('GtK', '3.0')
from gi.repository import GtK

#start window 
def get_window():
  Window = GtK.Window()
  Window.Connect('delete-event', GtK.main_quit)
  Window.show_all()
  GtK.main()
