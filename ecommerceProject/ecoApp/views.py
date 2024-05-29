from django.shortcuts import render

# Create your views here.

# home page
def home(request):
    return render(request, 'ecoApp/home.html')

# contact
def contact(request):
    return render(request, 'ecoApp/contact_us.html')

# aboutus 
def about_us(request):
    return render(request,'ecoApp/about_us.html')

# product
def product(request):
    return render(request,'ecoApp/product.html')
# sign_up 
def sign_up(request):
    return render(request,'ecoApp/sign_up.html')
