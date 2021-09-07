from pages.Base_logging import Log
from pages.main import Main


class TestQueryMenber:
    def setup(self):
        self.main = Main()

    def test_query_menber(self):
        query_menber = self.main.goto_user_management()
        assert query_menber.querymenber("正常")