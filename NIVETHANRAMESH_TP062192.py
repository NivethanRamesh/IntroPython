# NIVETHAN A/L RAMESH
# TP062192



# Defining the user login to store user authentication details.
def user_login():
      print("******** BANKING SERVICE SYSTEM *********")
      print("******** Welcome to Bankrevel **********")
      user_id = input("Please enter your user ID: ")
      user_pass = input("Please enter your password: ")
      with open("userpass.txt","r") as fh:
            founddata = "notfound"
            for dataline in fh:
                  datalist = dataline.strip().split(":")
                  if datalist[0] == user_id and datalist[1] == user_pass:
                        founddata = datalist
                        break
            if founddata == "notfound":
                  print("Login is not successful!!!")
            else:
                  print("Login is successful!!!")
      return founddata
      fh.close()




# Defining the gen_id used for the ID generation.
def gen_id(perm):
      with open("id.txt","r") as fh:
            data = fh.readline()
            datalist = data.strip().split(":")
      if perm == "staff":
            perf = "STF"
            old_id = datalist[0][3:]
      elif perm == "customer":
            perf = "CUS"
            old_id = datalist[1][3:]
      elif perm == "transaction" :
            perf = "TRS"
            old_id = datalist[2][3:]
      next_id = int(old_id) + 1
      if len(str(next_id)) == 1:
          new_id = "0000"+str(next_id)
      elif len(str(next_id)) == 2:
          new_id = "000"+str(next_id)
      elif len(str(next_id)) == 3:
          new_id = "00"+str(next_id)
      elif len(str(next_id)) == 4:
          new_id = "0"+str(next_id)
      elif len(str(next_id)) == 5:
          new_id = str(next_id)
      new_id = perf + new_id
      if perm == "staff":
            datalist[0] = new_id
      elif perm == "customer" :
            datalist[1] = new_id
      elif perm == "transaction" :
            datalist[2] = new_id
      else:
            datalist[3] = new_id
            
      data = ":".join(datalist)
      with open("id.txt","w") as fh:
            fh.write(data)
      return new_id
      fh.close()

            
# Defining the gen_pass used for the password generation.   
def gen_pass(perm):
      with open("pass.txt" , 'r') as fh :
            data = fh.readline()
            datalist = data.strip().split(":")
      if perm == "staff" :
            pref = "STA"
            old_pass = datalist[0][3:]
      elif perm == "customer":
            pref = "COS"
            old_pass = datalist[1][3:]
      next_pass = int(old_pass) + 1
      if len(str(next_pass)) == 1:
          new_pass = "0000"+str(next_pass)
      elif len(str(next_pass)) == 2:
          new_pass = "000"+str(next_pass)
      elif len(str(next_pass)) == 3:
          new_pass = "00"+str(next_pass)
      elif len(str(next_pass)) == 4:
          new_pass = "0"+str(next_pass)
      elif len(str(next_pass)) == 5:
          new_pass = str(next_pass)
      new_pass = pref + new_pass
      if perm == "staff":
            datalist[0] = new_pass
      elif perm == "customer" :
            datalist[1] = new_pass
      else:
            datalist[2] = new_pass
            
      data = ":".join(datalist)
      with open("pass.txt","w") as fh:
            fh.write(data)
      fh.close()
      return new_pass





# Defining addstaff() to add staffs into the system. 
      
def addstaff():
      user_id = gen_id("staff")
      user_pass = gen_pass("staff")
      print("User ID :",user_id)
      print("User Password:",user_pass)
      user_name = input("Please enter your name :")
      print("Your account is created.")
      account_type = "2"
      with open("userpass.txt","a") as fh:
            data = user_id+":"+user_pass+":"+user_name+":"+account_type+"\n"
            fh.write(data)
      fh.close()

   
      
 # Defining addcustomer() to add customer into the system.
def addcustomer(logdetails):
      user_id = gen_id("customer")
      user_pass = gen_pass("customer")
      print("User ID : ",user_id)
      print("User Password: ",user_pass)
      user_name = input("Please enter you name : ")
      account_type = "3"
      contact_num = input("Enter Customer's Contact Number : ")
      account = int(input("Choose 1 for Savings Account or 2 for Current Account : "))
      first_balance = 500
      new_balance = 500
      if account == 1 :
            acc = "Savings account"    
      elif account == 2 :
            acc = "Current account "
      print("Your account is created. Thanks for registering with us.")
      with open("userpass.txt","a") as ufh:
            data = str(user_id)+":"+str(user_pass)+":"+str(user_name)+":"+str(account_type)+":"+str(acc)+"\n"
            ufh.write(data)
      ufh.close()
      with open("customer.txt","a") as sfh:
            data = str(user_id)+":"+str(user_name)+":"+str(user_pass) +":"+str(contact_num)+":"+str(first_balance)+":"+str(new_balance)+":"+str(acc)+"\n"
            sfh.write(data)
      sfh.close()

