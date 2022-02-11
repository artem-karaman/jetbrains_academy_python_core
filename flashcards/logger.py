from io import StringIO


class Logger:
    def __init__(self):
        # write data to memory buffer https://docs.python.org/3/library/io.html#io.StringIO
        self.logger = StringIO()

    def logged_input(self, promt=""):
        _in = "INPUT"
        _input = input(promt)
        self.logger.write(f'{_in}: {_input}\n')
        return _input

    def print_and_log(self, *args, **kwargs):
        _out = "OUTPUT"
        # print to sys.stdout
        print(*args, **kwargs)
        # print to log file
        print(_out, *args, **kwargs, file=self.logger, sep=': ')

    def save_logs(self):
        logger_file = self.logged_input("File name:\n")
        with open(logger_file, "w") as log_file:
            for log_value in self.logger.getvalue():
                log_file.write(log_value)
        print("The log has been saved.")
