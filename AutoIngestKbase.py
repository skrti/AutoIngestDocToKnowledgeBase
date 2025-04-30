import boto3
import json
import os
import uuid

# Initialize Bedrock Agent client
bedrock_agent = boto3.client('bedrock-agent')

# Environment Variables (set in Lambda console)
KNOWLEDGE_BASE_ID = os.environ.get['KNOWLEDGE_BASE_ID']

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))
    
    # Get bucket and object key from the event
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        s3_uri = f"s3://{bucket}/{key}"
        print(f"Processing file at {s3_uri}")

        try:
            client_token = str(uuid.uuid4())
            # Call Bedrock Knowledge Base API to ingest the file
            response = bedrock_agent.start_ingestion_job(
                knowledgeBaseId='KNOWLEDGE_BASE_ID',
                dataSourceId='DATA_SOURCE_ID',
                clientToken=client_token
            )

            print("Bedrock ingestion response:", json.dumps(response, default=str))
            return {
                'statusCode': 200,
                'body': json.dumps('Document successfully ingested into Bedrock Knowledge Base.')
            }
        
        except Exception as e:
            print("Error:", str(e))
            return {
                'statusCode': 500,
                'body': json.dumps(f'Error processing document ingestion.: {str(e)}')
            }
