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
    '''
    post:
    signup api to get your token for authorization.

    If you already have an account, use the login api to get your token. 
    
    If you do not have an account use this api. The signup api provides the token needed for authorization for all other todo apis. Copy the token after using the signup api and paste the token in the Authorize button at the top right of the page.

    '''
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
    '''
    post:
    login api to get your token for authorization.

    If you have not signed up, use the signup api below. The login api provides the token needed for authorization for all other todo apis. Copy the token after using the login api and paste the token in the Authorize button at the top right of the page.

    '''
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
    '''
    get:
    api to get list of completed todos.

    this api requires authorization. use the login api or signup api if you do not have an account yet to get your authorization token.
    '''
    serializer_class = TodoSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_anonymous:
            raise AuthenticationFailed()
        return Todo.objects.filter(user=self.request.user, datecompleted__isnull=False).order_by('-datecompleted')


class TodoListCreate(generics.ListCreateAPIView):
    '''
    post:
    api to create new todos.

    this api requires authorization. use the login api or signup api if you do not have an account yet to get your authorization token.

    get:
    api to list all todos.

    this api requires authorization. use the login api or signup api if you do not have an account yet to get your authorization token.
    '''
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
    '''
    get:
    api to get a specific todo.

    this api requires authorization. use the login api or signup api if you do not have an account yet to get your authorization token.

    put:
    api to update a specific todo.

    this api requires authorization. use the login api or signup api if you do not have an account yet to get your authorization token.

    patch:
    api to update a specific todo.

    this api requires authorization. use the login api or signup api if you do not have an account yet to get your authorization token.

    delete:
    api to delete a specific todo.

    this api requires authorization. use the login api or signup api if you do not have an account yet to get your authorization token.
    '''
    serializer_class = TodoSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)


class TodoComplete(generics.UpdateAPIView):
    '''
    get:
    api to get list of completed todos.

    this api requires authorization. use the login api or signup api if you do not have an account yet to get your authorization token.

    put:
    api to update a specific completed todo.

    this api requires authorization. use the login api or signup api if you do not have an account yet to get your authorization token.

    patch:
    api to update a specific completed todo.

    this api requires authorization. use the login api or signup api if you do not have an account yet to get your authorization token.
    '''
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
