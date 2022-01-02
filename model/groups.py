from sys import maxsize


class Group:

    def __init__(self, group_name=None, new_group_name=None):
        self.group_name = group_name
        self.new_group_name = new_group_name

    # def __repr__(self):
    #     return "%s;%s" % (self.group_name, self.new_group_name)
