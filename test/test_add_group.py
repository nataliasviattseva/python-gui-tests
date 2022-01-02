
def test_add_group(app, json_groups):
    group_name = json_groups.group_name
    old_groups = app.groups.get_groups_list()
    app.groups.add_new_group(group_name)
    new_groups = app.groups.get_groups_list()
    old_groups.append(group_name)
    assert sorted(old_groups) == sorted(new_groups)
