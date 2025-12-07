from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), label='')

    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        data = self.cleaned_data.get('content','').strip()
        if not data:
            raise forms.ValidationError("Comment cannot be empty.")
        if len(data) > 2000:
            raise forms.ValidationError("Comment is too long (max 2000 characters).")
        return data
