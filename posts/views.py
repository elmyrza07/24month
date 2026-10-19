from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from posts.models import Post


def post_list(request):
    posts = Post.objects.all()

    # Фильтрация по is_active
    is_active_param = request.GET.get('is_active')
    if is_active_param is not None:
        if is_active_param.lower() in ['true', '1']:
            posts = posts.filter(is_active=True)
        elif is_active_param.lower() in ['false', '0']:
            posts = posts.filter(is_active=False)

    # Поиск по названию или описанию
    query = request.GET.get('search', '').strip()
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    return render(request, 'posts/list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/detail.html', {'post': post})