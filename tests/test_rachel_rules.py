# tests/test_rachel_rules.py
import unittest
from classroom_bot.knowledge_base import KNOWLEDGE_BASE
from classroom_bot.rules.rachel import match_rachel_rule

class TestRachelRules(unittest.TestCase):
    def test_q4_class_strength(self):
        for q in ["how many students are in our class", "what's our class strength", "how many people in our section"]:
            resp = match_rachel_rule(q, KNOWLEDGE_BASE)
            self.assertIsNotNone(resp, f"Query '{q}' failed to match Q4")
            self.assertIn("Total Students", resp)

    def test_q12_minor_program(self):
        resp = match_rachel_rule("what are the minors", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp)
        self.assertIn("18", resp)

    def test_q13_certificate_program(self):
        resp = match_rachel_rule("what certificate programs are available", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp)
        self.assertIn("30 Contact Hours", resp)

    def test_q18_subject_faculty(self):
        # AI and DBMS are not subjects in this section's timetable, so test real subjects.
        resp_dl = match_rachel_rule("who teaches dl", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_dl)
        self.assertIn("Dr. Amos Bortiew", resp_dl)
        resp_nlp = match_rachel_rule("who teaches nlp", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_nlp)
        self.assertIn("Dr. D Vinodha", resp_nlp)
        resp_dip = match_rachel_rule("which faculty handles dip", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_dip)
        self.assertIn("Prof. Wims Magdalene Mary A", resp_dip)

    def test_q19_course_credits(self):
        resp_dl = match_rachel_rule("how many credits does dl have", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_dl)
        self.assertIn("4 Credits", resp_dl)
        resp_sir = match_rachel_rule("what are the credits for sir", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_sir)
        self.assertIn("3 Credits", resp_sir)

    def test_q21_mentor_mentee(self):
        # Mentors are looked up by full registration number, not by short roll number.
        resp_roll = match_rachel_rule("who is my mentor for roll 2462132", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_roll)
        self.assertIn("Rachel Febin Pulicken", resp_roll)
        self.assertIn("Dr Santhrupth B C", resp_roll)
        resp_prof = match_rachel_rule("which students are under professor swati", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_prof)
        self.assertIn("Prof Swati Raj", resp_prof)
        self.assertIn("Total Mentees: 7", resp_prof)
        self.assertIn("Vedant Joshi", resp_prof)

if __name__ == "__main__":
    unittest.main()
