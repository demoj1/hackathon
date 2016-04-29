from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from app.forms import CustomUserForm
from app.forms import ProfileUserForm
from app.models import UserProfile

from registration.backends.simple.views import RegistrationView

# Create your views here.

class RegistrationRedirectView(RegistrationView):
    def get_success_url(self, user):
        return reverse("app:root")

def quest(request):
    return render(request, "root.html")

def page_404(request):
    return render(request, "404.html")

@login_required
def profile(request):
    instance = UserProfile.objects.get(pk=request.user.id)
    if request.method == "POST":
        form = ProfileUserForm(request.POST, instance=instance)
        if form.is_valid():
            puf = form.save(commit=False)
            puf.user = request.user
            puf.save()
    else:
        form = ProfileUserForm(instance=instance)
        
    return render_to_response("registration/profile.html", {"form": form})
