from __future__ import annotations

from django.test import TestCase
from .models import Post

# Create your tests here.
def update_view(object):
        object.page_views = page_views + 1
        return True

class PostViewsTestCase(TestCase):

        def setUp(self):
                Post.objects.create(title="TestTitle", slug="test-title", page_views=0)

        def test_updated_views(self):
                post = Post.objects.get(slug="test-title")
                update_view(post)
                self.assertEqual(post.page_views, 1)