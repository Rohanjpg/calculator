print("<-----select------>")
print("1.add = +")
print("2.sum = -")
print("3.div = /")
print("4.mul = *")

while True:
    	#select
    user=str(input("select symbol by number",))
        	
    a=float(input("enter number"))
    b=float(input("enter number"))	

    add=("1")
    sum=("2")
    div=("3")
    mul=("4")

			#conditions
    if add==user:        	
   	     print("total",a+b)   	     
   
    elif sum==user:        	
	     	   print("total",a-b)			
    elif div==user:
		       print("total",a/b)		
    elif mul==user:
		       print( "total",a*b)   
		       	        	     
    elif add!=user:
	          print("please select correct Serial numbers of symbol")
	          
       #next calculation
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
          break