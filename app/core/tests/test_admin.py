from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdmindSiteTests(TestCase):

    def setUp(self):
        """setUp get called before all test case
           we usually do some initial setup here.
        """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@outlook.com',
            password='password@123'
        )
        # it saves us from physically loggin user
        # and login user virtually.
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="vignesh.jeyaraman@outlook.com",
            password="password@123",
            name="Test user full name"
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        # reverse string take app: url name
        # this url is predefined in django
        # reverse is used is because if we ever change
        # url in the future reverse will take care of it
        # automatically.
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        # contains check whether HTTP response code is 200
        # plus whether requirement fields are there or not.
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that user edit page works"""
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
