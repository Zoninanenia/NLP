'''
2. สร้างแชทบอทอะไรก็ได้เพื่อทดสอบพื้นฐานความรู้หลังเรียน
'''
import re
print("Hello ! I am Smart Queueing ChatBot")
customer = input("How can I help you ? :")
process = "Inprocess"

while process != "Done":
    if re.match(r"(.*[qQ]ueue.*\s)(?P<store>.*)\b", customer) :
        res = re.match(r"(.*[qQ]ueue.*\s)(?P<store>.*)\b", customer)
        store = res.group('store')
        customer = input(f"Please enter the number of seats you want to make a reservation for {store}. : ")

    
    elif re.match(r"\b\d+", customer) :
        res = re.match(r"(?P<numSeat>\b\d+\b)", customer)
        seat = res.group('numSeat')
        print(f"You have already reserved {seat} seats for {store}.")
        customer = input("Please type 'Check' to view your reservation history. (You can 'unqueue' your reservation at anytime.) : ")
        
    elif re.search(r"\b[cC]heck", customer) :
        print(f"Your Queue for {store} is reserve for {seat} seats, You are now on position 3 in {store} queue.")
        process = "Done"
            
    
    elif re.search(r"\b[Uu]nqueue", customer) :
        res = re.search(r"\b[Uu]nqueue", customer)
        customer = input(f"Type 'yes' to unqueue : ")
        if re.match(r"\b[yY]es", customer) :
            print(f"OK ! You already cancel your queue")
            process = "Done"
        
    else:
        print("I Don't understand what are you trying to say, Please repeat it again.")
        process = "Done"
    
print("Thank you for your attention in Smart Queueing ChatBot ! See you again next Queue. :-)")