# blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Post title", "class": "form-input"}),
            "content": forms.Textarea(attrs={"placeholder": "Write your post...", "rows": 10, "class": "form-textarea"}),
        }
