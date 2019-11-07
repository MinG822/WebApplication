from django import forms
from .models import Article, Comment
from IPython import embed

# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=20,
#         label='제목',
#         help_text='제목은 20자 이내로 써주세요.',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control mt-content',
#                 'placeholder': '제목을 입력해주세요.',
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'form-control my-content',
#                 'placeholder': '내용을 입력해주세요',
#                 'rows': 5,
#             }
#         )
#     )

# 크루드 로직 전체를 만들어놓고 하는게 좋다
class ArticleForm(forms.ModelForm): #form클래스가 아닌 modelform클래스, form과 model을 연결해 놓은 클래스이다, 위의 form 클래스에서 일일이 지정했던 걸 대신해준다.
    class Meta:
        model = Article
        fields = ('title', 'content',) # created_at과 updated_at은 장고가 대신 해주므로 안써줘도 된다
        #  exclude = ('title') 제외하고 싶은 필드를 명시할 수 있다
        #  widget = {
        #      'title': forms.TextInput(
        #          attrs={
        #              'placeholder': '제목을 입력해주세요.',
        #              'class': 'form-control title-class',
        #              'id': 'title',
        #         })
        # }
    title = forms.CharField( # 로직상 meta 안에 widget으로 집어넣는 것보다 바깥에서 하나하나에 대해 작성하는게 좋다. 관리하기도 좋음
        max_length=20,
        label='제목',
        help_text='제목은 20자 이내로 써주세요.',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mt-content',
                'placeholder': '제목을 입력해주세요.',
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
            }
        )
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

    title = forms.TextInput(
        attrs={
            'class': 'form-control mt-content',
            'placeholder': '코멘트를 작성해 주세요'
        }
    )
    # def __init__(self, *args, **kwargs):
    #     embed()
    #     article_pk = args
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #     self.fields['article'].queryset = Article.objects.filter(pk=article_pk)
        