from django.shortcuts import render
from django.http import HttpResponse


def calculator(request):
    return render (request,'calculator/calculator.html')



# Create your views here.
   # def transaction(self):
        # connect with html for the choise of either incriment or withdraw
    #  pass


def incrimention(initial, incriment):
    pass
     #   initial = 0
        #the incriment varies with the type of action performed by the client
        # get the action performed
        #should return the final_amount
        #come back to this


def withdrawal(final_amount,withdraw):
    
        #from db
    final_amount = final_amount
        #from user input
    withdraw = withdraw
    message ="The transaction was not possible"
    if(final_amount == 0):
            #the transaction cannot happen
        print(message)
            
    elif(withdraw > final_amount):
        print(message)
        #come back
        #     
    else:
        print("your transaction will be proccesed")

        final_amount -=withdraw  

    #def on_referal():
     #   pass    

    #def earnings():
        #shows the statistics ofhow the user has been earning for the month
     #   pass                          

    
    #def withdrawals():
        #shows the user on the usage
     #   pass
def usebase():
        #shows how and whether the services incerased the usage
        pass

def references():
        #for the user to know how good he/she is dooing on marketing  
        pass
    # make the view function for the statistics