from pages.main import Main


class TestAddMenber:
    def setup(self):
        self.main = Main()
        # self.main.log().info('开始')

    def test_Add_menber(self):
        add_menber = self.main.goto_user_management()
        add_menber.AddMenber()
        assert add_menber.get_menber('D')
