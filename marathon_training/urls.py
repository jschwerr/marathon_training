"""marathon_training URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import marathon_training.views as views
from django.contrib.auth  import views as auth_views

urlpatterns = [
    # include training tracker app
    url(r'^training_tracker/', include('training_tracker.urls', namespace="training_tracker")),
    # root directory redirects to training tracker
    url(r'^$', views.root),
    # login page
    url(r'^login/$', auth_views.login),
    # logout page
    url(r'^logout/$', auth_views.logout, {'next_page': '../training_tracker/'}),
    # admin site
    url(r'^admin/', admin.site.urls),
]
