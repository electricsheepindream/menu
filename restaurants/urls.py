from django.conf.urls import url
from .views import ResLisView, EastResLisView, WestResLisView, SearchListView, ResDetailView, ResCreateView

urlpatterns = [
    url(r'^listview/$',     ResLisView.as_view()),

    url(r'^westlistview/$', WestResLisView.as_view()),

    url(r'^eastlistview/$', EastResLisView.as_view()),

    url(r'^searchlistview/type=(?P<slug>[-\w]+)/$', SearchListView.as_view()),

    url(r'^detailview/detail=(?P<mark>[-\w]+)/$', ResDetailView.as_view(), name='detail'),

    url(r'^create/$', ResCreateView.as_view()),

]