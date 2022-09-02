import unittest
from models.member import Member

class TestMember(unittest.TestCase):
    
    def setUp(self):
        
        self.member = Member("Katie Booth", True, True)
        
        
    def test_member_has_name(self):
        self.assertEqual("Katie Booth", self.member.name)

    def test_member_has_active_status(self):
        self.assertEqual(True, self.member.active)

    def test_member_has_premium_status(self):
        self.assertEqual(True, self.member.premium)