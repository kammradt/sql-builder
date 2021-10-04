from builder import Select

print(
    Select('field').from_('table').where_('a = 1').group_by_(1)
)