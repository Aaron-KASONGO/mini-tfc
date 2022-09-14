from datetime import datetime
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .analyse.read_search import ReaderSearch
from .models import Document
from .forms import SignUpForm

# Create your views here.
@login_required
def home(request):
    if request.method == 'POST':
        file = request.FILES['file']
        print(file)
        rd = ReaderSearch(file)
        rd.readPDF()
        # Document.objects.create(create_date=datetime.now(), link=file)
        return JsonResponse({'valid' : rd.links})
    else:
        return render(request, 'mini_tfc/add.html')

def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})