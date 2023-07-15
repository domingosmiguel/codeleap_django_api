from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from PostApp.models import Post
from PostApp.serializers import PostSerializer


@csrf_exempt
def postApi(request, id=0):
    if request.method == 'GET':
        posts = Post.objects.order_by('created_datetime').reverse()
        post_serializer = PostSerializer(posts, many=True)
        return JsonResponse(post_serializer.data, safe=False)

    elif request.method == 'POST':
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(data=post_data)

        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse('Post created successfully!', safe=False)
        return JsonResponse(post_serializer.errors, status=400)

    elif request.method == 'PATCH':
        post_data = JSONParser().parse(request)
        post = Post.objects.get(id=id)
        post_serializer = PostSerializer(post, data=post_data, partial=True)

        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse('Post updated successfully!', safe=False)
        return JsonResponse(post_serializer.errors, status=400)

    elif request.method == 'DELETE':
        Post.objects.get(id=id).delete()
        return JsonResponse('Post deleted successfully!', safe=False)
