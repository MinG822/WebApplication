from django import forms
from .models import Article, Comment, Comment2

# # Form Class
# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=20,
#         label='제목',
#         help_text='제목은 20자를 넘길 수 없습니다.',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control my-content',
#                 'placeholder': '제목을 입력해주세요',
#             }
#         )
#         )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'form-control my-content',
#                 'placeholder': '내용을 입력해주세요',
#                 'rows': 5,
#                 'cols': 50,
#             }
#         )
#         )

# modelForm class
class ArticleForm(forms.ModelForm):
    # class Meta:
    #     """
    #     사용할 필드를 명시하는 것이 중요하다.
    #     # exclude = ('title', ...)
    #     # widgets = {
    #     #     '필드': form속성
    #     # }
    #     """
    #     model = Article
    #     fields = ('title', 'content',)

    #     widgets = {
    #         'title': forms.TextInput(attrs={
    #             'placeholder': '제목을 입력해주세요.',
    #             'class': 'form-control my-content',
    #             'id': 'title'
    #         })
    #     }
    
    # 필드를 커스텀하여 관리하기 편한 방식: 장고에서는 이러한 것을 추천한다.

    class Meta:
        model = Article
        fields = ('title', 'content',)


    title = forms.CharField(
        max_length=20,
        label='제목',
        help_text='제목은 20자를 넘길 수 없습니다.',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control my-content',
                'placeholder': '제목을 입력해주세요',
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control my-content',
                'placeholder': '내용을 입력해주세요',
                'rows': 5,
                'cols': 50,
            }
        )
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
    
    content = forms.CharField(
        max_length=300,
        label='댓글',
    )
    # article = forms.ModelChoiceField(queryset=Article.objects.all())




# 보충수업
class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment2
        fields = ('content',)