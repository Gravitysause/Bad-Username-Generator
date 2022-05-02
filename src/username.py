import requests

class Username:
    def __init__(self):
        self.__username = self.set_username()

    def set_username(self):
        """
        Retrieves an adjective from https://random-word-form.herokuapp.com/random/adjective and noun from https://random-word-form.herokuapp.com/random/noun
        combines them with a line in the middle.


        Example(s)
        ----------
        For the examples, "un" will represent an instance of Username.

        1.
        >>> un.set_username()
        >>> print(un.get_username())
        Big_Chungus

        2. 
        >>> print(un.get_username())
        Grey_Car
        >>> un.set_username()
        >>> print(un.get_username())
        Saucy_Apple
        """
        adjective = requests.get("https://random-word-form.herokuapp.com/random/adjective").text[2:-2]
        noun = requests.get("https://random-word-form.herokuapp.com/random/noun").text[2:-2]
        
        return f"Xx{adjective}_{noun}xX"

    def get_username(self):
        """
        Returns the username.

        Parameters
        ----------
        None

        Returns
        -------
        self.__username : str
        """
        
        return self.__username

username = Username()
print(username.get_username())
