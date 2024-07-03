
class Utils:
    @staticmethod
    def del_prefix(string:str, prefix="NEW-"):
        if string.startswith(prefix):
            string = string.removeprefix(prefix)
        return string
