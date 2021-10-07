import unittest
from evenstar import (
    Field,
    Query,
    VarDeclaration,
)


class TestQueryRendering(unittest.TestCase):
    def test_without_name(self):
        obj = Query([Field("banana"), Field("apple")])
        correct_result = "query {\nbanana\napple\n}"
        self.assertEqual(obj.render(), correct_result)

    def test_with_name(self):
        obj = Query([Field("banana"), Field("apple")], name="basket")
        correct_result = "query basket {\nbanana\napple\n}"
        self.assertEqual(obj.render(), correct_result)

    def test_without_name_with_vars(self):
        obj = Query(
            children=[Field("banana"), Field("apple")],
            variables=[
                VarDeclaration("$b", "Float"),
                VarDeclaration("$a", "Int", 234),
            ],
        )
        correct_result = (
            "query ($b: Float, $a: Int = 234)" " {\nbanana\napple\n}"
        )
        self.assertEqual(obj.render(), correct_result)

    def test_with_name_with_vars(self):
        obj = Query(
            children=[Field("banana"), Field("apple")],
            name="basket",
            variables=[
                VarDeclaration("$b", "Float"),
                VarDeclaration("$a", "Int", 234),
            ],
        )
        correct_result = (
            "query basket ($b: Float, $a: Int = 234)" " {\nbanana\napple\n}"
        )
        self.assertEqual(obj.render(), correct_result)
