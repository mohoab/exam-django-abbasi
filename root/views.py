from django.shortcuts import render

def home(request):
    return render(request,'root/index.html')
def about(request):
    return render(request,'root/about.html')
def services(request):
    return render(request,'root/services.html')
def contact(request):
    return render(request,'root/contact.html')





