from .notificator_interface import NotificatorInterface


class EmailNotificator(NotificatorInterface):
  def send_notification(self, message: str):
    print(f'Sending email: {message}')