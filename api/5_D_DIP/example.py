#  High classes can not depend on low level classes.
# In this example, ClientService, can not directly depend on either email or sms notificator

from .notificator_interface import NotificatorInterface


class ClientService:
  def __init__(self, notificator: NotificatorInterface) -> None:
    self.notificator = notificator
    

  def send(self, message: str) -> None:
    self.notificator.send_notification()