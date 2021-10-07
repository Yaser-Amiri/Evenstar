import unittest
from evenstar import Arguments, Enum, VarSymbol


class TestArgumentsRendering(unittest.TestCase):
    def test_without_members(self):
        with self.assertRaises(ValueError) as e:
            Arguments({})
        self.assertEqual(
            e.exception.args[0], "Arguments must have at least one member."
        )

    def test_flat(self):
        obj = Arguments(
            {
                "a": 1,
                "b": 2.123,
                "c": False,
                "d": None,
                "e": "Black!",
                "f": Enum("APPLE"),
                "g": VarSymbol("$count"),
            }
        )
        correct_result = (
            "a: 1, b: 2.123, c: false, d: null, "
            'e: "Black!", f: APPLE, g: $count'
        )
        self.assertEqual(obj.render(), correct_result)

    def test_inner_list(self):
        py_list = [
            1,
            2.123,
            False,
            None,
            "Black!",
            Enum("APPLE"),
            VarSymbol("$count"),
        ]
        obj = Arguments({"x": py_list, "y": py_list})
        correct_result = (
            'x: [1, 2.123, false, null, "Black!", APPLE, $count], '
            'y: [1, 2.123, false, null, "Black!", APPLE, $count]'
        )
        self.assertEqual(obj.render(), correct_result)

    def test_inner_dict(self):
        py_dict = {
            "a": 1,
            "b": 2.123,
            "c": False,
            "d": None,
            "e": "Black!",
            "f": Enum("APPLE"),
            "g": VarSymbol("$count"),
        }
        obj = Arguments({"x": py_dict, "y": py_dict})
        correct_result = (
            "x: {a: 1, b: 2.123, c: false, d: null, "
            'e: "Black!", f: APPLE, g: $count}, '
            "y: {a: 1, b: 2.123, c: false, d: null, "
            'e: "Black!", f: APPLE, g: $count}'
        )
        self.assertEqual(obj.render(), correct_result)

    def test_mix_dict_and_list(self):
        py_dict = {
            "a": 1,
            "b": 2.123,
            "c": False,
            "d": None,
            "e": "Black!",
            "f": Enum("APPLE"),
            "g": VarSymbol("$count"),
            "h": [
                9,
                9.321,
                None,
                True,
                "White!",
                Enum("BANANA"),
                VarSymbol("$quantity"),
                {"p1": [2, False], "p2": [None, 2.3]},
            ],
        }
        obj = Arguments({"x": py_dict, "y": py_dict})
        correct_result = (
            'x: {a: 1, b: 2.123, c: false, d: null, e: "Black!", f: APPLE, '
            'g: $count, h: [9, 9.321, null, true, "White!", BANANA, '
            "$quantity, {p1: [2, false], p2: [null, 2.3]}]}, "
            'y: {a: 1, b: 2.123, c: false, d: null, e: "Black!", f: APPLE, '
            'g: $count, h: [9, 9.321, null, true, "White!", BANANA, '
            "$quantity, {p1: [2, false], p2: [null, 2.3]}]}"
        )
        self.maxDiff = None
        self.assertEqual(obj.render(), correct_result)
