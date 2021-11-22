
import jwt
import json
tests = [{"test1": "1", "test2": "2", "token": "token"}]
payload = {"content": tests}
secret_key = "secret_key"
algorithm = "HS256"
encoded_jwt = jwt.encode(payload=payload, key=secret_key, algorithm=algorithm)
print("=======")
print("encoded_jwt")
print(encoded_jwt)
for index, test in enumerate(tests):
    tests[index].update({"token": encoded_jwt})

decoded_jwt = jwt.decode(jwt=encoded_jwt, key=secret_key, algorithm=algorithm)
print("decoded_jwt")
print(decoded_jwt)
print("tests")
print(tests)