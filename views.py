from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person
from django.db import IntegrityError

def home(request):
    error = None
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except IntegrityError:
                error = 'Email already exists.'
    else:
        form = PersonForm()
    people = Person.objects.all().order_by('-id')
    return render(request, 'registrations/home.html', {'form': form, 'people': people, 'error': error})
