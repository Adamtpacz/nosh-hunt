from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import List, Restaurant, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def lists_index(request):
    # Dont forget to add this in to see specific lists for logged in users
    lists = List.objects.filter(user=request.user)
    return render(request, 'lists/index.html', {'lists': lists})

@login_required
def lists_detail(request, list_id):
    list = List.objects.get(id=list_id)
    return render(request, 'lists/detail.html', {'list': list})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
        # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class ListCreate(LoginRequiredMixin, CreateView):
    model = List
    fields = ['title', 'category', 'city', 'restaurants']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ListUpdate(LoginRequiredMixin, UpdateView):
    model = List
    fields = ['title', 'category', 'city', 'restaurants']

class ListDelete(LoginRequiredMixin, DeleteView):
    model = List
    success_url = '/lists'