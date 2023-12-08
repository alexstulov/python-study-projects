import copy

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  local_hat = copy.copy(hat)
  success_times = 0
  i = 0
  while i < num_experiments:
    local_hat = copy.copy(hat)
    is_experiment_successful = True
    drawn_balls_list = local_hat.draw(num_balls_drawn)
    drawn_balls = {}
    for ball in drawn_balls_list:
      drawn_balls[ball] = drawn_balls.get(ball, 0) + 1
    for ball, amount in expected_balls.items():
      if (drawn_balls.get(ball, 0) < amount):
        is_experiment_successful = False
        break
    if (is_experiment_successful):
      success_times += 1
    i += 1
  return success_times / num_experiments
