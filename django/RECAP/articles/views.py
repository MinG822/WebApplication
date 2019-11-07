from django.shortcuts import render, redirect, get_object_or_404 #개발 에러를 띄우면안되니까 중요. 시험!
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from IPython import embed
from django.http import Http404, HttpResponse
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    # embed()
    # request.user
    visit_num = request.session.get('visits', 0)
    request.session['visits'] = visit_num + 1
    request.session.modified = True
    embed()
    articles = Article.objects.all()
    context = {
        'articles':articles,
        'visits': visit_num,
    }
    return render(request, 'articles/index.html', context) # http request = render

# detail
def detail(request, article_pk):
    # article = get_object_or_404(Article, pk=article_pk)
    # 만약 Article.objects.get(pk=article_pk)가 있으면 변수에 저장, 아니면 에러를 띄운다.
    try:
        article = Article.objects.get(pk=article_pk)
        comments = article.comment_set.all()
        form = CommentForm()
    except Article.DoesNotExist:
        raise Http404('해당하는 id의 글이 존재하지 않습니다.')

    context = {
        'article' : article,
        'comments' : comments,
        'form' : form,
    }

    return render(request, 'articles/detail.html', context)

@require_POST #디폴트 redirect url이 login. 다른 곳으로 가고 싶으면 require_POST(login_url="/accounts/log_in") 또는 settings 의 login_url에 박아두어도된다. 
def comment_create(request, article_pk):
    form = CommentForm(request.POST)
    article = Article.objects.get(pk=article_pk)
    # embed()
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.article = article
        new_comment = form.save()
        return redirect(article)
    else:
        return redirect(article)

@require_POST
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    article = Article.objects.get(pk=article_pk)
    comment.delete()
    return redirect(article)

# create
@login_required #next가 붙어서 더 논리적이다. next 핸들링 구문도 넣어줘야한다.
def create(request):
    if request.user.is_authenticated:
    # if not request.user.is_authenticated:
    #     return redirect('accounts:create')
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            # embed() 
            # 장고가 파일을 실행하다 embed를 만나면 실행을 잠시 중단한 이후 shell(shell_plus가 ipython shell을 인식해서 ipython_shell로 실행)을 켜주게 된다. 
            # 모든 맥락들이 들어있는 shell (일일이 import 하고 실행해보지 않아도된다.)
            # 결국 편한 디버깅 지원
            # 이시점에서는 저 밑의 else의 form = ArticleForm()이 실행되었을 것이다.
            # 이때 request.POST 를 실행할시 우리가 가지고 있는 데이터가 나온다.
            # type(request.POST)를 할 시 결과. 쿼리를 넘겨주는 딕셔너리와 같은 객체
            # 그러니까 날리려는 순간 약간 얼음! 같은 존재

            # 전송된 데이터가 유효한 값인지 검사
            if form.is_valid(): # 서버쪽 유효성 검사
                # title = form.cleaned_data.get('title')
                # 유효성검사를 통과한 친구들만 깔끔해진 데이터를 가지고 있는 딕셔너리
                # form 클래스가 가지고 있는 속성같은 것
                # is_valid()를 해야지만 cleaned_data에 들어갈 수 있는 애들이 들어가게된다.
                # content = form.cleaned_data.get('content')
                # new_article = Article.objects.create(title=title, content=content)
                new_article = form.save()
                # 이 모든 것 대신 form.save()해주면 된다.
                return redirect(new_article)
            else:
                return redirect('articles:create')
        else:
            form = ArticleForm() # 프론트엔드단에서 validation 로직을 포함한 폼이 생긴다. required 는 null값을 허용하지 않는다는 뜻.
            context = {
                'form' : form,
            }
            return render(request, 'articles/create.html', context)
    return HttpResponse('승인되지 않았습니다.', status=401)


# update -> articles/:id/update 
# def update(request, article_pk):
#     if request.method == 'POST': # 수정한 내용을 제출할 때
#         form = ArticleForm(request.POST)
#         if form.is_valid(): # form 을 통해 제출한 내용이 유효한지 검사한다
#             article = Article.objects.get(pk=article_pk)
#             article.title = form.cleaned_data.get('title')
#             article.content = form.cleaned_data.get('content')
#             article.save() 
#             return redirect(article)
#     else: # 만약 수정하고 싶다고 요청한 경우
#         try: # 수정을 요청한 article이 존재하는지 확인하기 위해 try except 문
#             # embed()
#             form = ArticleForm()
#             article = Article.objects.get(pk=article_pk)
#             context = {
#                 'form': form,
#                 'article': article,
#             }
#             return render(request, 'articles/update.html', context)
#         except Article.DoesNotExist:
#             raise Http404('수정하려는 글이 존재하지 않습니다.')
@login_required
def update(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article) # form.save()는 새롭게 저장하는 것. 그래서 수정하기 위해서는 모델form클래스의 인자로 instance=article을 같이 보내줘야한다
            if form.is_valid():
                # article.title = form.cleaned_data.get('title')
                # article.content = form.cleaned_data.get('content')
                # article.save()
                form.save()
                return redirect(article)
            # 실제 DB의 데이터를 수정

        # 편집 화면
        # form = ArticleForm(initial={ #initial 대신 data도 가능 #모델폼 클래스는 instance로 가능
        #     'title':article.title,
        #     'content':article.content,
        # })
        form = ArticleForm(instance=article)
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'articles/update.html', context)
    return HttpResponse('승인되지 않았습니다.', status=401)

# delete -> articles/:id/delete
# def delete(request, article_pk):
#     try:
#         Article.objects.get(pk=article_pk).delete()
#     except Article.DoesNotExist:
#         raise Http404('지우려는 글이 존재하지 않습니다.')
    
#     return render(request, 'articles/index.html')

# 특정한 method로만 오게 만들고 싶으면 데코레이터를 통해 쓰면된다. 다른 method를 통할 경우 405 에러를 던진다.

@login_required
@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        if request.method == 'POST': # 데코레이터 때문에 필요없긴 하지만 혹시 모르니깐.
            article = get_object_or_404(Article, pk=article_pk)
            article.delete()
            return redirect('articles:index')
        else:
            return redirect(article)
    return HttpResponse('승인되지 않았습니다.', status=401)

# delete를 post방식으로 해야 더 안전하다


# render와 redirect의 차이



# wwr, gitlab, 위시켓, wordpress, slowwolk, mailchimp, 스티비

def send_cooke(request):
    # return render() -> html 페이지 만들어줌
    # return redirect() -> 렌더해주는 주소로 보내줌
    # return reverse()
    # return HttpResponse()  응답객체
    res = HttpResponse('과자 받아랏')
    res.set_cookie('mycookie', 'oreo')
    return res

