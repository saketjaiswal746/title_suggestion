from django.shortcuts import render, redirect
from .forms import BlogPostForm
from .models import BlogPost
from .nlp import suggest_titles
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            # Generate title suggestions
            suggested_titles = suggest_titles(content)
            blog_post = BlogPost.objects.create(content=content, suggested_titles=suggested_titles)
            return redirect('suggested_titles', pk=blog_post.pk)  # Redirect to view titles
    else:
        form = BlogPostForm()

    return render(request, 'blog/create_post.html', {'form': form})

def suggested_titles(request, pk):
    blog_post = BlogPost.objects.get(pk=pk)
    return render(request, 'blog/suggested_titles.html', {'blog_post': blog_post})

@csrf_exempt
def api_suggest_titles(request):
    if request.method == 'POST':
        try:
            # Get content from the request body (assumed to be JSON)
            body = json.loads(request.body)
            content = body.get('content', '')

            if not content:
                return JsonResponse({'error': 'No content provided'}, status=400)

            # Generate title suggestions using the NLP model
            suggested_titles = suggest_titles(content)

            # Return the suggestions as JSON
            return JsonResponse({'suggested_titles': suggested_titles}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid method'}, status=405)



