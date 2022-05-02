import requests

class Username:
    def __init__(self):
        self.__username = self.set_username()

    def set_username(self):
        """
        Retrieves an adjective from https://random-word-form.herokuapp.com/random/adjective and 
        noun from https://random-word-form.herokuapp.com/random/noun.
        
        The program then combines them into "Xx{adjective}_{noun}xX".

        Example(s)
        ----------
        For the examples, "un" will represent an instance of Username.

        1.
        >>> un.set_username()
        >>> print(un.get_username())
        XxBig_ChungusxX

        2. 
        >>> print(un.get_username())
        XxGrey_CarxX
        >>> un.set_username()
        >>> print(un.get_username())
        XxSaucy_ApplexX

        Parameters
        ----------
        None

        Returns
        -------
        "Xx{adjective}_{noun}xX" : str
            This is the newly generated username
        """

        adjective = requests.get("https://random-word-form.herokuapp.com/random/adjective").text[2:-2]
        noun = requests.get("https://random-word-form.herokuapp.com/random/noun").text[2:-2]
        
        return f"Xx{adjective}_{noun}xX"

    def get_username(self):
        """
        Returns the username.

        Example(s)
        ----------
        For the examples, "un" will represent an instance of Username.
        
        1.
        >>> print(un.get_username())
        Xxdescriptive_wordxX

        2.
        >>> print(un.get_username())
        Xxwordy_textxX
        >>> un.set_username()
        >>> print(un.get_username())
        Xxnewer_wordxX

        Parameters
        ----------
        None

        Returns
        -------
        self.__username : str
            The username
        """
        
        return self.__username

username = Username()
print(username.get_username())
