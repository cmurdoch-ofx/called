import os


secret_token = os.getenv('SECRET_TOKEN', 'Unable to get')
secret_user = os.getenv('SECRET_USER', 'Unable to get')
json_input = os.getenv('JSON_INPUT', 'Unable to get')


def main():
    if secret_token is not None:
        print("hey we passed the token through")
        print(secret_token)
    if secret_user is not None:
        print("hey we passed the user")
        print(secret_user)
    if json_input is not None:
        print("Hey we got the input too")
        print(json_input)
    else:
        print("we didn't get anything")


if __name__ == "__main__":
    main()
