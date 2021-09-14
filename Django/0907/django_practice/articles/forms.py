from articles.models import Article
from django import forms
from django.forms.widgets import Select

# 일반 Form클래스
# class ArticleForm(forms.Form):
    # REGION_A = 'sl'
    # REGION_B = 'dj'
    # REGION_C = 'gj'
    # REGION_D = 'gm'
    # REGION_CHOICES = [
    #     (REGION_A, '서울'),
    #     (REGION_B, '대전'),
    #     (REGION_C, '광주'),
    #     (REGION_D, '구미'),
        
    # ]
    
    # title = forms.CharField(max_length=20)
    # content = forms.CharField(widget=forms.Textarea)
    # region = forms.ChoiceField(choices=REGION_CHOICES, widget=forms.Select())


# ModelForm 클래스
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget= forms.TextInput(
            attrs={
                'class': 'my_title',
                'placeholder': 'Enter the title',
                'maxlength' : 20,
            }
        )
    )
    content = forms.CharField(
        label = '내용',
        widget = forms.Textarea(
            attrs = {
                'class': 'my_content',
                'placeholder': 'Enter the content',
                'rows' : 5,
                'cols' : 50,
            }
        )
    )
    class Meta:
        model = Article  # 사용할 모델 정보
        fields = '__all__'  # 들고 올 fields 
