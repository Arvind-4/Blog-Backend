from django.urls import path

from .views import (
    PostListAPIView,
    SinglePostAPIView,
    TagAPIView,
    TagListView,
)

urlpatterns = [

    # Posts

    path('list-view/', PostListAPIView.as_view()),
    path('<str:slug>/detail-view/', SinglePostAPIView.as_view()),

    # Tags

    path('tags/lists/', TagListView.as_view()),
    path('tags/<str:slug>/', TagAPIView.as_view()),
]