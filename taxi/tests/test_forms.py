from django.test import TestCase

from taxi.forms import DriverCreationForm


class FormTests(TestCase):
    def test_driver_creation_form_is_valid(self):
        form_data = {
            "username": "test_username",
            "password1": "1qazcde3",
            "password2": "1qazcde3",
            "first_name": "Test first",
            "last_name": "Test last",
            "license_number": "TES12346",
        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)