from rest_framework import serializers
from todo.models import Todo
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id','title','memo','created','datecompleted','important']


class TodoCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id']
        read_only_fields = ['title','memo','created','datecompleted','important']


class TodoLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']