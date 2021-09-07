from pages.main import Main


class TestDeleteMenber:
    def setup(self):
        self.main = Main()

    def test_delete_menber(self):
        delete_menber = self.main.goto_user_management()
        assert delete_menber.deletemenber('huqingwei')