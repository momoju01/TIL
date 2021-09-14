from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget= forms.TextInput(
            attrs={
                'class': 'my_title',
                'placeholder':'Enter the Title',
                'maxlength': 20,
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget= forms.Textarea(
            attrs={
                'class': 'my_content',
                'placeholder': 'Enter the Content',
                'rows':5,
                'cols':50,
            }
        )
    )

    class Meta:
        model = Article
        fields = '__all__'
