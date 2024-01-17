from django.shortcuts import render
import os 
import json
from django.conf import settings
from .models import UserPreference
from django.contrib import messages

# Create your views here.

def index(request):    
    currency_data = []
            # Get the directory of the current Python script (views.py in this case)
            # Construct the full path to currency.json in the project directory
    file_path = os.path.join(settings.BASE_DIR, 'shop', 'currency.json')

            # Check if the file exists before trying to read from it
    with open(file_path,'r') as json_file:
                data = json.load(json_file)
                
                for k,v in data.items():
                    currency_data.append({'name':k,'value':v})
                
    exists = UserPreference.objects.filter(user=request.user).exists()
    user_preference =None
    if exists:
       user_preference= UserPreference.objects.get(user=request.user)
    if request.method=="GET":
    
            
        return render(request, 'preferences/index.html', {'currency_data': currency_data})
    else:
        currency = request.POST['currency']
        if exists:
            user_preference.currency = currency
            user_preference.save()
        
        else:
            UserPreference.objects.create(user=request.user,currency=currency)
            messages.success(request,'Changes saved')
        return render(request, 'preferences/index.html', {'currency_data': currency_data,'user_preference':user_preference})
        