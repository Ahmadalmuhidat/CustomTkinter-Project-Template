from app.core.dummy_core_class import Dummy_Core_Class

def dummy_controller():
  # Process data or send request to API
  dummy_core_class = Dummy_Core_Class()

  # Access the attribute (don't call it like a method)
  print(dummy_core_class.dummy_attribute)

  # Optionally call the method
  result = dummy_core_class.dummy_method()
  print(result)

  return True