# To allow staff to change customer details.

def staffchangedetails(logdetails):
      alldata =[]
      with open("customer.txt","r") as fh:
            for data in fh:
                  datalist = data.strip().split(":")
                  alldata.append(datalist)
      print(alldata)
      cus_id=input("Enter Customer ID to change the details: ")
      cus_name = input(" Enter the Customer Name to change the details:  ")
      new_pass = input("Please Enter new Password : ")
      new_contact = input("Please Enter new contact number : ")
      old_balance = input(" Please Enter old balance : ")
      new_balance = input(" Please Enter new balance : ")
      acct_type = input(" Please Enter your account type  : ")
      print(" Details are now changed. Enjoy!")
      ind = -1
      nor = len(alldata)
      for cnt in range(0,nor):
            if cus_id  == alldata[cnt][0]:
                  ind = cnt
                  break
      alldata[ind][2:] = [new_pass,new_contact,old_balance,new_balance,acct_type]
      with open("customer.txt","w") as fh:
            nor = len(alldata)
            for cnt in range(0,nor):
                  data = ":".join(alldata[cnt])+"\n"
                  fh.write(data)
      fh.close()

# Defining displayuser to show interface.
def displayuser():
      with open("userpass.txt","r") as fh:
            print("="*70)
            print("User ID".center(10)+"|"+"User Password".center(14)+"|"+"User Name".center(30)+"|"+"Account Type")
            print("="*70)
            for data in fh:
                  datalist = data.strip().split(":")
                  print(datalist[0].ljust(10)+"|"+ datalist[1].ljust(14)+"|"+ datalist[2].ljust(30)+"|"+datalist[3].center(12))
      print("\n\n\n")
      fh.close()


# Defining changepass to allow user to change password.
def changepass(logdetails):
      alldata = []
      with open("userpass.txt","r") as fh:
            for data in fh:
                  datalist = data.strip().split(":")
                  alldata.append(datalist)
      us_id = input( "Enter your user ID:  ")
      new_pass = input("Please Enter new Password : ")
      print(" Your new password has been set. Enjoy ! ")
      ind = -1
      nor = len(alldata)
      for cnt in range(0,nor):
            if us_id == alldata[cnt][0]:
                  ind = cnt
                  break
      
      alldata[ind][1] = new_pass
      with open("userpass.txt","w") as fh:
            nor = len(alldata)
            for cnt in range(0,nor):
                  data = ":".join(alldata[cnt])+"\n"
                  fh.write(data)
      fh.close()

# To allow customer to do deposit in the system.
def Deposit(logdetails):
      import datetime
      allrec = []
      with open( "customer.txt" , 'r') as fh :
            for data in fh :
                  datalist = data.strip().split(":")
                  allrec.append(datalist)
      ind = -1
      for cnt in range(0,len(allrec)):
            if logdetails[0] == allrec[cnt][0]:
                  ind = cnt
                  break
      if ind != -1:
            currentbal = int(allrec[ind][5])
            transaction_date = datetime.datetime.now()
            new_deposit = int(input("Insert value to deposit : " ))
            currentbal += new_deposit
            allrec[ind][5] = str(currentbal)
      with open("customer.txt","w") as fh:
            for cnt in range(0,len(allrec)):
                  fh.write(":".join(allrec[cnt])+"\n")
      print("Your amount has been deposited.")
      print("Thank you for being with us.")
      print(" Your transaction date is : " , transaction_date)
      transaction_id = gen_id("transaction")            
      
      with open("transaction.txt" , "a") as sfh:
            data = logdetails[0]+":"+transaction_id+":"+str(transaction_date)[0:10] +":"+str(new_deposit)+":"+"1"+"\n"
            sfh.write(data)


# To allow customer to do withdraw in the system.
def Withdraw(logdetails):
      import datetime
      allrec = []
      with open( "customer.txt" , 'r') as fh :
            for data in fh :
                  datalist = data.strip().split(":")
                  allrec.append(datalist)
      ind = -1
      for cnt in range(0,len(allrec)):
            if logdetails[0] == allrec[cnt][0]:
                  ind = cnt
                  break
      if ind != -1:
            trans_amount = (int(input("Insert value to withdraw : " )))
            currentbal = int(allrec[ind][5])
            if allrec[ind][6] == "Savings account":
                  availbal = currentbal - 100
            else:
                  availbal = currentbal - 500
            if availbal >= trans_amount:
                  print("Your amount has been withdraw.")
                  transaction_date = datetime.datetime.now()
                  currentbal -= trans_amount
                  allrec[ind][5] = str(currentbal)
                        
            with open("customer.txt","w") as fh:
                     for cnt in range(0,len(allrec)):
                        fh.write(":".join(allrec[cnt])+"\n")
            transaction_date = datetime.datetime.now()
            print("Thank you for being with us.")
            print("Your transaction date is : " , transaction_date)
            transaction_id = gen_id("transaction")            
            
            with open("transaction.txt" , "a") as sfh:
                     data = logdetails[0]+":"+transaction_id+":"+str(transaction_date)[0:10] +":"+str(trans_amount)+":"+"0"+"\n"
                     sfh.write(data)



