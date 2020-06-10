from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import EntryViewSet, CreateEntry, EntryDetailsView, EntryPublicView

router = DefaultRouter()
router.register('entries', EntryViewSet, basename='entries')

custom_urlpatterns = [
    url(r'^create-entry/$', CreateEntry.as_view(), name='create-entry'),
    url(r'^update-entry/(?P<pk>\d+)/$', EntryDetailsView.as_view(), name='update-entry'),
    url(r'^public-entries/$', EntryPublicView.as_view(), name='public-entries')
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns