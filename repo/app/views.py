from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from forms import CustomUserForm
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
    instance = get_object_or_404(CustomUserForm, r.user.id)
    form = CustomUserForm(r.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect("quest")
    return render(r, "root.html")