from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.authtoken.views import obtain_auth_token

from wurst.api.router import get_router
from wurst.api.views import CliView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(get_router().urls, namespace='v1')),
    url(r'^api/v1/cli/', CliView.as_view()),
    url(r'^api/v1/tokens/', obtain_auth_token),
]
