from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, HttpResponseServerError
from rest_framework import generics, authentication
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
    authentication_classes = (authentication.TokenAuthentication,)
    parser_classes = (FileUploadParser,)

    def get(self, request):
        return HttpResponseForbidden()

    def post(self, request):
        if request.user.is_authenticated():
            return HttpResponseServerError()
            # TODO: Implement file upload
        else:
            return HttpResponseForbidden()



