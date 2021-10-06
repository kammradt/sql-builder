from builder import Select

print(
    Select('field').from_('table').where_('a = 1').group_by_(1)
)

print(
    Select('field').from_('table').where_('a = 1').and_('b = 2')
)

print(
    Select('field').from_('table').where_('a = 1').or_('b = 2').limit_(10)
)
