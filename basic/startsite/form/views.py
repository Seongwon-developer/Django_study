from django.shortcuts import render
from django.http import HttpResponseRedirect

from forms import NameForm

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_date['name']
        return HttpResponseRedirect('/thanks/')

    else:
        form = NameForm()
        return render(request, 'name.html', {'form':form})
            
    
import logging

logger = logging.getLoger('mylogger')

def my_view(request, arg1, arg):
    if bad_mojo:
        logger.error('Something went wrong!')