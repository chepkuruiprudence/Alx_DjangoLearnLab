from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# --- Post form with proper TagWidget ---
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(attrs={'placeholder': 'Add tags separated by commas'})
        }

# --- Comment form ---
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment...'})
        }

    def clean_content(self):
        data = self.cleaned_data.get('content', '').strip()
        if not data:
            raise forms.ValidationError("Comment cannot be empty.")
        if len(data) > 2000:
            raise forms.ValidationError("Comment is too long (max 2000 characters).")
        return data

# --- User registration form ---
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
