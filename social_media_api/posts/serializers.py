from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model().objects.create_user


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # display username instead of ID
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Comment content cannot be empty.")
        return value


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # display username
    comments = CommentSerializer(many=True, read_only=True)  # nested comments

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Post content cannot be empty.")
        return value
