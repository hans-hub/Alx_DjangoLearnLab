from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import permission_required
from .models import Article

@permission_required('bookseview', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})

@permission_required('advanced_features_and_security.can_create', raise_exception=True)
def article_create(request):
    if request.method == 'POST':
        # handle creation
        pass
    return render(request, 'articles/create.html')

@permission_required('advanced_features_and_security.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # handle edit
    return render(request, 'articles/edit.html', {'article': article})

@permission_required('advanced_features_and_security.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')