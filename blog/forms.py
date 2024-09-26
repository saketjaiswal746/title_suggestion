from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 10,
                'cols': 80,
                'class': 'form-control',  # Bootstrap styling
                'placeholder': 'Write your blog post content here...',
                'style': 'resize: vertical;'  # Allows only vertical resizing
            }),
        }
