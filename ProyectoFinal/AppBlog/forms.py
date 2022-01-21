from django import forms
from AppBlog.models import User,Post


class NewPost(forms.Form):
    title = forms.CharField(max_length=200)
    slug = forms.SlugField(max_length=200) ##Esta palabra define la parte final de la URL que identifica una página dentro de un sitio web.
    author = forms.ForeignKey(User)
    content= forms.TextField()
    status = forms.IntegerField(choices=STATUS, default=0)
    image = forms.ImageField()
    created_on = forms.DateTimeField(auto_now_add=True)
    updated_on = forms.DateTimeField(auto_now= True)

class NewComment(forms.Form):
    content = forms.TextField()
    post = forms.ForeignKey(Post)
    user = forms.ForeignKey(User)
    created_on = forms.DateTimeField(auto_now_add=True)