from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'appspire/templates/index.html')

def about(request):
	return render(request,'appspire/templates/about.html')

def contact(request):
        return render(request,'appspire/templates/contact.html')
