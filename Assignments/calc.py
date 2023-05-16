
def Add(Numbers):
 result = 0
 for num in Numbers:
  result+= num
 return result 
 
 
def Sub(Numbers):
 result = Numbers[0]
 for num in range(1 , len(Numbers)):
  result-= Numbers[num]
 return result
 
 
def Multi(Numbers):
 result = 1
 for num in Numbers:
  result*= num
 return result 
 
 
def Div(Numbers):
 result = Numbers[0]
 for num in range(1 , len(Numbers)):
  if Numbers[num] == 0:
    print("Cannot divide by zero")
    return None
  result /= Numbers[num]
  return result
  
  
  
  
  
  
#This Is List I will Store Inside It  
Numbers = []  
while(True):
   Num = input("Please Enter Numbers Want To Calculate : (Press F If You Finish Entering Numbers : )")
   if Num == 'F' or Num == 'f':
      break
   #Convert To Float Because The Division   
   Numbers.append(float(Num))  
   
   
while (True):   
    #Choose The Operation
    print("That Is Your Operations In Your Calculator")
    print("   1. Add   -> +")
    print("   2. Sub   -> -")
    print("   3. Multi -> *")
    print("   4. Div   -> /")
    print("   5. Exit  -> E")
              
    operation = input("Enter An Operation : ")
    if operation == '+':
        result = Add(Numbers)
        print("_______________________________________________")
        print(f"       Sum Of Numbers Is : {result}")
        print("_______________________________________________")

       
    elif operation == '-':
        result = Sub(Numbers)
        print("_______________________________________________")
        print(f"Subtraction Of Numbers Is : {result}")
        print("_______________________________________________")

       
    elif operation == '*':
        result = Multi(Numbers)
        print("_______________________________________________")
        print(f"Multiplication Of Numbers Is : {result}")      
        print("_______________________________________________")

      
    elif operation == '/':
        result = Div(Numbers)
        print("_______________________________________________")
        print(f"Division Of Numbers Is : {result}") 
        print("_______________________________________________")

       
    elif operation == 'E' or operation == 'e':
        print("_______________________________________________")
        print("Thanks For Use This App.........")
        print("_______________________________________________")
        break

    else:
        print("!!!!!!!!!!!!!! Error! Invalid operation !!!!!!!!!!!!!!")

    
 

