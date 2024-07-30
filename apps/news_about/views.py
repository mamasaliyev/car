from django.shortcuts import render
from django.views import View
from rest_framework import viewsets

from .models import News, About
from .serializers import NewsSerializer, AboutSerializer


class NewsAPIViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class AboutAPIViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class NewsList(View):
    def get(self, request):
        news = News.objects.all()
        context = {news: 'news'}
        return render(request, 'news_about/', context)
