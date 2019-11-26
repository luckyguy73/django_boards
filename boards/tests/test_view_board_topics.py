from boards.models import Board
from boards.views import TopicListView
from django.test import TestCase
from django.urls import reverse, resolve


class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        self.response = self.client.get(board_topics_url)
        self.homepage_url = reverse('home')

    def test_board_topics_view_success_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func.view_class, TopicListView)

    def test_board_topics_view_contains_link_back_to_homepage(self):
        self.assertContains(self.response, 'href="{0}"'.format(self.homepage_url))

    def test_board_topics_view_contains_navigation_links(self):
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        self.assertContains(self.response, 'href="{0}"'.format(new_topic_url))

