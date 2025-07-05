import sys
import os
import customtkinter

from CTkMessagebox import CTkMessagebox
from app.controller.dummy_controller import dummy_controller

class Second_Page:
  def __init__(self):
    try:
      super().__init__()

      title = "Welcome"
      message = "second page has been created"
      icon = "check"
      CTkMessagebox(
        title=title,
        message=message,
        icon=icon
      )

      self.table_widgets = []  # For cleanup
      # Dummy data
      self.dummy_data = [
        ["1", "Course A", "3", "Unit A"],
        ["2", "Course B", "4", "Unit B"],
        ["3", "Course C", "2", "Unit C"]
      ]
      self.headers = ["ID", "Title", "Credits", "Unit", "Action"]

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def display_dummy_table(self):
    try:
      # Clear previous widgets
      for widget in self.table_widgets:
        widget.destroy()
      self.table_widgets.clear()

      # Display headers
      for col, header in enumerate(self.headers):
        label = customtkinter.CTkLabel(
          self.courses_table_frame,
          text=header,
          font=("Arial", 12, "bold")
        )
        label.grid(
          row=0,
          column=col,
          padx=10,
          pady=5,
          sticky="nsew"
        )
        self.table_widgets.append(label)

      # Display rows
      for row_idx, row_data in enumerate(self.dummy_data, start=1):
        for col_idx, value in enumerate(row_data):
          label = customtkinter.CTkLabel(
            self.courses_table_frame,
            text=value,
            padx=10,
            pady=5
          )
          label.grid(
            row=row_idx,
            column=col_idx,
            sticky="nsew"
          )
          self.table_widgets.append(label)

        # Add Delete button
        delete_button = customtkinter.CTkButton(
          self.courses_table_frame,
          text="Delete",
          fg_color="red",
          command=lambda course_id=row_data[0]: dummy_controller()
        )
        delete_button.grid(
          row=row_idx,
          column=len(row_data),
          padx=10,
          pady=5,
          sticky="nsew"
        )
        self.table_widgets.append(delete_button)

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def lunch_view(self, parent):
    try:
      # Search bar
      search_bar_frame = customtkinter.CTkFrame(
        parent,
        bg_color="transparent"
      )
      search_bar_frame.pack(
        fill="x",
        expand=False
      )

      search_button = customtkinter.CTkButton(
        search_bar_frame,
        text="Search"
      )
      search_button.grid(
        row=0,
        column=0,
        sticky="nsew",
        pady=10,
        padx=5
      )

      self.search_bar = customtkinter.CTkEntry(
        search_bar_frame,
        width=400
      )
      self.search_bar.grid(
        row=0,
        column=1,
        sticky="nsew",
        pady=10
      )

      # Create Course Button
      create_button = customtkinter.CTkButton(
        search_bar_frame,
        text="Create Course",
        command=self.open_create_course_popup
      )
      create_button.grid(
        row=0,
        column=2,
        sticky="nsew",
        pady=10,
        padx=5
      )

      # Table Frame
      self.courses_table_frame = customtkinter.CTkScrollableFrame(parent)
      self.courses_table_frame.pack(
        fill="both",
        expand=True
      )

      for col, header in enumerate(self.headers):
        header_label = customtkinter.CTkLabel(
          self.courses_table_frame,
          text=header,
          padx=10,
          pady=10
        )
        header_label.grid(
          row=0,
          column=col,
          sticky="nsew"
        )

      for col in range(len(self.headers)):
        self.courses_table_frame.columnconfigure(col, weight=1)

      self.display_dummy_table()

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)

  def open_create_course_popup(self):
    try:
      popup = customtkinter.CTkToplevel()
      popup.title("Create Course")
      popup.geometry("400x350")
      popup.grab_set()  # Block interaction with main window

      # Course ID
      id_label = customtkinter.CTkLabel(popup, text="Course ID:")
      id_label.pack(pady=(20, 5))
      id_entry = customtkinter.CTkEntry(popup)
      id_entry.pack(pady=(0, 10))

      # Course Title
      title_label = customtkinter.CTkLabel(popup, text="Title:")
      title_label.pack(pady=(10, 5))
      title_entry = customtkinter.CTkEntry(popup)
      title_entry.pack(pady=(0, 10))

      # Credits
      credit_label = customtkinter.CTkLabel(popup, text="Credits:")
      credit_label.pack(pady=(10, 5))
      credit_entry = customtkinter.CTkEntry(popup)
      credit_entry.pack(pady=(0, 10))

      def submit():
        print("Course Created:")
        print("ID:", id_entry.get())
        print("Title:", title_entry.get())
        print("Credits:", credit_entry.get())
        CTkMessagebox(title="Success", message="Course created!", icon="check")

      submit_button = customtkinter.CTkButton(popup, text="Submit", command=submit)
      submit_button.pack(pady=20)

    except Exception as e:
      ExceptionType, ExceptionObject, ExceptionTraceBack = sys.exc_info()
      FileName = os.path.split(ExceptionTraceBack.tb_frame.f_code.co_filename)[1]
      print(ExceptionType, FileName, ExceptionTraceBack.tb_lineno)
      print(ExceptionObject)