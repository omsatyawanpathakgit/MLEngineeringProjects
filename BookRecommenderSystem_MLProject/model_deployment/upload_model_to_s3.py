import boto3
import os
from dotenv import load_dotenv


load_dotenv()


model_path = "../books_recommender_system.pkl"

model_filename = "books_recommender_system.pkl"


bucket_name = "bookrecommendationmodel"

s3_folder = "models_deployed"

s3_key = s3_folder + "/" + model_filename


s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)


s3.upload_file(
    Filename=model_path,
    Bucket=bucket_name,
    Key=s3_key
)


print("Model uploaded successfully to S3!")

print(
    f"S3 Path: s3://{bucket_name}/{s3_key}"
)