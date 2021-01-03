from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, View
from django.contrib import messages
from django.urls import reverse
from .models import *
from .forms import *


class all_(View):
    def get(self, *args, **kwargs):
        image = Images.objects.all()
        context = {'image': image}
        return render(self.request, 'all_images.html', context)

def likes(request, pk):
    image = get_object_or_404(Images, pk=pk)
    if image:
        image.likes += 1
        image.save()
        return redirect("images:all")

class nature(View):
    def get(self, *args, **kwargs):
        image = Images.objects.all()
        one = Images.objects.filter(category=1)
        context = {'image': image, 'one': one}
        return render(self.request, 'nature.html', context)

def likes_n(request, pk):
    image = get_object_or_404(Images, pk=pk)
    if image:
        image.likes += 1
        image.save()
        return redirect("images:nature")

class space(View):
    def get(self, *args, **kwargs):
        image = Images.objects.all()
        two = Images.objects.filter(category=2)
        context = {'image': image, 'two': two}
        return render(self.request, 'space.html', context)

def likes_s(request, pk):
    image = get_object_or_404(Images, pk=pk)
    if image:
        image.likes += 1
        image.save()
        return redirect("images:space")

class wildlife(View):
    def get(self, *args, **kwargs):
        image = Images.objects.all()
        three = Images.objects.filter(category=3)
        context = {'image': image, 'three': three}
        return render(self.request, 'wildlife.html', context)

def likes_w(request, pk):
    image = get_object_or_404(Images, pk=pk)
    if image:
        image.likes += 1
        image.save()
        return redirect("images:wildlife")

class popular_sort(View):
    def get(self, *args, **kwargs):
        popular = Images.objects.all().order_by('-likes')
        context = {'popular': popular}
        return render(self.request, 'all_images_pop.html', context)

class newest_sort(View):
    def get(self, *args, **kwargs):
        ordered = Images.objects.all().order_by('-time')
        context = {'ordered': ordered}
        return render(self.request, 'all_images_new.html', context)

def upload(request):
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, 'Successfully Submitted.')
            form.save()
        return redirect('/images/upload')
    context = {'form': form}
    return render(request, 'upload.html', context)

def register(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created. Welcome {username}')
            return redirect('/images/register')
    context = {'form': form}
    return render(request, 'register.html', context)

def login_p(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username Or Password Incorrect')
    context = {}
    return render(request, 'login.html', context)

def logout_p(request):
    logout(request)
    return redirect('/images/login')