from builder import Select

Select('field').from_('table')

Select('field').from_('table').where_('field = 1')

Select('field0, field1').from_('table').where_('field0 = 0').or_('field1 = 1')

Select('field').from_('table').group_by_("field").order_by_("field")

Select().from_('table').limit_(10)
