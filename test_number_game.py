import unittest
from number_game import get_ai_hint, calculate_score

class TestNumberGame(unittest.TestCase):

    # ── AI Hint Tests ──────────────────────────────────────────────────────

    def test_hint_go_higher(self):
        _, direction, _, _ = get_ai_hint(50, 30, 1, 1, 100)
        self.assertIn("HIGHER", direction)

    def test_hint_go_lower(self):
        _, direction, _, _ = get_ai_hint(30, 50, 1, 1, 100)
        self.assertIn("LOWER", direction)

    def test_hint_exact(self):
        temperature, _, _, _ = get_ai_hint(50, 50, 1, 1, 100)
        self.assertIn("EXACT", temperature)

    def test_hint_burning_hot(self):
        # difference = 2, range = 100, so 2% → burning hot
        temperature, _, _, _ = get_ai_hint(50, 48, 1, 1, 100)
        self.assertIn("hot", temperature.lower())

    def test_hint_freezing(self):
        # difference = 90, range = 100 → freezing
        temperature, _, _, _ = get_ai_hint(95, 5, 1, 1, 100)
        self.assertIn("reezing", temperature)

    def test_smart_hint_range_higher(self):
        _, _, smart_hint, _ = get_ai_hint(70, 40, 1, 1, 100)
        self.assertIn("40", smart_hint)
        self.assertIn("100", smart_hint)

    def test_smart_hint_range_lower(self):
        _, _, smart_hint, _ = get_ai_hint(30, 60, 1, 1, 100)
        self.assertIn("1", smart_hint)
        self.assertIn("60", smart_hint)

    def test_encouragement_first_attempt(self):
        _, _, _, enc = get_ai_hint(50, 30, 1, 1, 100)
        self.assertIsInstance(enc, str)
        self.assertGreater(len(enc), 0)

    # ── Score Tests ────────────────────────────────────────────────────────

    def test_score_decreases_with_attempts(self):
        score_fast = calculate_score(1, 10, 5.0, "Medium")
        score_slow = calculate_score(8, 10, 5.0, "Medium")
        self.assertGreater(score_fast, score_slow)

    def test_score_higher_for_hard(self):
        score_easy   = calculate_score(3, 10, 5.0, "Easy")
        score_expert = calculate_score(3, 10, 5.0, "Expert")
        self.assertGreater(score_expert, score_easy)

    def test_score_never_negative(self):
        score = calculate_score(20, 10, 300.0, "Easy")
        self.assertGreaterEqual(score, 0)

    def test_score_is_integer(self):
        score = calculate_score(3, 10, 5.0, "Medium")
        self.assertIsInstance(score, int)


if __name__ == "__main__":
    unittest.main()
