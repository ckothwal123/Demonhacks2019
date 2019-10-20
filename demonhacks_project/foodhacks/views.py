from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.forms import modelform_factory
from .models import Resources
# Create your views here.
def index(request):

    return render(request,'foodhacks/dashboard.html')
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

def restaurant(request):
    # if this is a POST request we need to process the form data
    ResourceForm = modelform_factory(Resources, fields=("rec_source" ,"quantity", "date_posted" ,"exp_date", "will_handle_delivery", "weight"))
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ResourceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return render(request, 'foodhacks/restaurant_copy.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ResourceForm()        

    return render(request, 'foodhacks/restaurant_copy.html', {'form': form})