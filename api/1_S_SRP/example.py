class Process:
  def handle(self, username: str, password: str) -> None:
    if isinstance(username, str) and isinstance(password, str):
      print('Accessing database...')
      print('Verifying user existence...')
      print('User successfully registered!')
    else:
      raise Exception('Invalid Data')