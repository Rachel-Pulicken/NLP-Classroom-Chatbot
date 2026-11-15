# tests/test_joshiny_rules.py
import unittest
from classroom_bot.knowledge_base import KNOWLEDGE_BASE
from classroom_bot.rules.joshiny import match_joshiny_rule

class TestJoshinyRules(unittest.TestCase):
    def test_q2_class_teacher(self):
        resp_ct = match_joshiny_rule("who is our class teacher", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_ct)
        self.assertIn("Dr. Poongodi C", resp_ct)
        resp_co = match_joshiny_rule("who is our co-class teacher", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_co)
        self.assertIn("Dr. Jeno Lovesum S P", resp_co)

    def test_q6_faculty_location(self):
        resp = match_joshiny_rule("where is professor poongodi's cabin", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp)
        self.assertIn("Faculty Room", resp)
        # Faculty that exists in the knowledge base is found with role and cabin.
        resp_raghavendra = match_joshiny_rule("where is professor raghavendra's cabin", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_raghavendra)
        self.assertIn("Dr. Raghavendra S", resp_raghavendra)
        self.assertIn("Faculty Room, GF-B3", resp_raghavendra)
        # Faculty that is not in the knowledge base gets a graceful "not found" reply.
        resp_unknown = match_joshiny_rule("where is professor saravanan's cabin", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_unknown)
        self.assertIn("not found", resp_unknown)

    def test_q9_global_elective_enrollment(self):
        resp = match_joshiny_rule("who enrolled in global elective intellectual property rights", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp)
        self.assertIn("Intellectual Property Rights", resp)
        self.assertIn("Total Enrolled: 3 students", resp)
        self.assertIn("Sreehari S", resp)

    def test_q15_sports_representative(self):
        resp = match_joshiny_rule("who is our sports representative", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp)
        self.assertIn("Vedant Joshi", resp)
        self.assertIn("Rachel Febin Pulicken", resp)

    def test_q20_department_info(self):
        resp_hod = match_joshiny_rule("who is our hod", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_hod)
        self.assertIn("Dr. Michael Moses T", resp_hod)
        resp_coord = match_joshiny_rule("who is the program coordinator", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_coord)
        self.assertIn("Dr. Raghavendra S", resp_coord)

if __name__ == "__main__":
    unittest.main()
