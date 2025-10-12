from django.urls import path
from .views import signup, UserLoginView, UserLogoutView, HomeView, DashboardView, EventCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', signup, name='register'),  
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('add-event/', EventCreateView.as_view(), name='add_event'),
]
