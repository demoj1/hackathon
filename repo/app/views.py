from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from registration.backends.simple.views import RegistrationView

# Create your views here.

class RegistrationRedirectView(RegistrationView):
    def get_success_url(self, user):
        return reverse("app:root")

def quest(r):
    return render(r, "root.html")

def page_404(r):
    return render(r, "404.html")

