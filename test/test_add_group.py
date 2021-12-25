def add_test_group(app):
    old_groups = app.groups.get_grops_list()
    app.groups.add_new_group("group name")
    new_groups = app.groups.get_grops_list()
    old_groups.append("group name")
    assert sorted(old_groups) == sorted(new_groups)
