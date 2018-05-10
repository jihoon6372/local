from django.http import HttpResponse, JsonResponse
from django.http import QueryDict
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from .forms import PostForm

# from rest_framework.decorators import list_route, detail_route
# from rest_framework.response import Response

# class PostViewSet(ModelViewSet):
#     queryset = PostViewSet.objectsl.all()
#     serializer_class = PostSerialzer

#     @list_route()
#     def public_list(self, request):
#         qs = self.queryset.filter(is_public=True)
#         serializer = self.get_serializer(qs, manu=True)
#         return Response(serializer.data)

#     @detail_route(methos=['path'])
#     def set_public(self, request, pk):
#         instance = self.get_object()
#         instance.is_public = True
#         instance.save()
#         serializers = self.get_serializer(instance)
#         return Response(serializers.data)


@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        qs = Post.objects.all()
        data = [{'id': post.pk, 'message': post.content} for post in qs]
        return JsonResponse(data, safe=False)
        
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponse(status=201)
        data = form.errors
        return JsonResponse(data, status=400)


