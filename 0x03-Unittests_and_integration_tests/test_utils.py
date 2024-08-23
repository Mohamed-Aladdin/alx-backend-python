#!/usr/bin/env python3
"""Test Utils Module"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap Class
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, nested_map, path, exp_op):
        """to test that the method returns what it is supposed to
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, exp_op)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError)
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, exp_op):
        """to test that a KeyError is raised for the following inputs
        """
        with self.assertRaises(exp_op) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson Class
    """

    @parameterized.expand(
        [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False})
        ]
    )
    def test_get_json(self, url, exp_op):
        """to test that utils.get_json returns the expected result
        """
        mock_response = Mock()
        mock_response.json.return_value = exp_op
        with patch('requests.get', return_value=mock_response):
            response = get_json(url)

            self.assertEqual(response, exp_op)


class TestMemoize(unittest.TestCase):
    """TestMemoize Class
    """

    def test_memoize(self):
        """Test that when calling a_property twice, the correct result is
        returned but a_method is only called once using assert_called_once"""
        class TestClass:
            """Test Class
            """

            def a_method(self):
                """method to return 42
                """
                return 42

            @memoize
            def a_property(self):
                """method"""
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
