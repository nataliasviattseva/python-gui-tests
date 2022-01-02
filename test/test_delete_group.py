import random
group_name = "group name" + str(random.randrange(10))

def test_delete_group(app, json_groups):
    if len(app.groups.get_groups_list()) == 1:
        app.groups.add_new_group("test group")
    group_name = json_groups.group_name
    old_groups = app.groups.get_groups_list()
    app.groups.delete_group(group_name)
    new_groups = app.groups.get_groups_list()
    old_groups.remove(group_name)
    assert sorted(old_groups) == sorted(new_groups)
