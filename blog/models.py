from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublisedManager(models.Manager):
    def get_queryset(self):
        return super(PublisedManager, self)\
            .get_queryset()\
            .filter(status='published')

class Post(models.Model):
    STAUTS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STAUTS_CHOICE,
                              default='draft')
    objects = models.Manager() #The default manager.
    published = PublisedManager() #Our custom manager

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return  self.title
