from pages.main import Main


class Testloganscreen:
    _base_url = 'https://www.baidu.com'

    def setup(self):
        self.main = Main()

    def test_find_error(self):
        self.main.finderror()
        assert True

