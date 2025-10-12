from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event, Calendar

class HomeView(TemplateView):
    template_name = "home.html"

class AboutView(TemplateView):
    template_name = "about.html"

class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("dashboard")

class UserLogoutView(LogoutView):
    template_name = "accounts/logout.html"
    next_page = "home"

class SignUpView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "accounts/signup.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
        return render(request, "accounts/signup.html", {"form": form})

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "events/dashboard.html"

class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "events/event_list.html"

    def get_queryset(self):
        return Event.objects.filter(calendar__owner=self.request.user)

class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = "events/event_detail.html"

class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ["title", "description", "start_time", "end_time"]
    template_name = "events/event_form.html"
    success_url = reverse_lazy("event-list")

    def form_valid(self, form):
        calendar, _ = Calendar.objects.get_or_create(owner=self.request.user, name="My Calendar")
        form.instance.calendar = calendar
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ["title", "description", "start_time", "end_time"]
    template_name = "events/event_form.html"
    success_url = reverse_lazy("event-list")

class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = "events/event_detail.html"
    success_url = reverse_lazy("event-list")
