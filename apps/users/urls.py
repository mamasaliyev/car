from django.urls import path
from .views import UserListView, UserUpdateView, UserLogoutView, UserDetailView, UserRegisterView, UserLoginView

app_name = 'users'
urlpatterns = [
    path('', UserListView.as_view(), name="user-list"),
    path('user-detail/<int:user_id>', UserDetailView.as_view(), name="user-detail"),
    path('user-register', UserRegisterView.as_view(), name="user-register"),
    path('user-login', UserLoginView.as_view(), name="user-login"),
    path('user-logout', UserLogoutView.as_view(), name="user-logout"),
    path('user-update/<int:user_id>', UserUpdateView.as_view(), name="user-update"),
]
