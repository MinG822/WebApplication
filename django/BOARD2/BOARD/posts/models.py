from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # on_delete 는 소속된 글이 사라졌을 때 Comment의 자료들은 어떻게 될 것인지? 좋은 관례는 같이 지워지는 것 
    # models.OneToOne()
    # models.ManyToMany()
    