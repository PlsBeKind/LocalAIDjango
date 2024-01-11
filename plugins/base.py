```python
from abc import ABC, abstractmethod

class BasePlugin(ABC):
    """
    Base class for all plugins. All plugins should inherit from this class
    and implement the methods.
    """

    @abstractmethod
    def login(self):
        """
        This method should be used to login to the service provided by the plugin.
        """
        pass

    @abstractmethod
    def get_description(self):
        """
        This method should return a description of the plugin.
        """
        pass

    @abstractmethod
    def get_methods_description(self):
        """
        This method should return a dictionary where the keys are the method names
        and the values are the descriptions of the methods.
        """
        pass
```