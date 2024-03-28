import keyring
import getpass
import requests

class BearerTokenStorage:
    
    def __init__(self, host):
        self.service_name = f"admin.uwm.{host}"
        self.host = host

    def get_key(self):
        """
        Retrieve the key from the keyring. If the key doesn't exist or is expired,
        prompt the user to input a new key.
        """
        key = keyring.get_password(self.service_name, 'access_token')
        if not key or not self.is_key_valid(key):
            key = self.collect_new_key()
        return key
    
    def is_key_valid(self, key):
        """
        Check if the API token is valid by making a test request to the Canvas API.
        """
        url = f"https://{self.host}/api/v1/courses"
        headers = {"Authorization": f"Bearer {key}"}
        response = requests.get(url, headers=headers)
        return response.status_code == 200

    def collect_new_key(self):
        """
        Prompt the user to input a new key.
        """
        while True:
            key = getpass.getpass("Enter new API token: ")
            if key.strip() and self.is_key_valid(key):
                self.store_key(key)
                return key
            else:
                print("Invalid API token. Please try again.")

    def store_key(self, key):
        """
        Store the new key in the keyring.
        """
        keyring.set_password(self.service_name, 'access_token', key)

    def reset_key(self):
        """
        Delete the key from the keyring.
        """
        try:
            keyring.delete_password(self.service_name, 'access_token')
        except:
            pass