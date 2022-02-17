from django import forms
from .models import Post, Category

#creating choices variable for category list loop

choices = Category.objects.all() .values_list('name','name')
choice_list =[]
for item in choices:
    choice_list.append(item)
    

#post form to add post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author','category', 'body',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title Tag'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'', 'id':'userid', 'type':'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post Text'}),

        }

#edit post form to edit post
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ('title', 'title_tag', 'author', 'body',)
        fields = ('title', 'title_tag', 'body',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title Tag'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post Text'}),

        }
