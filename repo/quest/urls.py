from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from app.views import RegistrationRedirectView
from app.forms import CustomUserForm
from app.views import quest
from app.views import profile

urlpatterns = [
    url(r'^hackathon/admin/', admin.site.urls),
    url(r'^hackathon/accounts/register/$', RegistrationRedirectView.as_view(
        form_class=CustomUserForm,),
        name='registration_register',
       ),
    url(r'^hackathon/accounts/', include('registration.backends.simple.urls')),
    url(r'^hackathon/$', quest, name="root"),
    url(r'^hackathon/accounts/profile/', profile),
]

handler404 = 'app.views.page_404'
