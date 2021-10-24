from django.urls    import path
from posts.views  import PostView, PostDetailView

urlpatterns = [
  path('/post', PostView.as_view()),
  path('/post/<int:post_id>', PostDetailView.as_view()),
]