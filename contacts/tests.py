"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from contacts.models import Contact

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class ContactTests(TestCase):
  
  def test_str(self):
    c = Contact(first_name = 'JoHn', last_name='Smith')

    self.assertEquals(
          str(c),
          'John Smith',
        )