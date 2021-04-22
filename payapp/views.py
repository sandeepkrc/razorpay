from django.shortcuts import render
import razorpay
from .models import Coffe



def home(request):
    if request.method =="POST":
        name= request.POST.get('name')
        amount = (int(request.POST.get('amount')))*100
        client = razorpay.Client(auth =("rzp_test_vlGsp0HDBUKKtx","XOLUpywOTVP2awpeXPFrD3lI"))
        payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        coffe = Coffe(name=name,amount=amount,payment_id=payment['id'],)
        coffe.save()
        print("saved the data in admin")
        print(coffe)
        print(payment)
        print(name)
        print(amount)
        return render(request,"index.html",{'payment' : payment})  
    return render(request,"index.html")
def success(request):
    if request.method =='POST':
        a= request.POST
        print(a)

    return render(request,"success.html")
