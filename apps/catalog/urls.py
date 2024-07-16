from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    LogoListView, LogoDetailView, LogoCreateView, LogoUpdateView, LogoDeleteView,
    CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView,
    ContractListView, ContractDetailView, ContractCreateView, ContractUpdateView, ContractDeleteView, LogoViewSet,
    CarViewSet, ContractViewSet,

)
router = DefaultRouter()
router.register(r'logos', LogoViewSet)
router.register(r'cars', CarViewSet)
router.register(r'contracts', ContractViewSet)

urlpatterns = [
#Logo
    path('logos/', LogoListView.as_view(), name='logo_list'),
    path('logos/<int:pk>/', LogoDetailView.as_view(), name='logo_detail'),
    path('logos/create/', LogoCreateView.as_view(), name='logo_create'),
    path('logos/<int:pk>/update/', LogoUpdateView.as_view(), name='logo_update'),
    path('logos/<int:pk>/delete/', LogoDeleteView.as_view(), name='logo_delete'),

#Car
    path('cars/', CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('cars/create/', CarCreateView.as_view(), name='car_create'),
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),

#Contract
    path('contracts/', ContractListView.as_view(), name='contract_list'),
    path('contracts/<int:pk>/', ContractDetailView.as_view(), name='contract_detail'),
    path('contracts/create/', ContractCreateView.as_view(), name='contract_create'),
    path('contracts/<int:pk>/update/', ContractUpdateView.as_view(), name='contract_update'),
    path('contracts/<int:pk>/delete/', ContractDeleteView.as_view(), name='contract_delete'),


]
