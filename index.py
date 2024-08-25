import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

iam = boto3.client('iam')

def create_iam_user(user_name):
    try:
        response = iam.create_user(UserName=user_name)
        print(f"User '{user_name}' created successfully.")
    except Exception as e:
        print(f"Error creating user: {e}")

def list_iam_users():
    try:
        response = iam.list_users()
        if not response['Users']:
            print("No IAM users found.")
        else:
            print("IAM Users:")
            for user in response['Users']:
                print(f"  - {user['UserName']}")
    except Exception as e:
        print(f"Error listing users: {e}")

def delete_iam_user(user_name):
    try:
        iam.delete_user(UserName=user_name)
        print(f"User '{user_name}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting user: {e}")

def attach_policy_to_user(user_name, policy_arn):
    try:
        iam.attach_user_policy(UserName=user_name, PolicyArn=policy_arn)
        print(f"Policy '{policy_arn}' attached to user '{user_name}' successfully.")
    except Exception as e:
        print(f"Error attaching policy: {e}")


create_iam_user('new-user')


list_iam_users()

policy_arn = 'arn:aws:iam::aws:policy/AmazonS3FullAccess'
attach_policy_to_user('new-user', policy_arn)


delete_iam_user('new-user')
