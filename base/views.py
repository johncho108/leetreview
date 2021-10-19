from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Entry, Feedback
from .forms import EntryForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login_page(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('feed')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('feed')
            else:
                messages.error(request, 'Password is incorrect. Please try again.')
        except:
            messages.error(request, 'User does not exist. Please try again or register below.')

        

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logout_user(request):
    logout(request)
    return redirect('feed')

def register_page(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('feed')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'base/login_register.html', context)

def feed(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    entries = Entry.objects.filter(
        Q(source__icontains=q) |
        Q(title__icontains=q) |
        Q(topic__icontains=q)
        )
    entries_count = entries.count()
    sources = Entry.SOURCE_CHOICES
    topics = Entry.TOPIC_CHOICES
    
    context = {'entries': entries,'entries_count': entries_count, 'sources': sources, 'topics': topics}
    return render(request, 'base/feed.html', context)

@login_required(login_url = '/login')
def my_entries(request):
    user_id = request.user.id
    entries = Entry.objects.filter(user=user_id)
    context = {'entries': entries}
    return render(request, 'base/my_entries.html', context)

def entry(request, pk):
    entry = Entry.objects.get(id=pk)
    feedbacks = entry.feedback_set.all().order_by('-updated')

    if request.method == 'POST':
        feedback = Feedback.objects.create(
            user=request.user,
            entry=entry,
            body=request.POST.get('body')
        )
        return redirect('entry', pk=entry.id)

    context = {'entry': entry, 'feedbacks': feedbacks}
    return render(request, 'base/entry.html', context)

@login_required(login_url = '/login')
def new_entry(request):
    form = EntryForm()
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('my-entries')

    context = {'form': form}
    return render(request, 'base/new_entry.html', context)

@login_required(login_url = '/login')
def edit_entry(request, pk):
    entry = Entry.objects.get(id=pk)
    form = EntryForm(instance=entry)

    if request.user != entry.user:
        return HttpResponse('You are not allowed here!')

    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('my-entries')

    context = {'form': form}
    return render(request, 'base/new_entry.html', context)

@login_required(login_url = '/login')
def delete_entry(request, pk):
    entry = Entry.objects.get(id=pk)

    if request.user != entry.user:
        return HttpResponse('You are not allowed here!')

    if request.method == 'POST':
        entry.delete()
        return redirect('my-entries')
    return render(request, 'base/delete.html', {'obj':entry})

@login_required(login_url = '/login')
def delete_feedback(request, pk):
    feedback = Feedback.objects.get(id=pk)

    if request.user != feedback.user:
        return HttpResponse('You are not allowed here!')

    if request.method == 'POST':
        feedback.delete()
        return redirect('feed')
    return render(request, 'base/delete.html', {'obj':feedback})
