from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
# instead of doing Post.objects.all or something else we can use now Post.published.filter(title = ....)

class PublishedManger(models.Manager):
    def get_queryset(self):
        return super(PublishedManger,self).get_queryset().filter(status='published')




class Post(models.Model):
    STATUS_CHOICES = (
        ('draft',"Draft"),
        ('published',"Published"),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    objects = models.Manager()
    published = PublishedManger()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
