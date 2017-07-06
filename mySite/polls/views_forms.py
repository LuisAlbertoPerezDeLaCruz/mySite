from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

myName="@"

def get_name(request):
    # if this is a POST request we need to process the form data"
    global myName
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            
            # Esta es una forma utilizando el request.POST
            # post = request.POST
            # myName=post.get('your_name')
            
            # Esta es la forma que ensena la documentacionde Django
            
            print('form.is_bound: '+ 'true' if form.is_bound else 'false')
            myName=form.cleaned_data['your_name']            
                        
            return HttpResponseRedirect('/polls/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'polls/name.html', {'form': form})

def show_thanks(request):
    global myName
    return render(request, 'polls/name.html', {
            'message': myName+", thanks!",
        })