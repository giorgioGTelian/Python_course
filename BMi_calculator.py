#first we declare what type of imput are we taking:
weight = float(input()) 
height = float(input())

#calculate the bmi:
bmi: float = weight/(height)**2
  

#could be made with switch?

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obesity")

    
#   switch case:

   # match term:
#    case pattern-1:
 #        action-1
  # case pattern-2:
  #    action-2
    #case pattern-3:
     #    action-3
    #case _:
     #   action-default                      
match bmi:
    case bmi < 18.5:
        print("Underweight")
    case bmi >= 18.5:
        print("normal")
        case

      
