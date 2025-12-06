
def log_setup(): 
 """
 This function helps creating a look.log file in current directory and a basic template 
 of log structure.

 """    
 import logging
 logging.basicConfig(filename="look.log",level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")


def get_input(command,data_type=str,error="Wrong Data...",num_check=False):
     """
      This function helps taking input with data type mentioned in parameters with handeling all error
       and allow reinput of data.
     """ 
    
    while True:
     try :
      data=data_type(input(command))
      if num_check==True and data_type!=str:
        if data>=0:
            return data
        else :
            print("Data must be postive number...")  
            continue  
      else:
        return data
     except ValueError:
        print("ValueError...")
     except Exception as e:
        print(e) 

"""       -     < Usage Of get_input()  >-     

roll_number=get_input("Enter your roll number : ",data_type=int,num_check=True)
number=get_input("Enter any number : ",data_type=float)
word=get_input("Enter Your Name :",data_type=str)
print(f"Hey {word},Your Roll Number : {roll_number} and any number : {number}")


         -     < Usage Of log_setup()  >-   

            > import helper
            > helper.log_setup()


"""     

