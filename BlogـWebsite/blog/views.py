from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User

from .models import Post, Comment, Category


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def users(request):
    myusers = User.objects.all()

    template = loader.get_template('users.html')

    context = {
        'users': myusers,
    }

    return HttpResponse(template.render(context, request))


def blogs(request):
    myblogs = Post.objects.all()

    template = loader.get_template('blogs.html')

    context = {
        'blogs': myblogs,
    }

    return HttpResponse(template.render(context, request))

def comments(request):
    mycomments = Comment.objects.select_related('blog').all()

    template = loader.get_template('comments.html')

    context = {
        'comments': mycomments,
    }

    return HttpResponse(template.render(context, request))

    return HttpResponse(template.render(context, request))
def categories(request):
    mycategories = Category.objects.all()

    template = loader.get_template('categories.html')

    context = {
        'categories': mycategories,
    }

    return HttpResponse(template.render(context, request))


def blogdetails(request, id):
    myblog = Post.objects.get(id=id)

    template = loader.get_template('blogdetails.html')

    context = {
        'blog': myblog,
    }

    return HttpResponse(template.render(context, request))