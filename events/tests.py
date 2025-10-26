from django.test import TestCase
from django.urls import reverse
from .models import Event


class EventsIndexTests(TestCase):
	def test_index_shows_no_events_message_when_empty(self):
		resp = self.client.get(reverse('events:index'))
		self.assertEqual(resp.status_code, 200)
		self.assertContains(resp, 'No events found')

	def test_index_shows_event_when_exists(self):
		Event.objects.create(name='Test Event')
		resp = self.client.get(reverse('events:index'))
		self.assertEqual(resp.status_code, 200)
		self.assertContains(resp, 'Test Event')
