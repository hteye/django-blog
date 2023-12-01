import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils.timezone import utc

from blogging.models import Post, Category


class PostTestCase(TestCase):
    fixtures = ["blogging_test_fixtures.json"]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "A good title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


class CategoryTestCase(TestCase):
    def test_string_representation(self):
        expected = "A category"
        c1 = Category(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)


class FrontEndTestCase(TestCase):
    fixtures = ["blogging_test_fixtures.json"]

    def setUp(self):
        self.now = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.time_delta = datetime.timedelta(days=15)
        self.author = User.objects.get(pk=1)
        for count in range(1, 11):
            post = Post(
                title=f"Post {count} Title",
                text="foo",
                author=self.author,
            )
            if count < 6:
                post.published_at = self.now - self.time_delta * count
            post.save()

    def test_list_only_published(self):
        response = self.client.get("/posts/")
        response_text = response.content.decode(response.charset)
        self.assertTrue("Recent Posts" in response_text)
        for count in range(1, 11):
            title = f"Post {count} Title"
            if count < 6:
                self.assertContains(response, title, count=1)
            else:
                self.assertNotContains(response, title)

    def test_details_only_published(self):
        for count in range(1, 11):
            title = f"Post {count} Title"
            post = Post.objects.get(title=title)
            response = self.client.get(f"/posts/{post.pk}")
            if count < 6:
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, title)
            else:
                self.assertEqual(response.status_code, 404)
