from django.views import View
from django.shortcuts import render

from apps.users.models import User


class BaseView(View):
    def get(self, request):
        users = User.objects.all()
        user = request.user
        context = {users: 'users', user: 'user'}
        return render(request, 'base.html', context)


class HomePageView(View):
    def get(self, request):
        users = User.objects.all()
        user = request.user
        context = {users: 'users', user: 'user'}
        return render(request, 'home.html', context)


