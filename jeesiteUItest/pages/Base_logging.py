import logging
import os
import time


class Log:

    def __init__(self, name=None):
        self.log_localtion = os.path.dirname(os.path.dirname(__file__)) + "\\result\\log\\" + time.strftime('%Y-%m-%d')
        if not os.path.exists(self.log_localtion):
            os.mkdir(self.log_localtion)
        self.log_name = os.path.join(self.log_localtion, '%s.log' % time.strftime('%m_%d_%H'))
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.formatter =logging.Formatter('[%(asctime)s] - %(name)s - %(levelname)s : %(message)s')

    def _console(self, level, message):
        # 创建一个FileHandler,用于写到本地
        fh = logging.FileHandler(self.log_name, "a", encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == "info":
            self.logger.info(message)
        elif level == "debug":
            self.logger.debug(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()

    # def ospath_writer(self):
    #     print(os.path.dirname(os.path.dirname(__file__))+ "\\result\\log\\" + time.strftime('%Y-%m-%d'))

    def debug(self, message):
        self._console("debug", message)

    def info(self, message):
        self._console("info", message)

    def warning(self, message):
        self._console("warning", message)

    def error(self, message):
        self._console("error", message)


if __name__ == '__main__':
    log = Log('aaa')
    # log._console('info', '第一次尝试')
    # log.ospath_writer()
    log.info("这是info")
    log.debug("这是debug")
    log.error('第二次尝试')