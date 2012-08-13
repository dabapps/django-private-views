from django.conf.urls import url, patterns
from testproject import views
from privateviews.decorators import login_not_required


urlpatterns = patterns('',
    url(r'^undecorated/$', views.undecorated),
    url(r'^decorated/$', login_not_required(views.undecorated)),
)
