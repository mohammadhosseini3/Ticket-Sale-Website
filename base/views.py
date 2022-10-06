from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.

@login_required
def concertListView(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        # print(searchForm.cleaned_data['searchText'])
        data = searchForm.cleaned_data['ConcertName']
        concerts = concertModel.objects.filter(name__contains=data)
    else:
        concerts = concertModel.objects.all()
    context={
        'searchForm':searchForm,
        'concerts':concerts,
        'concerts_count':concerts.count()
    }
    return render(request,'base/concertList.html',context)

@login_required
def locationListView(request):
    locations = locationModel.objects.all()
    context = {
        'locations':locations,
    }
    return render(request,'base/locationList.html',context)

@login_required
def detailView(request,pk):
    concert = concertModel.objects.get(id=pk)
    context = {
        'concert':concert
    }
    return render(request,'base/detail.html',context)

@login_required
def timeListView(request):
    # request is included the user 
    '''
    for authenticating we should check two elements
    1- user.is_authenticated
    2- user.is_active
    '''
    # if request.user.is_authenticated and request.user.is_active:
    times = timeModel.objects.all()
    context = {
        'times':times
    }
    return render(request,'base/timeList.html',context)

@login_required
def concertEditing(request,pk):
    concert = concertModel.objects.get(id=pk)
    if request.method == 'POST':
        concertForm = ConcertForm(request.POST,request.FILES,instance=concert)
        if concertForm.is_valid():
            concertForm.save()
            return redirect('concert_app:concert_list')
    concertForm = ConcertForm(instance=concert)
    context = {
        'concertForm':concertForm,
        'posterImage':concert.poster
    }
    return render(request,'base/concertEditing.html',context)
        