from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Notification
from .serializers import NotificationSerializer


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by("read", "-timestamp")


class MarkNotificationAsReadView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    queryset = Notification.objects.all()

    def patch(self, request, pk):
        notification = self.get_object()
        if notification.recipient != request.user:
            return Response({"detail": "Not allowed"}, status=403)

        notification.read = True
        notification.save()
        return Response({"detail": "Notification marked as read."}, status=200)
