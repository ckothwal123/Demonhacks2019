from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.forms import modelform_factory
from .models import Resources, Dest, Result
from .utilities import calculate_cost

# Create your views here.
def index(request):
    all_entries = Result.objects.all()
    result_list = []

    for i in all_entries:
        new_dict = {
            "source": i.source_restaurant,
            "destination": i.destination_shelter,
            "quantity" : i.quantity_delivered
        }
        result_list.append(new_dict)

    return render(request,'foodhacks/dashboard.html',{'result_list': result_list})
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
            reqTray = [{
                    'name': form.cleaned_data['rec_source'].name,
                    'feeds': form.cleaned_data['quantity'],
                    'location': (form.cleaned_data['rec_source'].latitude, form.cleaned_data['rec_source'].longitude)
                    },]

            shelters = []
            
            shelter_list = Dest.objects.all()
            for shelter in shelter_list:
                shelter_dict = {"name": shelter.name, "n_people": shelter.requirement, "location": (shelter.latitude, shelter.longitude)}
                shelters.append(shelter_dict)

            # print(reqTray)
            # print(shelters)
            
            reqTray_result, cost_estimate = calculate_cost(reqTray, shelters)
            # print("Result of route=",reqTray_result)
            # print("Cost estimate array",cost_estimate)
            # print(cost_estimate[0]['req']['feeds'])
            # result = Result()
            restaurant_name = cost_estimate[0]['req']['name']
            for i in cost_estimate[0]['shelters']:
                result = Result()
                result.source_restaurant = restaurant_name
                result.destination_shelter = i['name']
                result.quantity_delivered = i['n_people']
                result.save()
                print(i['name'], i['n_people'])
            response = redirect('/')
            return response

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ResourceForm()        

    return render(request, 'foodhacks/restaurant_copy.html', {'form': form})

