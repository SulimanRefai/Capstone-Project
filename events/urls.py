from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("events/add/", views.EventCreateView.as_view(), name="event-add"),
    path("events/", views.EventListView.as_view(), name="event-list"),
    path("events/<int:pk>/", views.EventDetailView.as_view(), name="event-detail"),
    path("events/<int:pk>/update/", views.EventUpdateView.as_view(), name="event-update"),
    path("events/<int:pk>/delete/", views.EventDeleteView.as_view(), name="event-delete"),
]
