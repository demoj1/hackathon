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


class RegistrationRedirectView(RegistrationView):
    def get_success_url(self, user):
        return reverse("app:root")


def quest(request):
    return render(request, "root.html")


def page_404(request):
    return render(request, "404.html")


@login_required
def report_view(request):
    user_instance = request.user

    if request.method == "POST":
        report = user_instance.report_set.first()
        form = ReportForm(request.POST, instance=report)

        if form.is_valid():
            report = form.save(commit=False)
            report.user = user_instance
            report.save()
    else:
        form = ReportForm(instance=user_instance.report_set.first())

    return render(request, "report.html", {"form": form})


@login_required
def profile(request):
    instance = request.user
    if request.method == "POST":
        form = ProfileUserForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
    else:
        form = ProfileUserForm(instance=instance)
        return render(request, "registration/profile.html", {"form": form})

    return render(request, "registration/profile.html", locals())
