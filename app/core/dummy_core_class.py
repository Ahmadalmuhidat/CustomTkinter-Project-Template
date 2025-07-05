from app.interfaces.dummy_interface import Dummy_Interface

class Dummy_Core_Class(Dummy_Interface):
  def __init__(self):
    super().__init__()
    self.dummy_attribute = ""

  def dummy_method(self):
    return "Implemented!"