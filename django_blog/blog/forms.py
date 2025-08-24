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
from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas"
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True, *args, **kwargs):
        instance = super().save(commit=False, *args, **kwargs)
        if commit:
            instance.save()
            tag_names = [t.strip() for t in self.cleaned_data['tags'].split(',') if t.strip()]
            tag_objs = []
            for name in tag_names:
                tag, created = Tag.objects.get_or_create(name=name)
                tag_objs.append(tag)
            instance.tags.set(tag_objs)
        return instance
