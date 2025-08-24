# blog/forms.py
from django import forms
from .models import Post

from django import forms
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Post title", "class": "form-input"}),
            "content": forms.Textarea(attrs={"placeholder": "Write your post...", "rows": 10, "class": "form-textarea"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'}),
        }
