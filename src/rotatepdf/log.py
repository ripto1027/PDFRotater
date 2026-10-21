class Log:
    __log_count: int = 0

    @staticmethod
    def __build_log(log_type: str, message: str) -> str:
        count: str = f"000{Log.__log_count}"[-3:]
        Log.__log_count += 1
        log_type_upper: str = log_type.upper()
        return f"[{log_type_upper}][{count}] {message}"

    @staticmethod
    def info(message: str) -> None:
        print(Log.__build_log("info", message))

    @staticmethod
    def warn(message: str) -> None:
        print(Log.__build_log("warn", message))

    @staticmethod
    def error(message: str) -> None:
        print(Log.__build_log("error", message))
