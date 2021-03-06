from unittest import TestCase

from builder import Select


class TestSelect(TestCase):
    def test_repr_and_sql(self):
        select = Select('field')

        self.assertEqual(select.sql(), f'{select}')

    def test_select_star(self):
        expected = 'SELECT *;'
        result = Select().sql()

        self.assertEqual(result, expected)

    def test_select(self):
        expected = 'SELECT field;'
        result = Select('field').sql()

        self.assertEqual(result, expected)

    def test_falsy_values(self):
        invalids = [{}, [], (), '']
        for invalid in invalids:
            with self.assertRaises(ValueError):
                Select(invalid)

            with self.assertRaises(ValueError):
                Select('valid').from_(invalid)

            with self.assertRaises(ValueError):
                Select('valid').from_('valid').where_(invalid)

            with self.assertRaises(ValueError):
                Select('valid').from_('valid').where_('valid').group_by_(invalid)

            with self.assertRaises(ValueError):
                Select('valid').from_('valid').where_('valid').group_by_('valid').order_by_(invalid)

            with self.assertRaises(ValueError):
                Select('valid').from_('valid').where_('valid').group_by_('valid').order_by_('valid').limit_(invalid)

    def test_from(self):
        expected = 'SELECT field FROM table;'
        result = Select('field').from_('table').sql()

        self.assertEqual(result, expected)

    def test_where(self):
        expected = 'SELECT field FROM table WHERE field = 1;'
        result = Select('field').from_('table').where_('field = 1').sql()

        self.assertEqual(result, expected)

    def test_where_with_and(self):
        expected = 'SELECT field0, field1 FROM table WHERE field0 = 0 AND field1 = 1;'
        result = Select('field0, field1').from_('table').where_('field0 = 0').and_('field1 = 1').sql()

        self.assertEqual(result, expected)

    def test_where_with_or(self):
        expected = 'SELECT field0, field1 FROM table WHERE field0 = 0 OR field1 = 1;'
        result = Select('field0, field1').from_('table').where_('field0 = 0').or_('field1 = 1').sql()

        self.assertEqual(result, expected)

    def test_where_with_both(self):
        expected = 'SELECT field0, field1, field2 FROM table WHERE field0 = 0 AND field1 = 1 OR field2 = 2;'
        result = (
            Select('field0, field1, field2')
                .from_('table')
                .where_('field0 = 0')
                .and_('field1 = 1')
                .or_('field2 = 2')
                .sql()
        )

        self.assertEqual(result, expected)

    def test_group_by_str(self):
        expected = 'SELECT field FROM table WHERE field = 1 GROUP BY field;'
        result = Select('field').from_('table').where_('field = 1').group_by_("field").sql()

        self.assertEqual(result, expected)

    def test_group_by_numeric(self):
        expected = 'SELECT field FROM table WHERE field = 1 GROUP BY 1;'
        result = Select('field').from_('table').where_('field = 1').group_by_(1).sql()

        self.assertEqual(result, expected)

    def test_order_by_str(self):
        expected = 'SELECT field FROM table WHERE field = 1 GROUP BY field ORDER BY field;'
        result = (
            Select('field')
                .from_('table')
                .where_('field = 1')
                .group_by_("field")
                .order_by_("field")
                .sql()
        )

        self.assertEqual(result, expected)

    def test_order_by_numeric(self):
        expected = 'SELECT field FROM table WHERE field = 1 GROUP BY 1 ORDER BY 1;'
        result = (
            Select('field')
                .from_('table')
                .where_('field = 1')
                .group_by_(1)
                .order_by_(1)
                .sql()
        )

        self.assertEqual(result, expected)

    def test_limit(self):
        expected = 'SELECT field FROM table WHERE field = 1 LIMIT 1;'
        result = Select('field').from_('table').where_('field = 1').limit_(1).sql()

        self.assertEqual(result, expected)
