import unittest

from sort_string_to_sql import sort_str_to_sql


class TestCase(unittest.TestCase):
    """
        Test sort_string_to_sql function
        """

    def test_case_1(self):
        """
                Test case
                'id'  -> 'id ASC'
                """
        result = sort_str_to_sql(sort_expression='id')
        self.assertEqual(result, 'id ASC')

    def test_case_2(self):
        """
                Test case
                '+id'  -> 'id ASC'
                """
        result = sort_str_to_sql(sort_expression='+id')
        self.assertEqual(result, 'id ASC')

    def test_case_3(self):
        """
                Test case
                '-id' -> 'id DESC'
                """
        result = sort_str_to_sql(sort_expression='-id')
        self.assertEqual(result, 'id DESC')

    def test_case_4(self):
        """
                Test case
                'person.id' -> 'person.id ASC'
                """
        result = sort_str_to_sql(sort_expression='person.id')
        self.assertEqual(result, 'person.id ASC')

    def test_case_5(self):
        """
                Test case
                '+id,-name'  -> 'id ASC, name DESC'
                """
        result = sort_str_to_sql(sort_expression='+id,-name')
        self.assertEqual(result, 'id ASC, name DESC')

    def test_case_6(self):
        """
                Test case
                ' +id , -name '  -> 'id ASC, name DESC'
                """
        result = sort_str_to_sql(sort_expression=' +id , -name ')
        self.assertEqual(result, 'id ASC, name DESC')

    def test_case_7(self):
        """
                Test case
                '-id,+age,-name'  -> 'id DESC, age ASC, name DESC'
                """
        result = sort_str_to_sql(sort_expression='-id,+age,-name')
        self.assertEqual(result, 'id DESC, age ASC, name DESC')

    def test_case_8(self):
        """
                Test case
                ''  -> ''
                """
        result = sort_str_to_sql(sort_expression='')
        self.assertEqual(result, '')

    def test_case_9(self):
        """
                Test case
                Incorrect input types -> ''
                """
        result = sort_str_to_sql(sort_expression=['+id'])
        self.assertEqual(result, '')


if __name__ == '__main__':
    unittest.main()
