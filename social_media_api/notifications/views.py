
from rest_framework import generics, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Like
from notifications.models import Notification
from .serializers import NotificationSerializer

class PostViewSet(viewsets.ModelViewSet):
    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        
        like, created = Like.objects.get_or_create(user=user, post=post)
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb='liked your post',
                target=post
            )
            return Response({'status': 'post liked'})
        return Response({'status': 'already liked'})

    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        user = request.user
        
        Like.objects.filter(user=user, post=post).delete()
        return Response({'status': 'post unliked'})

class NotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)