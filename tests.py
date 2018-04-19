# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.urls import reverse
from .models import Customer, Reading
from .views import *

class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Customer.objects.create(id=55, area='Bob5', tariff='Bug5')
        #Create 13 authors for pagination tests
        number_of_authors = 4

        print('testing!')

    #test model
    def test_id_label(self):
        cust=Customer.objects.get(id=55)
        field_label = cust._meta.get_field('id').verbose_name
        self.assertEquals(field_label,'id_intentionalFail')
    #test model - should pass
    def test_char_id_label(self):
        cust=Customer.objects.get(id=55)
        field_label = cust._meta.get_field('area').verbose_name
        self.assertEquals(field_label,'area')
    #test home page
    def test_view_url_exists_at_home_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)
    #1 failure total
