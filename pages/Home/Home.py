import sys
import os
import customtkinter

from CTkMessagebox import CTkMessagebox

class Home():
  def __init__(self):
    try:
      super().__init__()

      title = "Welcome"
      message = "Home page has been created"
      icon = "check"
      CTkMessagebox(
        title = title,
        message = message,
        icon = icon
      )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def create(self, parent):
    try:
      SearchBarFrame = customtkinter.CTkFrame(
        parent,
        bg_color = "transparent"
      )
      SearchBarFrame.pack(
        fill = "x",
        expand = False
      )

      SearchButton = customtkinter.CTkButton(
        SearchBarFrame,
        text = "Search"
      )
      SearchButton.grid(
        row = 0,
        column = 0,
        sticky = "nsew",
        pady = 10,
        padx = 5
      )

      self.SearchBar = customtkinter.CTkEntry(
        SearchBarFrame,
        width = 400
      )
      self.SearchBar.grid(
        row = 0,
        column = 1,
        sticky = "nsew",
        pady = 10
      )

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)
