from django.urls import path

from .views import ArticleListCreateView,ArticleRetriveUpdateDistroyView,ClapArticleView

urlpatterns = [
    path("",ArticleListCreateView.as_view(),name="article-list-create"),
    path("<uuid:id>/",ArticleRetriveUpdateDistroyView.as_view(),name="article-retrive-update-distroy"),
    path("<uuid:article_id>/clap/",ClapArticleView.as_view(),name="clap-article")
]