class cms:
  def __init__(self):
    self.complaint_list = []
  def show(self):
    if not self.complaint_list:
      print("No complaints registered.")
    else:
      for complaint in self.complaint_list:
        print(f"Title: {complaint[0]}")
        print(f"\nDescription: {complaint[1]}")
        print("---------------------------------------------------------------------------")
        print("\nsome works are pending")
        print("\nwe will solve the problem quickly,thankyou for spend your valuable time")
  def accept_complaint(self,complaint):
    if not  self.complaint_list:
      self.complaint_list.append(complaint)
      print('your complaint was success fully registered,we will solve the problem quickly')
      return True
    else:
      print("This complaint is not availabe,try again ")
      return False

class customer:
  def __init__(self):
    self.complaintList = []
  def my_complaints(self,complaint):
    self.complaintList.append(complaint)
  def show(self):
    if not self.complaintList:
      print("No complaints raised.")
    else:
      for complaint in self.complaintList:
        print(f"Title: {complaint[0]}")
        print(f"\nDescription: {complaint[1]}")
        print("\nyour complaints")
  def register_complaint(self):
    print('Enter the complaint ')
    self.title = input("enter the title:-")
    self.description=input("enter the description:-")
    return self.title,self.description


CMS=cms()
customer_name=customer()


while True:
  print('-----------------------------------------------------------------------------')
  print("select the option below ")
  print("1 - register the complaint\n2 - complaint status \n3 - customer complaint list \n0 - exit")
  option = int(input())
  if option == 1:
    requested_complaint = customer_name.register_complaint()
    status = CMS.accept_complaint(requested_complaint)
    if status == True:
      customer_name.my_complaints(requested_complaint)
  elif option == 2:
    CMS.show()
  elif option == 3:
    customer_name.show()
  elif option == 0:
    break
