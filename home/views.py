from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅Your message has been sent!')
        else:
            messages.error(request, 'Please fill in the form corrently!.')
           
    else:
        form = ContactForm()
    
    #todo add contact form
    return render(request, 'contact.html', {'form':form})
