from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionsTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        """
        GET /inscricao/ must return status code 200
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """
        Must use subscriptions/subscription_form.html
        """
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        """
        Html must contain input tags
        """
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """
        Html must contain csfr
        """
        self.assertContains(self.resp, 'csrfmiddlewaretoken')
        """
        Context must have subscription form
        """
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_has_form(self):
        """
        Context must have subscription form
        """
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """
        Form must have 4 fields
        """
        form = self.resp.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))

class SubscribePostTes(TestCase):
    def setUp(self):
        data = dict(name='Raffael Tancman', cpf='12345678901', email='rtancman@gmail.com', phone='21-99999-9999')
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        """
        Valid POST should redirect to /inscricao/
        """
        self.assertEqual(302, self.resp.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_subscription_email_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, email.subject)

