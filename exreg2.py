import re
print("Hello! Welcome to smart chatbot.")
text = input("Can I help you?: ")
intend = "process"

while intend != "bye":
  if re.match(r"\b(Do you have|I want) ([A-Za-z ]+)\b", text):
    res = re.match(r"\b(Do you have|I want) ([A-Za-z ]+)\b", text)
    product = res.group(2)
    print(f"We have some {product}. Price is 200 baht/piece. [A01, A02, A03]")
    text = input("Please type the product number that you want: ")
  elif re.match(r"\bA(\d+)\b", text): #ไม่มีอะไรนำหน้า ขึ้นด้วยA ต่อด้วยตัวเลขมากกว่า 1 ตัว ไม่มีอะไรต่อท้าย
    res = re.match(r"\b(A\d+)\b", text)
    item = res.group(1)
    print(f"You select {product} number {item}")
    text = input("How many pieces do you want? ")
  elif re.match(r"\b(\d+)\b", text): #ไม่มีอะไรนำหน้า ต่อด้วยตัวเลขมากกว่า 1 ตัว ไม่มีไรต่อท้าย
    res = re.match(r"\b(\d+)\b", text)
    quantity = res.group(1)
    print(f"You select {product} number {item} {quantity} pieces")
    text = input("Do you want anymore?")
  elif re.match(r"\b[n|N]o|[t|T]hank [you]*([A-Za-z ]+)\b", text): #ไม่มีไรนำหน้า พิมไม่noก็thankyou
    intend = "bye"
  else:
    print("Sorry! I don't understand. Please contact to admin")
    intend = "bye"

print("Thank you. See you again next time.")