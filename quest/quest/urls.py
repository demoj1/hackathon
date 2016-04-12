from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from app.forms import CustomUserForm
from app.views import quest


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$', RegistrationView.as_view(
            form_class=CustomUserForm),
        name='registration_register'
    ),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', quest),
]

handler404 = 'app.views.page_404'