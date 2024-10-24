from django.urls import path
from .views import ResponseListCreateVeiw,ResponseUpdateDeleteView

urlpatterns = [
    path(
        "article/<uuid:article_id>/" , 
        ResponseListCreateVeiw.as_view() , 
        name="article_responses"
        ),
    path(
        "<uuid:id>/" , 
        ResponseUpdateDeleteView.as_view() , 
        name="response_details"
        ),
]