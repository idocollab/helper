from helper import get_input,log_setup
import logging             # import logging 
log_setup()                # run log_setup() function 

#input as string 
name=get_input("Enter your name :",error="Seems Wrong Name?")
logging.info("Data taken to name...")
if name.isdigit()==True :
    logging.warning("Data entered as name is numbers...")  
  
 #input as any number 
number=get_input("Enter any number(+ve/-ve) : ",data_type=float,error="Seems wrong Number ?")
logging.info("A number taken in number variable...")

 #input as postitive number 
age=get_input("Enter your age : ",data_type=float,error="Seems Wrong Age ?")
logging.info("Age taken...")
print(f"Hey {name},You are {age}yrs old and you gave a number {number}")
logging.info("Printing done...")