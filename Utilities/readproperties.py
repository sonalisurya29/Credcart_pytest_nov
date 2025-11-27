import configparser

config = configparser.RawConfigParser()
config.read("F:\\Sonali\\python revision nov\\Pytest_credframework\\Configuration\\config.ini")


class Readconfig():

    @staticmethod
    def getLoginUrl():
        LoginUrl = config.get('user info', 'loginUrl')
        return LoginUrl

    @staticmethod
    def getRegistrationUrl():
        RegistrationUrl = config.get('user info', 'RegistrationUrl')
        return RegistrationUrl

    @staticmethod
    def getname():
        Name = config.get('user info', 'name')
        return Name

    @staticmethod
    def getUsername():
        Username = config.get('user info', 'User_email')
        return Username

    @staticmethod
    def getPassword():
        Password = config.get('user info', 'Password')
        return Password

    @staticmethod
    def getConfirmPassword():
        ConfirmPassword = config.get('user info', 'ConfirmPassword')
        return ConfirmPassword
