from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Raffael Tancman',
            slug='raffael-tancman',
            photo='https://en.gravatar.com/userimage/13875073/84f1851e22c02c91da36322a80a9170c.jpg'
        )


    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker,kind=Contact.EMAIL,
                                         value='rtancman@gmail.com')

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker,kind=Contact.PHONE,
                                         value='21-99999-9999')

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """
        contact kind should be limete to E or P
        """
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker,kind='E',
                                 value='rtancman@gmail.com')

        self.assertEqual('rtancman@gmail.com', str(contact))