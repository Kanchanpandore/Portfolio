from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/index.html')

# def base(request):
#     return render(request, 'portfolio/base.html')
def About(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def skills(request):
    return render(request, 'portfolio/skills.html')

def project(request):
    return render(request, 'portfolio/project.html')


