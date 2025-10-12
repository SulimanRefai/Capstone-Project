from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.views import View
from .models import Calendar, Event

# ----------------------------
# Signup view (Function-Based)
# ----------------------------
def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
        else:
            error_message = "Invalid sign up - try again"
    else:
        form = UserCreationForm()

    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)

# ----------------------------
# Login view (Function-Based)
# ----------------------------
class UserLoginView(View):
    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        return render(request, self.template_name, {"error": "Invalid username or password"})

# ----------------------------
# Logout
# ----------------------------
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")

# ----------------------------
# Dashboard (List Events)
# ----------------------------
class DashboardView(LoginRequiredMixin, ListView):
    model = Event
    template_name = "dashboard.html"
    context_object_name = "events"

    def get_queryset(self):
        calendar, _ = Calendar.objects.get_or_create(
            owner=self.request.user,
            defaults={"name": f"{self.request.user.username}'s Calendar"}
        )
        return Event.objects.filter(calendar=calendar).order_by("start_time")

# ----------------------------
# Add Event
# ----------------------------
class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ["title", "description", "start_time", "end_time"]
    template_name = "add_event.html"
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        calendar, _ = Calendar.objects.get_or_create(
            owner=self.request.user,
            defaults={"name": f"{self.request.user.username}'s Calendar"}
        )
        form.instance.calendar = calendar
        return super().form_valid(form)

# ----------------------------
# Home view
# ----------------------------
class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("dashboard")
        return redirect("login")
