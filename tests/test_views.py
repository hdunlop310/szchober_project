import os
from django.urls import reverse
from django.test import TestCase

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

class index_View_Tests(TestCase):
    def setUp(self):
       self.response = self.client.get(reverse('szchober:index'))
       self.content = self.response.content.decode()

    def test_template(self):
       self.assertTemplateUsed(self.response, 'szchober/index.html', f"{FAILURE_HEADER}Is index.html being called{FAILURE_FOOTER}")

    def test_for_rider_hyperlink(self):
       response = self.client.get(reverse('szchober'))
       self.assertContains(response, '<a href="%s">Rider</a>' % reverse("szchober:become-a-rider"), html=True)

    def test_for_driver_hyperlink(self):
       response = self.client.get(reverse('szchober'))
       self.assertContains(response, '<a href="%s">Driver</a>' % reverse("szchober:become-a-driver"), html=True)

    def test_for_about_hyperlink(self):
       response = self.client.get(reverse('szchober'))
       self.assertContains(response, '<a href="%s">About us</a>' % reverse("szchober:about-us"), html=True)

class sign_up_Tests(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('szchober:sign-up'))
        self.content = self.response.content.decode()

    def test_template(self):
        self.assertTemplateUsed(self.response, 'szchober/sign-up.html',
                                f"{FAILURE_HEADER}Is sign-up.html being called?{FAILURE_FOOTER}")

class find_lift_Tests(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('szchober:find-a-lift'))
        self.content = self.response.content.decode()

    def test_template(self):
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(self.response, 'szchober/find-a-lift.html',
                                f"{FAILURE_HEADER}Is become_a_find-a-lift.html being called?{FAILURE_FOOTER}")

class about_Tests(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('szchober:about-us'))
        self.content = self.response.content.decode()

    def test_template(self):
        self.assertTemplateUsed(self.response, 'szchober/about-us.html',
                                f"{FAILURE_HEADER}Is about-us.html being called?{FAILURE_FOOTER}")
    def test_for_about_hyperlink(self):
       response = self.client.get(reverse('szchober:about-us'))
       self.assertContains(response, '<a href="%s">About us</a>' % reverse("szchober:about-us"), html=True)

    def test_for_rider_hyperlink(self):
       response = self.client.get(reverse('szchober:about-us'))
       self.assertContains(response, '<a href="%s">Rider</a>' % reverse("szchober:become-a-rider"), html=True)

    def test_for_driver_hyperlink(self):
       response = self.client.get(reverse('szchober:about-us'))
       self.assertContains(response, '<a href="%s">Driver</a>' % reverse("szchober:become-a-driver"), html=True)

class feedback_Tests(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('szchober:feedback'))
        self.content = self.response.content.decode()

    def test_template(self):

        self.assertTemplateUsed(self.response, 'szchober/feedback.html',
                                f"{FAILURE_HEADER}Is feedback.html being called?{FAILURE_FOOTER}")


class login_Tests(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('szchober:login'))
        self.content = self.response.content.decode()

    def test_template(self):
        self.assertTemplateUsed(self.response, 'szchober/login.html',
                                f"{FAILURE_HEADER}Is login.html being called?{FAILURE_FOOTER}")

