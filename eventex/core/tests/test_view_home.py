from django.test import TestCase
from django.shortcuts import resolve_url as r

class HomeTest(TestCase):
    fixtures = ['keynotes.json']

    def setUp(self):
        self.resp = self.client.get(r('home'))

    def test_get(self):
        """
        GET / must return status code 200
        """
        self.assertEquals(200,self.resp.status_code)

    def test_template(self):
        """
        must use index.html
        """
        self.assertTemplateUsed(self.resp, "index.html")

    def test_subscription_link(self):
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.resp, expected)

    def test_speakers(self):
        """
        must show keynote speakers
        """
        contents = [
            'href="{}"'.format(r('speaker_detail', slug='grace-hopper')),
            'href="{}"'.format(r('speaker_detail', slug='alan-turing')),
            'Grace Hopper',
            'http://hbn.link/hopper-pic',
            'Alan Turing',
            'http://hbn.link/turing-pic',
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_speakers_link(self):
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.resp, expected)

    def test_talks_link(self):
        expected = 'href="{}"'.format(r('talk_list'))
        self.assertContains(self.resp, expected)
