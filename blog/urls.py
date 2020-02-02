from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name="home"),
    path('<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('tags/<str:name>/', views.tag_search, name="tag_search")
]
