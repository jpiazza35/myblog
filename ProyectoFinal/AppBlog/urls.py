from django.urls import path 
from AppBlog import views



urlpatterns = [
    path('', views.post, name='Post'),
    path('showPost/<id>',views.showPost, name="ShowPost"),
    path('about/', views.About, name="About"),
    path("comment/<id>", views.comment, name="Comment"),
    path("newPost/", views.newPost, name="newPost")

    
]
