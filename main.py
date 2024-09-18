import os
import sys
import customtkinter

import pages.Home.Home as Home

class Main():
  def __init__(self):
    try:
      super().__init__()

      self.CurrentPage = None
      self.pages = {}

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def Navbar(self, window):
    try:
      navbar = customtkinter.CTkFrame(window)
      navbar.pack(fill=customtkinter.X)

      StudentsButton = customtkinter.CTkButton(
        navbar,
        corner_radius = 0,
        command = lambda: self.showPage("Home"),
        text = "Home"
      )
      StudentsButton.pack(side=customtkinter.LEFT)

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def showPage(self, name):
    try:
      if self.CurrentPage:
        self.CurrentPage.pack_forget()

      self.CurrentPage = self.pages[name]
      self.CurrentPage.pack(
        fill = customtkinter.BOTH,
        expand = True
      )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def createPage(self, window, name):
    try:
      page = customtkinter.CTkFrame(window)
      self.pages[name] = page

      if name == "Home":
        Home.Home().create(page)

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def startTheProgram(self):
    try:
      customtkinter.set_appearance_mode("dark")

      self.window = customtkinter.CTk()

      width= self.window.winfo_screenwidth()
      height= self.window.winfo_screenheight()
      self.window.geometry("%dx%d" % (width, height))

      self.window.title("CustomTkinter Template")

      self.Navbar(self.window)

      self.createPage(self.window, "Home")

      self.showPage("Home")

      self.window.mainloop()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
    except KeyboardInterrupt:
      pass

if __name__ == "__main__":
  Main().startTheProgram()
