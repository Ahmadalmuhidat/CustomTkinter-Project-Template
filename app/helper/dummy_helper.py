def format_course_title(course_id, title):
  """Returns a formatted course string."""
  return f"[{course_id}] {title}"

def calculate_total_credits(course_list):
  """
  Takes a list of course dictionaries with 'credits' field and returns the total.
  Example:
    course_list = [{'id': 1, 'title': 'Math', 'credits': 3}]
  """
  return sum(course.get("credits", 0) for course in course_list)

def is_valid_course_id(course_id):
  """Basic dummy validation: must be digits only."""
  return str(course_id).isdigit()
