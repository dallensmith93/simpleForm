from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SimpleForm

def home_view(request):
    return HttpResponse("Welcome to the home page!")

def contact_view(request):
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            # Process form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Redirect to success page
            return redirect('success')
    else:
        form = SimpleForm()  

    return render(request, 'contact.html', {'form': form})



def success_view(request):
    return render(request, 'success.html')
