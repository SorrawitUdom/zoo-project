import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_notvalid(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), None)

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
       
    # Add your additional test cases here
    def test_teenager_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)
    
    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_elder_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

if __name__ == '__main__':
    unittest.main()