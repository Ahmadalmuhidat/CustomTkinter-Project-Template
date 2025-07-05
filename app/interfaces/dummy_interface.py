from abc import ABC, abstractmethod

class Dummy_Interface(ABC):
  def __init__(self):
    self.dummy_attribute = ""

  @abstractmethod
  def dummy_method(self):
    """This method should be implemented by any subclass."""
    pass
