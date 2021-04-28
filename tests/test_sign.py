import jwt
from nitropay.sponsor import Signer

def test_sign():
    private_key = "testkey"
    user_id = "0f2feb505b6b4b9895d59acb049e463f"
    site_id = 2
    name = "Tester McTest"
    email = "test@example.com"

    signer = Signer(private_key)
    signed = signer.sign(
        user_id, 
        site_id, 
        name, 
        email
    )
    decoded = jwt.decode(signed, private_key, algorithms=["HS512"])
    assert user_id == decoded["sub"]
    assert site_id == decoded["iss"]
    assert name == decoded["name"]
    assert email == decoded["email"]
    assert "" == decoded["avatar"]
