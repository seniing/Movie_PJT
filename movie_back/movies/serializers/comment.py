from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Comment, Movie

# 세은님 여기에 ()가 없어서 댓글부분에서 에러가 났었네요!!!
User = get_user_model()
class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username',)
    
    user = UserSerializer(read_only=True)

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('user', 'content', 'movie',)
        # read_only_fields = ('user', 'movie',)