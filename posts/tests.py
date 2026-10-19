from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostModelTests(TestCase):
    def test_post_has_expected_blog_fields(self):
        self.assertTrue(hasattr(Post, 'category'))
        self.assertTrue(hasattr(Post, 'image'))
        self.assertTrue(hasattr(Post, 'image_caption'))
        self.assertTrue(hasattr(Post, 'user'))


class PostViewTests(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title='Hello world',
            description='A test post description.',
            rate=5,
            category='Tech',
        )

    def test_post_list_page_renders_posts(self):
        response = self.client.get(reverse('post_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello world')

    def test_post_detail_page_renders_post(self):
        response = self.client.get(reverse('post_detail', kwargs={'pk': self.post.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello world')
