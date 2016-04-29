from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from app.forms import CustomUserForm
from app.models import UserProfile

from registration.backends.simple.views import RegistrationView

# Create your views here.

class RegistrationRedirectView(RegistrationView):
    def get_success_url(self, user):
        return reverse("app:root")

def quest(r):
    return render(r, "root.html")

def page_404(r):
    return render(r, "404.html")

@login_required
def profile(r):
    instance = get_object_or_404(UserProfile, id=r.user.id)
    form = CustomUserForm(instance=instance)
    return render_to_response(r, "registration/profile.html", {"form": form})
