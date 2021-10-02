from django.urls import path

from api.views import VisitedLinksAPIView, VisitedDomainsAPIView

urlpatterns = [
    path('visited_links/', VisitedLinksAPIView.as_view(), name='visited_links'),
    path('visited_domains/', VisitedDomainsAPIView.as_view(), name='visited_domains')
]