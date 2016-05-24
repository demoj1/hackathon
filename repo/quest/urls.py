from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

from app.views import RegistrationRedirectView
from app.forms import CustomUserForm
from app.views import quest
from app.views import profile
from app.views import report_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$', RegistrationRedirectView.as_view(
        form_class=CustomUserForm,),
        name='registration_register',
       ),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', quest, name="root"),
    url(r'^accounts/profile/', profile, name="profile"),
    url(r'^report/$', report_view, name="report"),
]

handler404 = 'app.views.page_404'
