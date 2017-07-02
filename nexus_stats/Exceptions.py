class NexusException(Exception):
    pass

class ServerException(NexusException):
    pass

class UserNotFound(NexusException):
    pass

class ProfileFieldNotFound(NexusException):
    def __init__(self, field):
        self.field = field
