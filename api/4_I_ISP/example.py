from abc import ABC, abstractmethod


# Initial Document unsegregated interface
class Document(ABC):

  @abstractmethod
  def load(self): pass

  @abstractmethod
  def view(self): pass
  
  @abstractmethod
  def format(self): pass
  
  @abstractmethod
  def calculate(self): pass


class PDF(Document):
  def load(self):
    print('load in pdf')

  def view(self):
    print('view informations')

  # Forced to implement format and calculate which do not apply to a pdf context


class PDFDocument(ABC):

  @abstractmethod
  def load(self): pass

  @abstractmethod
  def view(self): pass


class TXTDocument(ABC):
  @abstractmethod
  def load(self): pass

  @abstractmethod
  def format(self): pass

class ExcelDocument(ABC):
  @abstractmethod
  def load(self): pass

  @abstractmethod
  def calculate(self): pass