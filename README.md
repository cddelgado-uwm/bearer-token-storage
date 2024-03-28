# bearer-token-storage
Securely store and refresh a token in Python. While this can theoretically be used for any 
bearer token project, it was originally designed as a way to store Canvas LMS API tokens
created from the user's account. 

## Installation
This package can be installed using pip.

```
pip install git+https://github.com/cddelgado-uwm/bearer-token-storage.git
```

## Usage
```
from bearer-token-storage import BearerTokenStorage

# Instantiate
bearer_handler = BearerTokenStorage(HOST)

# Reset a token
bearer_handler.reset_key()

# Get a token
token = bearer_handler.get_key()

# Check if a token is valid
if not bearer_handler.is_key_valid():
    print('Time to update your token')
    bearer_handler.collect_new_key()

# Delete the key
bearer_handler.reset_key()
```

In practice, the class takes care key maintenance by checking and asking without delibrate calls

```
# Instantiates the class and sets a namespace
bearer_handler = BearerTokenStorage(HOST)

# reset a token based on an argument
if args.resettoken:
    bearer_handler.reset_key()

# If the token doesn't work, this will automatically ask for a new token to be inputted
ACCESS_TOKEN = bearer_handler.get_key()
```

## Safe Use
This code is intended for personal development activities and should not be used for
production applications. For production code, use a more secure method to create and
manage tokens such as OAuth2. 
