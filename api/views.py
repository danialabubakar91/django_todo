from .serializers import TodoSerializer, TodoCompleteSerializer, TodoLoginSerializer
from todo.models import Todo
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.parsers import JSONParser

@swagger_auto_schema(method='post', request_body=TodoLoginSerializer)
@api_view(['POST'])
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(
                data['username'], password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token': f'token {str(token)}'}, status=201)
        except:
            return JsonResponse({'error': 'That username has already been taken.'}, status=400)


@swagger_auto_schema(method='post', request_body=TodoLoginSerializer)
@api_view(['POST'])
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            request, username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error': 'Could not login. Please check username and password'}, status=400)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)

            return JsonResponse({'token': f'token {str(token)}'}, status=200)


class TodoCompletedList(generics.ListAPIView):
    """
    List users completed todos. This API requires authorization.
    """
    serializer_class = TodoSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_anonymous:
            raise AuthenticationFailed()
        return Todo.objects.filter(user=self.request.user, datecompleted__isnull=False).order_by('-datecompleted')


class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_class = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.is_anonymous:
            raise AuthenticationFailed()
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_anonymous:
            raise AuthenticationFailed()
        return Todo.objects.filter(user=self.request.user, datecompleted__isnull=True)


class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)


class TodoComplete(generics.UpdateAPIView):
    serializer_class = TodoCompleteSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_anonymous:
            raise AuthenticationFailed()
        return Todo.objects.filter(user=self.request.user)
        # queryset just for schema generation metadata

    def perform_update(self, serializer):
        serializer.instance.datecompleted = timezone.now()
        serializer.save()
