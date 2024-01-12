from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
  def setUp(self):
    User.objects.create_user(username='joe', password='bloggs')

  def test_can_list_posts(self):
    joe = User.objects.get(username='joe')
    Post.objects.create(owner=joe, title='test title')
    response = self.client.get('/posts/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_logged_in_user_can_create_post(self):
    self.client.login(username='joe', password='bloggs')
    response = self.client.post('/posts/', {'title': 'test title'})
    count = Post.objects.count()
    self.assertEqual(count, 1)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
  
  def test_user_not_logged_in_cant_create_post(self):
    response = self.client.post('/posts/', {'title': 'test title'})
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
