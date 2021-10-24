
import json
from json.decoder import JSONDecodeError

from django.http          import JsonResponse
from django.views         import View

from posts.models     import Post
from users.models     import User
from wanted_minhokim.utils import login_decorator

# 게시물 등록
class PostView(View):
  @login_decorator
  def post(self, request):
    try:
      data = json.loads(request.body)
      user = request.user

      title = data['title']
      content = data.get('content')

      Post.objects.create(
        title = title,
        content = content,
        user = user
      )

      return JsonResponse({'MESSAGE' : 'SUCCESS'}, status = 201)
    
    except KeyError:
      return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 400)

    except JSONDecodeError:
      return JSONDecodeError({'MESSAGE' : 'JSON_DECODE_ERROR'}, status = 400)

# 전체 게시물 조회
  @login_decorator
  def get(self, request):

    limit = int(request.GET.get('limit', 30))
    offset = int(request.GET.get('offset', 0))

    try:
      post_list = [{
        'id' : post.id,
        '작성자' : User.objects.get(id=post.user.id).name,
        '제목' : post.title,
        '내용' : post.content,
      } for post in Post.objects.all()[offset:limit+offset]]

      return JsonResponse({'MESSAGE' : 'SUCCESS', 'POST_LIST' : post_list}, status = 200)

    except KeyError:
      return JsonResponse({'MESSAGE' : 'KEY_ERROR'}, status = 400)


class PostDetailView(View):
  # 특정 게시물 조회
  @login_decorator
  def get(self, request, post_id):
    if not Post.objects.filter(id=post_id).exists():
      return JsonResponse({'MESSAGE' : 'POST_DOES_NOT_EXIST'}, status = 404)

    post = Post.objects.get(id=post_id)

    post_info = [{
      'id' : post.id,
      '작성자' : User.objects.get(id=post.user.id).name,
      '제목' : post.title,
      '내용' : post.content
    }]

    return JsonResponse({'MESSAGE' : 'SUCCESS', 'POST_IFNO' : post_info}, status = 200)


  # 특정 게시물 삭제
  @login_decorator
  def delete(self, request, post_id):
    try:
      user = request.user
      
      if not Post.objects.filter(id=post_id, user=user).exists():
        return JsonResponse({'MESSAGE' : 'POST_DOES_NOT_EXIST'}, status = 404)

      Post.objects.get(id=post_id, user=user).delete()
      return JsonResponse({'MESSAGE' : 'SUCCESS'}, status = 200)

    except ValueError:
      return JsonResponse({'MESSAGE' : 'VALUE_ERROR'}, status = 400)

  # 게시물 수정
  @login_decorator
  def put(self, request, post_id):
    try:
      user = request.user
      data = json.loads(request.body)

      if not Post.objects.filter(id=post_id).exists():
        return JsonResponse({'MESSAGE' : 'POST_DOES_NOT_EXIST'}, status = 404)

      post = Post.objects.get(id=post_id)

      post.title = data.get('title', post.title)
      post.content = data.get('content', post.content)
      post.save()

      return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=201)

    except JSONDecodeError:
      return JsonResponse({'MESSAGE' : 'JSON_DECODE_ERROR'}, status = 400)