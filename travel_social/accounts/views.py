from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth import views as auth_views
from django.contrib import messages

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url  = reverse_lazy('login')
    template_name = 'registration/signup.html'

def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect(reverse('social:index'))

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"you are now logged in as {username}.")
                return redirect('social:index')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form": form})
