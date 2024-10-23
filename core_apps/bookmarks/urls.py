from django.urls import path
from .views import BookmarkCreateView,BookmarkDistroyView

urlpatterns = [
    path("bookmark_article/<uuid:article_id>/",BookmarkCreateView.as_view(),name="bookmark_article"),
    path("remove_bookmark/<uuid:article_id>/",BookmarkDistroyView.as_view(),name="remove_bookmark")
]