class Programmer:
  def make(self):
    print('Programmer creating code')

  
class Seller:
  def make(self):
    print('Seller is selling product')

class HR:
  def make(self):
    print('HR hiring devs')

class Company:
  def do_work(self, worker: any) -> None:
    worker.make()

programmer = Programmer()
seller = Seller()
hr = HR()

company = Company()
company.do_work(programmer)
company.do_work(seller)
company.do_work(hr)



# Initial state
class InitialCompany:
  def do_work(self, worker: int) -> None:
    if worker == 1:
      print('Programmer creating code')
    elif worker == 2:
      print('Seller is selling product')
    elif worker == 3:
      print('HR is hiring devs')
    else:
      print('Error! No worker')
    