from plugins.base import PluginBase

class SpotifyPlugin(PluginBase):
    def __init__(self):
        self.name = "spotify"
        self.description = "Spotify music streaming service"
        self.methods = {
            "login": {
                "description": "authorizes the spotify api with the users account",
                "function": self.login
            },
            # Add more methods as needed
        }

    def login(self):
        # Implement the login functionality here
        pass

    def handle_error(self, error):
        if "not logged in" in str(error):
            self.methods["login"]["function"]()

    def execute(self, command):
        for method, details in self.methods.items():
            if command in details["description"]:
                try:
                    details["function"]()
                except Exception as e:
                    self.handle_error(e)
                    details["function"]()