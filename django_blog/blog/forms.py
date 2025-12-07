from django import forms
from .models import Post, Comment, Tag

class PostForm(forms.ModelForm):
    # user will type tags as a comma-separated string
    tags = forms.CharField(required=False,
                           help_text="Enter comma-separated tags (e.g. django,python)",
                           widget=forms.TextInput())

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def clean_tags(self):
        raw = self.cleaned_data.get('tags','')
        # normalize: split by comma, strip, lower, remove empties, unique
        tags = [t.strip().lower() for t in raw.split(',') if t.strip()]
        # optionally enforce some validation:
        if any(len(t)>50 for t in tags):
            raise forms.ValidationError("Each tag must be 50 characters or fewer.")
        # return a cleaned unique list
        return list(dict.fromkeys(tags))

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
