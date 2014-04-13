#!/usr/bin/env python2.7
#file: tests.py

u"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

#TODO, write tests

class SimpleTest(TestCase):
    def test_basic_addition(self):
        u"""
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
