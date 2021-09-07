from pages.main import Main


class TestGotoUserManagement:
    def setup(self):
        self.main=Main()

    def test_goto_user_management(self):
        goto_user=self.main
        goto_user.goto_user_management().AddMenber()
        assert goto_user.get_usermanagetitle("用户管理")

