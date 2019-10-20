from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):

    return render(request,'foodhacks/restaurant.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

def getdata(request):
    if request.method == 'POST':
        print(request.POST.get("restaurantName", "No value entered"))
        print(request.POST.get("unitsOfFood","Units of food not specified"))
        #To add the code to save to the database
        return HttpResponse("Hello, User. You have successfully submitted the request.")
    if request.method == 'GET':
        return render(request,'foodhacks/restaurant.html')
    
def shelter(request):

    return render(request,'foodhacks/shelter.html')