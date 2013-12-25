from employee.tests import *

class TestContemployeeController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='contemployee', action='index'))
        # Test response...
