from .notificator_interface import NotificatorInterface

class SMSNotificator(NotificatorInterface):
  def send_notification(self, message: str):
    print(f'Sending SMS: {message}')