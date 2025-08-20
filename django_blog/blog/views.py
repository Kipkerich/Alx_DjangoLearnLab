
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

def home_view(request):
    
    return render(request, 'blog/index.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Home redirect URL
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Home redirect URL
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home after logout


def profile_view(request):
    
    return render(request, 'blog/profile.html')


        
@api_view(['GET', 'PUT', 'DELETE'])
def view_posts(request, pk):
    try:
        post =Post.objects.get(pk=pk)
    except post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = Post(Post)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PostSerializer(Post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        Post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
           
@api_view(['POST'])  
def create_posts(request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    
@api_view(['PUT'])
def update_posts(request, pk):
        try:
            post = PostSerializer.objects.get(pk=pk)
        except post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        finally:
            if request.method == 'PUT':
                serializer = PostSerializer(post, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])    
def delete_posts(request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        finally:
            if request.method == 'DELETE':
                post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
