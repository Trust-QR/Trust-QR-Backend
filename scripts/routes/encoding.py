import hashlib
import re



def encrypt(data) :
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    encoded_data = sha256.hexdigest()
    return encoded_data




def is_valid_email(email_address):
  regex = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*$"
  match = re.match(regex, email_address)
  return match is not None


def is_strong_password(password):
  regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!?@#$%^&*])[a-zA-Z0-9!?@#$%^&*]{8,}$"
  match = re.match(regex, password)
  return match is not None