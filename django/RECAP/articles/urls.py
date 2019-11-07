from . import views
from django.urls import path

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('<int:article_pk>/delete/', views.delete, name="delete"),
    path('<int:article_pk>/update/', views.update, name="update"),
    path('<int:article_pk>/comments/', views.comment_create, name="comment_create"),
    path('<int:article_pk>/comments_delete/<int:comment_pk>/', views.comment_delete, name="comment_delete"),
    path('send_cooke/', views.send_cookie, name="send")
]