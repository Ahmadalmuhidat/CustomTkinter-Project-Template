import os
import sys
import customtkinter
import app.views.home as Home
import app.views.second_page as Second_Page

from app.config.configrations import Configrations
from app.config.router import Router

customtkinter.set_appearance_mode("dark")

class Main():
  def __init__(self):
    try:
      self._config = Configrations()
      self._router = Router()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def create_navbar(self):
    try:
      navbar = customtkinter.CTkFrame(self._config.window)
      navbar.pack(fill=customtkinter.X)

      home = customtkinter.CTkButton(
        navbar,
        corner_radius = 0,
        command = lambda: self._router.navigate(Home.Home),
        text = "Home"
      )
      home.pack(side=customtkinter.LEFT)

      second_page = customtkinter.CTkButton(
        navbar,
        corner_radius = 0,
        command = lambda: self._router.navigate(Second_Page.Second_Page),
        text = "Second Page"
      )
      second_page.pack(side=customtkinter.LEFT)

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def start_program(self):
    try:
      self.window = customtkinter.CTk()
      self._config.set_window(self.window)

      width= self.window.winfo_screenwidth()
      height= self.window.winfo_screenheight()
      self.window.geometry("%dx%d" % (width, height))
      self.window.title("CustomTkinter Template")

      self.create_navbar()
      self._router.navigate(Home.Home)

      self.window.mainloop()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
    except KeyboardInterrupt:
      pass

if __name__ == "__main__":
  Main().start_program()
