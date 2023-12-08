import random

class Hat:
  contents = []

  def make_a_content(self):
    return []

  def __init__(self, **balls):
    self.contents = self.make_a_content()
    for color, amount in balls.items():
      self.contents.extend([color] * amount)

  def draw(self, balls_amount):
    result = []
    if (balls_amount >= len(self.contents)):
      # The way to really copy, instead of bind
      result = list(self.contents)
      self.contents = []
      result.sort()
      return result

    random_indices = random.sample(range(0, len(self.contents)), balls_amount)
    new_contents = []
    for index, item in enumerate(self.contents):
      if (index in random_indices):
        result.append(item)
      else:
        new_contents.append(item)
    self.contents = new_contents
    result.sort()
    return result
