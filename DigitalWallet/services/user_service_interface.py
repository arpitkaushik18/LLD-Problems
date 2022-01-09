import abc

class UserServiceInterface(metaclass=abc.ABCMeta):
   @abc.abstractmethod
   def add_user(self,name):
       pass