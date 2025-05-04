Auto-Ingest Documents to Bedrock KnowledgeBase via S3 Uploads

A serverless solution that automatically ingests documents into an Amazon Bedrock Knowledge Base whenever new files are uploaded to an S3 bucket — enabling real-time updates for GenAI-powered applications like a Service Desk Bot.
This helps the bot stay up to date by syncing customer issues from auto-recorded phone calls, making the knowledge base dynamically responsive as issues evolve — no manual updates required!

🔧 How It Works:
A new file is uploaded to an S3 bucket.
An S3 event notification triggers a Lambda function, which invokes Amazon Transcribe to convert the podcast into text and store in S3 bucket.
The Lambda function uses Bedrock Knowledge Base APIs to ingest the file automatically.
Upon successful ingestion, a confirmation is sent via SNS.
This removes manual intervention and enables continuous learning for the chatbot — making it smarter with each update.

🛠️ Tech Stack:
Amazon S3 – Stores files
Lambda – Automates file ingestion
Amazon Transcribe - To convert audio into text and make it readable
Amazon Bedrock Knowledge Base – Stores and indexes knowledge
API Gateway – Secures API access
SNS – Sends ingestion status notifications
IAM Roles & Policies – Provides secure permissions


