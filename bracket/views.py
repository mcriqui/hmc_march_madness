from django.shortcuts import render

# Create your views here.
def get_template(request):
    return render(request, 'home.html')