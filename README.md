Cloned and altered from: https://github.com/aws-samples/amazon-sagemaker-nlu-search

In backend/template.yaml there is a line like:

    CodeUri: s3://sbert-lambda/lambda.zip

So before creating the stack for the backend, there must exist an s3 bucket named sbert-lambda with a zip file named lambda. This zip file contains only the app.py file (no subfolders!)
