class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_groups_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")
        self.close_group_editor()

    def delete_group(self, group_name):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        for node in root.children():
            if node.text() == group_name:
                node.click()
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.delete_group_window = self.app.application.window(title="Delete group")
        self.delete_group_window.window(auto_id="uxDeleteAllRadioButton").click()
        self.delete_group_window.window(auto_id="uxOKAddressButton").click()
        self.close_group_editor()

    def edit_group(self, group_name, new_group_name):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        for node in root.children():
            if node.text() == group_name:
                node.click()
        self.group_editor.window(auto_id="uxEditAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(new_group_name)
        input.type_keys("\n")
        self.delete_group_window = self.app.application.window(title="Delete group")
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()