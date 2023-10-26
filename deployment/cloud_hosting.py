```python
import boto3

def deploy_cloud_hosting():
    # Create a session using your user credentials
    session = boto3.Session(
        aws_access_key_id='YOUR_ACCESS_KEY',
        aws_secret_access_key='YOUR_SECRET_KEY',
        region_name='YOUR_REGION'
    )

    # Create an AWS Lambda client
    lambda_client = session.client('lambda')

    # Specify the details of the Lambda function you want to create
    function_name = 'AutoEmailReplyDrafter'
    runtime = 'python3.8'
    role = 'arn:aws:iam::YOUR_ACCOUNT_ID:role/service-role/YOUR_IAM_ROLE'
    handler = 'backend.data_processing.analyzeEmailChain'
    code = {'ZipFile': open('backend/data_processing.py', 'rb').read()}

    # Create the Lambda function
    response = lambda_client.create_function(
        FunctionName=function_name,
        Runtime=runtime,
        Role=role,
        Handler=handler,
        Code=code,
    )

    # Print the details of the created function
    print(response)

# Call the function to deploy the application on cloud hosting
deploy_cloud_hosting()
```