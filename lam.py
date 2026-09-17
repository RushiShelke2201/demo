Search for Lambda->Create function->Author from scratch->Function name:my-lambda-s3-function->Runtime:Python 3.11->Create function
Code: Remove the existing code and copy and paste the code from the next slide->Deploy
Configuration->Permissions->Click on the Execution role name link->Add permissions->Attach policies->Search for S3->Select AmazonS3FullAccess ->Add permission
Go to Lambda->Triggers->Add Trigger->Select a source: S3->Bucket:Select your bucket->Leave everything else as default->Acknowledge->Add
In S3, Click on the Bucket name->Properties->Scroll down->Event notifications will show our Lambda event


Go to S3 Bucket and upload 2-3 files
Go to Lambda->Monitor->View CloudWatch logs->Scroll down to Log streams->Click on the URL
We should see the logs for the uploaded files

Remove all objects from the S3 bucket
Remove S3 bucket
Remove Lambda function


import boto3
import urllib.parse

s3 = boto3.client('s3')
target_bucket_name = 'YOUR_TARGET_BUCKET_NAME'  # Replace with your target bucket name

def lambda_handler(event, context):
    source_bucket_name = ‘YOUR_SOURCE_BUCKET_NAME’
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    try:
        copy_source = {'Bucket': source_bucket_name, 'Key': key}
        s3.copy(copy_source, target_bucket_name, key)
        print(f"Successfully copied {key} from {source_bucket_name} to {target_bucket_name}")
    except Exception as e:
        print(f"Error copying {key}: {e}")
        raise e
