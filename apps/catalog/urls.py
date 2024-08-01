from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    LogoListView, LogoDetailView, LogoCreateView, LogoUpdateView, LogoDeleteView,
    CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView,
    ContractListView, ContractDetailView, ContractCreateView, ContractUpdateView, ContractDeleteView, LogoViewSet,
    CarViewSet, ContractViewSet, SearchView, FilterView

)

router = DefaultRouter()
router.register(r'logos', LogoViewSet)
router.register(r'cars', CarViewSet)
router.register(r'contracts', ContractViewSet)

app_name = 'catalog'
urlpatterns = [
    # Logo
    path('logos/', LogoListView.as_view(), name='logo-list'),
    path('logos/<int:pk>/', LogoDetailView.as_view(), name='logo-detail'),
    path('logos/create/', LogoCreateView.as_view(), name='logo-create'),
    path('logos/<int:pk>/update/', LogoUpdateView.as_view(), name='logo-update'),
    path('logos/<int:pk>/delete/', LogoDeleteView.as_view(), name='logo-delete'),

    # Car
    path('cars/', CarListView.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('cars/create/', CarCreateView.as_view(), name='car-create'),
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='car-update'),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),
    path('cars/search/', SearchView.as_view(), name='car-search'),
    path('cars/filter/', FilterView.as_view(), name='car-filter'),

    # Contract
    path('contracts/', ContractListView.as_view(), name='contract-list'),
    path('contracts/<int:pk>/', ContractDetailView.as_view(), name='contract-detail'),
    path('contracts/create/', ContractCreateView.as_view(), name='contract-create'),
    path('contracts/<int:pk>/update/', ContractUpdateView.as_view(), name='contract-update'),
    path('contracts/<int:pk>/delete/', ContractDeleteView.as_view(), name='contract-delete'),

]
