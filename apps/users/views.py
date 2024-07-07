from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from rest_framework import viewsets

from apps.users.forms import UserLoginForm, UserRegisterForm, UserUpdateForm
from apps.users.models import User
from apps.users.serializers import UserSerializer


class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        context = {'users': users}
        return render(request, '/', context)


class UserDetailView(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        context = {'user': user}
        return render(request, '/', context)


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {'form': form}
        return render(request, '/', context)

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password.')

        return render(request, '/', {'form': form})


class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        context = {'form': form}
        return render(request, '/', context)

    def post(self, request):
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created.')
            return redirect('/')

        return render(request, '/', {'form': form})


class UserLogoutView(View):
    def get(self, request):
        messages.success(request, 'You are now logged out.')
        logout(request)
        return redirect('/')


class UserUpdateView(View):
    def get(self, request, user_id):
        form = UserUpdateForm()
        context = {'form': form}
        return render(request, '/', context)

    def post(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(pk=request.user.id)
            form = UserUpdateForm(request.POST or None, request.FILES, instance=user)
            if form.is_valid():
                form.save()

                login(request, user)
                messages.success(request, 'Your account has been updated.')
                return redirect('/')
            return render(request, '/', {'form': form})
        else:
            messages.error(request, 'You must be logged in to access this page!')
            return redirect('/')


class UserAPIViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer