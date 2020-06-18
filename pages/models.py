from django.db import models
from django import forms
from django.core import validators
from django.core.validators import ValidationError
from django.contrib.auth.models import User

# Create your models here.
def min_length_char(val):
    if len(val)<=4:
        raise validators.ValidationError(f"char must be graeter then 10 char and you enterd {val}")
class Contact(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    city  = models.CharField(validators=[min_length_char], max_length= 20)
    state = models.CharField(max_length = 20)
    zipcode = models.IntegerField()
    # image_of_person = models.ImageField()
    def __str__(self):
        return f"{self.name} {self.email}"
    objects = models.Manager
class Catagory(models.Model):
    title = models.CharField(validators=[min_length_char], max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title





class Posts(models.Model):
    def value_char_check(va):
        if len(va) <= 10:
            raise validators.ValidationError(f"char must be greater then 10 char you write just  {va}")
    email = models.EmailField(validators = [validators.validate_email], max_length= 20)#here we use the pre defined validators
    title = models.CharField(validators=[value_char_check], max_length= 20)#use the coustom validators
    ''' this is of one to one relation ship
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)

   ''' # it is for many to one or one to many
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
    # catagory = models.ManyToManyField(Catagory,related_name='catagory', default= 0)
    catagory = models.ManyToManyField(Catagory, default= 0)
    content = models.TextField(validators=[value_char_check])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager
    def __str__(self):
        return self.title
class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['email', 'title', 'content', 'user', 'catagory']
        def clean(self):
            fields = self.cleaned_data
            keys = list(fields.keys())
            if(len(fields['title']) <=10):
                raise validators.ValidationError("%(val)s Must be Greater Then 10 ", params={'val':keys[0]})
            if(len(fields['Content']) <=10):
                raise validators.ValidationError("%(val)s Must be Greater Then 10 ", params={'val':keys[0]})

