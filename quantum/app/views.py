from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.http import Http404
from datetime import datetime, date, time
from django.urls import reverse
from .models import *


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'app/list.html', {'latest_articles_list': latest_articles_list})
# Create your views here.


def details(request, article_id):
    try:
      a = Article.objects.get(id=article_id)
      total_comment = len(Comment.objects.filter(article_id=article_id))
    except:
      raise Http404("Статьи не найдены")


    latest_comments_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'app/details.html', {'article': a,
                  'latest_comments_list': latest_comments_list, 'total_comment': total_comment})


def leave_comment(request, article_id):
    try:
      a = Article.objects.get(id=article_id)
    except:
      raise Http404("Статья не найдена")


    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'], comment_pub_date=datetime.now())

    return HttpResponseRedirect(reverse('app:details', args=(a.id,)))


def test(request):
    return HttpResponse("Тестовая Страница должна содержать код для тестирования")


def contact(request):
    return render(request, 'app/menu1.html')
