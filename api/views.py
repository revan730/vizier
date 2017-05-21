from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.utils.timezone import now
from rest_framework import generics, authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from .models import Screenshot
from .serializers import ScreenDetailSerializer, UserDetailSerializer

class ScreenDetail(generics.RetrieveAPIView):
    serializer_class = ScreenDetailSerializer
    queryset = Screenshot.objects.all()

class UserDetail(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()

class ScreenUpload(APIView):
    authentication_classes = (authentication.BasicAuthentication,)
    parser_classes = (FileUploadParser,)

    def get(self):
        return HttpResponseForbidden()

    def post(self, request):
        screen = Screenshot(raw=request.data['file'], user=request.user,
                            upload_date=now())
        screen.save()

        serializer = ScreenDetailSerializer(screen)

        return Response(serializer.data)



