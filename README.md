# NitroPay Sponsor Library for Python

## Description

Creates a signed token, for passing user identity to sponsor client library.

## Installation

```console
$ pip install nitropay-sponsor-python
```

## Usage
```python
from nitropay.sponsor import Signer

signer = Signer(private_key)
signed = signer.sign(
    user_id # required
    site_id # required
    name   # optional
    email  # optional
    avatar # optional
)

```

You can also retrieve subscription status for a user with:

```python
signer.getUserSubscription(user_id)
````
