from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/comment/', views.comment, name='comment'),
    path('<int:article_pk>/comment_delete/<int:comment_pk>', views.comment_delete, name='comment_delete'),
    # 보충수업
    path('<int:article_pk>/comment2/', views.comment2, name='comment2'),
    path('<int:article_pk>/comment2_delete/<int:comment2_pk>', views.comment2_delete, name='comment2_delete'),
    # cookie
    path('send_cookie/', views.send_cookie, name='send_cookie'),
    # add like
    path('<int:article_pk>/like/', views.like, name='like'),
    path('<int:article_pk>/like2/', views.like2, name='like2'),
    path('explore/', views.explore, name='explore'),
    path('tags/', views.tags, name='tags'),
    path('hashtag/<int:hashtag_pk>', views.Hashtag, name="hashtag")
]