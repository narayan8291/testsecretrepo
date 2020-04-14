if os.getenv("JOB_IS_RUNNING_ON_CI"):
    S3_CLIENT = boto3.client("s3")
else:
    S3_CLIENT = boto3.client(
        "s3",
        aws_access_key_id=" AKIAIOSFODNN7EXAMPLE",  # nosec
        aws_secret_access_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",  # nosec
    )