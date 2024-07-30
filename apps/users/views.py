from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
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
        return render(request, 'users/user-list.html', context)


class UserDetailView(View):
    def get(self, request, user_id, *args, **kwargs):
        user = get_object_or_404(User, id=user_id)
        context = {'user': user}
        return render(request, 'users/user-detail.html', context)


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'users/user-login.html', context)

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')

        return render(request, 'users/user-login.html', {'form': form})


class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        context = {'form': form}
        return render(request, 'users/user-register.html', context)

    def post(self, request):
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created.')
            return redirect('users:user-login')

        return render(request, 'users/user-register.html', {'form': form})


class UserLogoutView(View):
    def get(self, request):
        messages.success(request, 'You are now logged out.')
        logout(request)
        return redirect('home')


class UserUpdateView(LoginRequiredMixin, View):
    form_class = UserUpdateForm
    template_name = 'users/user-update.html'

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        user = get_object_or_404(User, id=user_id)
        form = self.form_class(instance=user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        user = get_object_or_404(User, id=user_id)
        form = self.form_class(request.POST, instance=user)
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect('users:user-detail', user_id=user.id)
        return render(request, self.template_name, {'form', form})


class UserAPIViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserUpdateView(View):
#     def get(self, request):
#         form = UserUpdateForm()
#         context = {'form': form}
#         return render(request, 'users/user-update.html', context)
#
#     def post(self, request, user_id, *args, **kwargs):
#         if request.user.is_authenticated:
#             user_id = request.user.id
#             user = get_object_or_404(User, pk=user_id)
#             form = UserUpdateForm(request.POST or None, request.FILES, instance=user)
#             if form.is_valid():
#                 form.save()
#
#                 login(request, user)
#                 messages.success(request, 'Your account has been updated.')
#                 return redirect('users:user-detail')
#             return render(request, 'users/user-update.html', {'form': form})
#         else:
#             messages.error(request, 'You must be logged in to access this page!')
#             return redirect('home')
