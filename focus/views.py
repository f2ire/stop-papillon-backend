from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Session
from .serializers import SessionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class SessionViewSet(viewsets.ModelViewSet):
    # queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Session.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response({"message": f"Hello {request.user.username}, you're authenticated!" })
    

