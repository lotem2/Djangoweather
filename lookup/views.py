from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests # module to grab stuff from the internet, not installed by deault. install with pip install requests

	if request.method == "POST":# and request.POST['zipcode'].isdigit():
		zipcode = request.POST['zipcode']
		#Check if given zipcode is valid
		if zipcode.isdigit() == False:
			api = "Zipcode Error..."
			return render(request, 'home.html', {'api': api}) 

		api_requests = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=60796877-C3A9-4D35-8CAB-2321FF5C74AC")
		
		try:
			api = json.loads(api_requests.content)
		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
			category_description = "(0-50):  Air quality is considered satisfactory"
			category_color = "good"
		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51-100):  Air quality is acceptable"
			category_color = "moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups (USG)":
			category_description = "(101-150):  Air quality is considered not acceptable for people i sensitive groups"
			category_color = "usg"
		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151-200):  Everyone may begin to experience health effects"
			category_color = "unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201-300):  Health alert: everyone may exprience more health sensitivity"
			category_color = "veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(301-500):  Health warnings of major emergency conditions"
			category_color = "hazardous"
		
		return render(request, 'home.html', 
			{'api': api, 
			'category_description': category_description,
			'category_color': category_color 
			})

	else:
		api_requests = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=60796877-C3A9-4D35-8CAB-2321FF5C74AC")

		try:
			api = json.loads(api_requests.content)
		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
			category_description = "(0-50):  Air quality is considered satisfactory"
			category_color = "good"
		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51-100):  Air quality is acceptable"
			category_color = "moderate"
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups (USG)":
			category_description = "(101-150):  Air quality is considered not acceptable for people i sensitive groups"
			category_color = "usg"
		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151-200):  Everyone may begin to experience health effects"
			category_color = "unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201-300):  Health alert: everyone may exprience more health sensitivity"
			category_color = "veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(301-500):  Health warnings of major emergency conditions"
			category_color = "hazardous"
		
		return render(request, 'home.html', 
			{'api': api, 
			'category_description': category_description,
			'category_color': category_color 
			})

def about(request):
	return render(request, 'about.html', {})