# To allow customer or staff to check Customer's statement of Account Report.
def Statementreport(logdetails) :
      import datetime
      print("\n")
      print("=" * 90)
      print("Customer's Statement of Account Report".center(100))
      print("=" * 90)
      print("\n")
      user = input("Enter your user ID :   ")
      start_date = input("Enter the start date :(DD/MM/YYYY)")
      end_date = input("Enter end date : (DD/MM/YYYY) ")
      start_date = datetime.datetime(int(start_date[6:]),int(start_date[3:5]),int(start_date[0:2]))
      end_date = datetime.datetime(int(end_date[6:]),int(end_date[3:5]),int(end_date[0:2]))
      print(start_date)
      print(end_date)
      alldata = []
      with open ("transaction.txt" , "r") as fh :
            for line in fh:
                  alldata.append(line.strip().split(":"))
      ans=input("Press enter to continue")
      print("=" * 80)
      print("User ID".center(10)+"|"+"Transaction ID".center(14)+"|"+"Transaction_date".center(15)+"|"+"Amt_trans".center(15)+"|"+"Trans_type")
      print("=" * 80)
      for cnt in range(0,len(alldata)):
            trandate=alldata[cnt][2]
            trandate= datetime.datetime(int(trandate[0:4]),int(trandate[5:7]),int(trandate[8:]))
            if ( trandate >= start_date and trandate <= end_date) and user == alldata[cnt][0]:
                  print(alldata[cnt][0].ljust(10)+"|"+alldata[cnt][1].center(14)+"|"+alldata[cnt][2].center(16)+"|"+alldata[cnt][3].center(15)+"|"+alldata[cnt][4].rjust(10))
      ans = input("Press Enter to continue...")
      fh.close()


          
# Defining superusermenu to allow options to superuser.
def superusermenu():
      while True:
            print("SUPER USER MENU")
            print("===============")
            print("===============")
            print("\n\t1. Add new admin staff account")
            print("\t2. Display all user accounts")
            print("\t3. Logout from the system")
            ans = input("Please enter your choice :")
            if ans == "1":
                  addstaff()
            elif ans == "2":
                  displayuser()
            elif ans == "3":
                  break
            
      
#Defining adminstaffmenu to allow options to admin staff.
def adminstaffmenu(logdetails):
        while True:
            print("================================")
            print("ADMIN STAFF MENU FOR : ",logdetails[2])
            print("================================")
            print("\n\t1. Register a new customer")
            print("\t2. Display all user accounts")
            print("\t3. Change Password")
            print("\t4. Edit customer details")
            print("\t5. Generate Customer's Statement of Account Report")
            print("\t6. Logout from the system")
            ans = input("Please enter your choice :")
            if ans == "1":
                  addcustomer(logdetails)
            elif ans == "2":
                  displayuser()
            elif ans == "3":
                  changepass(logdetails)
            elif ans == "4":
                  staffchangedetails(logdetails)
            elif ans == "5" :
                  Statementreport(logdetails)
            elif ans == "6" :
                  break
            
#Defining customermenu to allow options to customer. 
def customermenu(logdetails):
      while True:
            print("================================")
            print("CUSTOMER MENU FOR :  ", logdetails[2])
            print("================================")
            print("\n\t1. Change the password ")
            print("\t2. Deposit")
            print("\t3. Withdraw")
            print("\t4. Generate Customer's Statement of Account ")
            print("\t5. Logout from the system")
            ans = input("Please enter your choice :")
            if ans == "1":
                  changepass(logdetails)
            elif ans == "2":
                  Deposit(logdetails)
            elif ans == "3":
                  Withdraw(logdetails)
            elif ans == "4":
                  Statementreport(logdetails)
            elif ans == "5":
                  break






#MAIN LOGIC
# This is the main logic behind the system.
#==========
while True:
      loginstat = user_login()
      if loginstat != "notfound":
            print("Welcome to the System "+loginstat[2])
            if loginstat[3] == "1":
                  superusermenu()
            elif loginstat[3] == "2":
                  adminstaffmenu(loginstat)
            elif loginstat[3] == "3":
                  customermenu(loginstat)
      else:
            print("INVALID LOGIN CREDENTIALS. TRY LOGIN AGAIN!!!!")
      ans = input("Press 'Q' key to quit the system. Press other key to continue.")
      if ans == "Q":
            break



