from pages.main import Main


class TestAlterMenberInfo:
    def setup(self):
        self.main = Main()

    def test_alter_menberinfo(self):
        altermenberinfo = self.main.goto_user_management()
        assert altermenberinfo.altermenberinfo('13720463070')