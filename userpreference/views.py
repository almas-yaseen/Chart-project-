from django.shortcuts import render
import os 
import json
from django.conf import settings

# Create your views here.

def index(request):
    
    
    
    
    
    if request.method=="GET":
    
            
        currency_data = []
        # Get the directory of the current Python script (views.py in this case)
        script_directory = os.path.dirname(__file__)
        print("script directory",script_directory)
        print("BASE_DIR:", settings.BASE_DIR)
        print("script_directory:", script_directory)
        # Construct the full path to currency.json in the project directory
        file_path = os.path.join(settings.BASE_DIR, 'shop', 'currency.json')

        # Check if the file exists before trying to read from it
        with open(file_path,'r') as json_file:
            data = json.load(json_file)
            
            for k,v in data.items():
                currency_data.append({'name':k,'value':v})
                
            
        return render(request, 'preferences/index.html', {'currency_data': currency_data})
    else:
        currency = request.POST['currency']
        