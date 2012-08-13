from django.conf.urls import url, patterns
from testproject import views
from privateviews.decorators import login_not_required


urlpatterns = patterns('',
    url(r'^undecorated/$', views.undecorated),
    url(r'^test-decorator/$', login_not_required(views.undecorated)),
    url(r'^test-undecorated-class-based-view/$', views.TestClassBasedView.as_view()),
    url(r'^test-decorated-class-based-view/$', login_not_required(views.TestClassBasedView.as_view())),
    url(r'^test-public-views/$', views.test_public_views),
    url(r'^test-public-paths/$', views.test_public_paths),
)
