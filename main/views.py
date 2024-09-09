from django.shortcuts import render, redirect, get_object_or_404
from database.models import News, Categories, Comment
from django.urls import reverse


def create_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        category =  get_object_or_404(Categories,id=category_id)
        News.objects.create(title=title, content=content, category=category)
        return redirect('news_list')

    categories = Categories.objects.all()
    return render(request, 'main/create_news.html', context={'categories': categories})


def update_news_page(request, id):
    news = get_object_or_404(News, id=id)
    categories = Categories.objects.all()
    if news.category:
        category = get_object_or_404(Categories, id=news.category.id)
    else:
        category = None
    return render(request, 'main/update_news.html', context={'news': news, 'categories': categories, 'category': category})
def update_news(request, id):
    news = get_object_or_404(News, id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        category = get_object_or_404(Categories, id=category_id)
        news.title = title
        news.content = content
        news.category = category
        news.save()

    return redirect('news_list')



def news_list(request):
    news = News.objects.all().prefetch_related('comments')
    return render(request, 'main/news_list.html', context={'news': news, })


def delete_news(request, id):
    news = get_object_or_404(News, id=id)
    news.delete()
    return redirect('news_list', )



def comment_page(request, id):
    news = get_object_or_404(News,id=id)
    comments = Comment.objects.filter(news=news)
    return render(request, 'main/add_comment.html', context={'news': news, 'comments': comments})


def create_comment(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        news_id = request.POST.get('news_id')
        user = request.POST.get('user')
        news =  get_object_or_404(News,id=news_id)
        Comment.objects.create(content=content, news=news, user=user)
        return redirect('news_list')

