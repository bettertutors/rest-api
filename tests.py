from unittest import TestCase, main as unittest_main
from re import compile, match

from webtest import TestApp

from bettertutors_rest_api import rest_api


class TestRestApi(TestCase):
    app = TestApp(rest_api)
    has_three_nums = compile('\d{1,3}\.\d{1,3}\.\d{1,3}\w*')

    def test_setup_dots(self):
        """ Not a full semver check, just checking if it starts like num.num.num """
        status_resp = self.app.get('/api/status').json
        for k in status_resp.keys():
            if k.endswith('_version'):
                self.assertTrue(match(self.has_three_nums, status_resp[k]), "Not in semver format")
        # Just an example test, could obviously import `__version__`, but want scaffold for API functional testing


if __name__ == '__main__':
    unittest_main()
