from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect

from app.forms import CustomUserForm
from app.forms import ProfileUserForm
from app.forms import ReportForm
from app.models import UserProfile

from registration.backends.simple.views import RegistrationView

# Create your views here.

class RegistrationRedirectView(RegistrationView):
    def get_success_url(self, user):
        return reverse("root")

def quest(request):
    return render(request, "root.html")

def page_404(request):
    return render(request, "404.html")

def report_view(request):
    user_instance = UserProfile.objects.get(pk=request.user.id)

    if request.method == "POST":
        form = ReportForm(request.POST)
        form.user = user_instance

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("root"))
    else:
        form = ReportForm()
        form.user = user_instance

    return render(request, "report.html", {"form": form})

@login_required
def profile(request):
    instance = UserProfile.objects.get(pk=request.user.id)
    if request.method == "POST":
        form = ProfileUserForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
    else:
        form = ProfileUserForm(instance=instance)
        return render(request, "registration/profile.html", {"form": form})

    return render(request, "registration/profile.html", locals())
