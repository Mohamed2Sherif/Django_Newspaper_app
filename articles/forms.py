from django.forms import ModelForm
from .models import Comment

class Comment_form(ModelForm) :
    class Meta :
        model = Comment
        fields = ('comment','author')
