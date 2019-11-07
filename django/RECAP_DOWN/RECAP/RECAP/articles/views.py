from django.shortcuts import render, redirect, get_object_or_404, get_or_create
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentModelForm, CommentForm
from IPython import embed
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from itertools import chain

# Create your views here.
@login_required
def index(request):
    # embed()
    # 세션 조작을 통해 방문수 카운트
    visits_num = request.session.get('visits', 0)
    request.session['visits'] = visits_num + 1
    request.session.modifided = True
    followings = request.user.followings.all()
    # 방법 1
    followings = chain(followings, [request.user])
    articles = Article.objects.filter(user__in=followings)

    context = {
        'articles': articles,
        'visits': visits_num,
    }
    return render(request, 'articles/index.html', context)

"""
# 보충수업용 commentout
def detail(request, article_pk):
    # article = get_object_or_404(Article, pk=article_pk)
    
    # article = Article.objects.get(pk=article_pk)

    # getobjector404
    try:
        article = Article.objects.get(pk=article_pk)
    except Article.DoesNotExist:
        raise Http404('해당하는 글이 없습니다.')

    form = CommentForm()

    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/detail.html', context)
"""

def detail(request, article_pk):
    # article = get_object_or_404(Article, pk=article_pk)

    # article = Article.objects.get(pk=article_pk)

    # getobjector404
    try:
        article = Article.objects.get(pk=article_pk)
    except Article.DoesNotExist:
        raise Http404('해당하는 글이 없습니다.')

    comment_form = CommentForm()

    # 보충수업
    # 명시적으로 commentForm 분리
    comment2_form = CommentModelForm()

    context = {
        'article': article,
        'comment2_form': comment2_form,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    """
    # user 로그인되어있는지 여부를 확인
    if request.user.is_anonymous:
        return redirect('accounts:login')
    """
    if request.method == 'POST':
        # embed()
        # 이 코드는 아래 코드로 대체
        # title = request.POST.get('title')
        # content = request.POST.get('content')        
        # new_article = Article.objects.create(title=title, content=content)

        form = ArticleForm(request.POST)
        
        # 전송된 데이터가 유효한지 검사
        if form.is_valid():
            # Using Form
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)

            # # using modelForm
            # article = form.save()

            # using user_id
            article = form.save(commit=False)
            article.user = request.user
            article.save()

            #hashtag
            for word in article.content.split():
                if word.startswith('#'):
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    #return 값이 (객체, T/F)
                    article.hastags.add(hashtag)
        # form.save()도 가능하지만 일단 데이터 클렌징 먼저 시행한다.

            return redirect(article)
        else:
            return redirect('articles:create')
    else:
        form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/create.html', context)

# UPDATE => articles/:id/update | (PUT) articles/:id (REST)
# DELETE => articles/:id/delete

@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    """
    추가: article을 수정하려는 유저가 접속한 유저와 같을 경우에만 등록
    """
    if article.user == request.user:
        if request.method == 'POST':
            # form = ArticleForm
            embed()
            # 만약 ArticleForm에 인자를 하나 넘겨주면 생성, instance 인자를 함께 넘겨주면 수정
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect(article)
                # using Form
                # article.title = form.cleaned_data.get('title')
                # article.content = form.cleaned_data.get('content')
                # article.save()

                # using modelForm
                # article = form.save()
                # return redirect(article)
    
        form = ArticleForm(instance=article)
        context = {
            'article': article,
            'form': form,
        }

        # article = Article.objects.get(pk=article_pk)
        # form = ArticleForm(initial={
        #     'title': article.title,
        #     'content': article.content,
        # })
        # context = {
        #     'article': article,
        #     'form': form,
        # }
        
        return render(request, 'articles/update.html', context)
    else:
        return redirect(article)

# make decorators for delete function
@login_required
@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    """
    추가: article을 수정하려는 유저가 접속한 유저와 같을 경우에만 삭제
    """
    if article.user == request.user:
        if request.method == 'POST':
            article.delete()
            return redirect('articles:index')
        else:
            return redirect(article)
    else:
        return redirect(article)

"""
# custom error(401 Error: Unauthorized User Error)
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if request.method == 'POST':
            article.delete()
            return redirect('articles:index')
        else:
            return redirect(article)

    return HttpResponse('검증되지 않은 유저입니다.', status=401)
"""

def comment(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
    
    return redirect(article)

@require_POST
def comment_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
    
    return redirect("articles:detail", article_pk=article_pk)

# 보충수업
def comment2(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'POST':
        comment_form = CommentModelForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)# commit == database commit, 실제 데이터베이스에 저장하는 과정
            embed()

            # 방법1
            comment.article_id = article_pk

            comment.save()

            # 객체를 직접 넣는것도 가능
            # comment.article = Article.objects.get(pk=article_pk)
    
    return redirect(article)


def comment2_delete(request, article_pk, comment_pk):
    pass


def send_cookie(request):
    """
    현재까지 return했던 것
    render(), redirect(), reverse(), HttpResponse()
    """

    res = HttpResponse('과자보냅니다')
    res.set_cookie('mycookie', 'oreo')
    return res


# like 기능
@login_required
def like(request, article_pk):
    # article_pk를 user가 좋아하는 것을 추가
    article = get_object_or_404(Article, pk=article_pk)
    # article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    """
    # 방법 1
    request.user.like_articles.add(Articles.objects.get(pk=article_pk))
    """
    """
    # 방법2 
    request.user.like_articles.add(article)
    """
    """
    # 방법 3
    else:
        article.like_users.add(request.user)
    """

    return redirect(article)

@login_required
@require_POST
def like2(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    # embed()
    """
    try:
        article.like_users.get(pk=user.pk)
        article.like_users.remove(request.user)
    except:
        article.like_users.add(request.user)
    """

    # 다른 방법
    if article.like_users.filter(pk=user.pk).exists(): # SQL-WHERE과 같은 역할을 한다.
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    
    """
    .get()의 경우 하나의 객체만 리턴한다.
    .filter()의 경우 여러 객체에 대한 queryset을 리턴한다.
    단, .get()보다는 .filter()를 쓰는 것이 좋은 이유는 없을 경우에 대한 error handling의 용이성때문이다.
    만약 찾는 객체가 없을 경우 .get()은 None을 리턴하여 에러를 발생시키지만, .filter()는 빈 쿼리셋을 리턴하기 때문에 

    """

    return redirect(article)


def explore(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/explore.html', context)

def tags(request):
    tags = Hashtag.objects.all()
    context = {
        'tags' : tags,
    }
    return render(request, 'articles/tags.html', context)

def hashtag(request, hashtag_pk):
    hashtag = get_object_or_404(Hashtag, pk=hashtag_pk)
    articles = hashtag.article_set.all()
    context = {
        'hashtag': hashtag,
        'articles':articles,
    }
    return render(request, 'articles/hashtags.html', context)