import unittest
from evenstar import InlineFragment


class TestInlineFragmentRendering(unittest.TestCase):
    def test_flat_strings(self):
        obj = InlineFragment("SMT", ["a", "b"])
        correct_result = "... on SMT {\na\nb\n}"
        self.assertEqual(obj.render(), correct_result)

    def test_without_children(self):
        with self.assertRaises(ValueError) as e:
            InlineFragment("SMT", [])
        self.assertEqual(
            e.exception.args[0], "InlineFragment must have at least one child."
        )

    def test_wrong_type_children(self):
        with self.assertRaises(TypeError) as e:
            InlineFragment("SMT", [1]).render()
        self.assertEqual(
            e.exception.args[0],
            "InlineFragment's children must be Field or"
            " str,you passed: <class 'int'>",
        )
