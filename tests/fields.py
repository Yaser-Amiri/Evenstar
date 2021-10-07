import unittest
from evenstar import Field, Arguments, InlineFragment


class TestFieldRendering(unittest.TestCase):
    def test_flat_field(self):
        obj = Field("apple")
        correct_result = "apple"
        self.assertEqual(obj.render(), correct_result)

    def test_flat_field_with_alias(self):
        obj = Field("apple", "fruit")
        correct_result = "fruit: apple"
        self.assertEqual(obj.render(), correct_result)

    def test_flat_field_with_arguments(self):
        obj = Field("apple", arguments=Arguments({"a": 1, "b": False}))
        correct_result = "apple(a: 1, b: false)"
        self.assertEqual(obj.render(), correct_result)

    def test_flat_field_with_arguments_and_alias(self):
        obj = Field(
            "apple", alias="fruit", arguments=Arguments({"a": 1, "b": False})
        )
        correct_result = "fruit: apple(a: 1, b: false)"
        self.assertEqual(obj.render(), correct_result)

    def test_with_arguments_and_alias_and_children(self):
        obj = Field(
            "basket",
            alias="fruits",
            arguments=Arguments({"a": 1, "b": False}),
            children=[
                Field("blueberry", "blue"),
                Field("banana", "yellow"),
                InlineFragment("AAA", ["a", "b"]),
                "j1",
                "j2",
            ],
        )
        correct_result = (
            "fruits: basket(a: 1, b: false) {\nblue: blueberry\n"
            "yellow: banana\n... on AAA {\na\nb\n}\nj1\nj2\n}"
        )
        self.assertEqual(obj.render(), correct_result)

    def test_wrong_type_children(self):
        with self.assertRaises(TypeError) as e:
            Field("SMT", children=[1]).render()
        self.assertEqual(
            e.exception.args[0],
            "Fields's children must be Field or InlineFragment"
            " or str, you passed: <class 'int'>",
        )
