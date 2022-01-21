from django.contrib.auth.models import User
from django.db import models 


#we created a tuple to determine the status of a blog
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True) ##Esta palabra define la parte final de la URL que identifica una página dentro de un sitio web.
    author = models.ForeignKey(User,on_delete= models.CASCADE)
    content= models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    ## esto va en la vista comments = Comment.objects.filter(post__id = id)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


'''
The Meta class inside the model contains metadata. 
We tell Django to sort results in the created_on field in descending order by default when we query the database.
We specify descending order using the negative prefix. By doing so, posts published recently will appear first.

The __str__() method is the default human-readable representation of the object. Django will use it in many places, such as the administration site.
'''

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    created_on = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    name=models.CharField(max_length=40)