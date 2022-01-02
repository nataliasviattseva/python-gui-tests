import random
new_group_name = " new group name" + str(random.randrange(10))

def test_edit_group(app, json_groups):
    old_groups = app.groups.get_groups_list()
    selected_group = random.choice(old_groups)
    new_group_name = json_groups.new_group_name
    app.groups.edit_group(selected_group, new_group_name)
    new_groups = app.groups.get_groups_list()
    old_groups.remove(selected_group)
    old_groups.append(new_group_name)
    assert sorted(old_groups) == sorted(new_groups)

