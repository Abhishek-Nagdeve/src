from django.urls import path

from .views import ArticleListCreateView,ArticleRetriveUpdateDistroyView

urlpatterns = [
    path("",ArticleListCreateView.as_view(),name="article-list-create"),
    path("<uuid:id>/",ArticleRetriveUpdateDistroyView.as_view(),name="article-retrive-update-distroy")
]