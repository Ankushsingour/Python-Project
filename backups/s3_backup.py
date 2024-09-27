"""
 thsi is a scipt to taka a backup from local to AWS s3
boto3 --> boto3 is a library in python that useed to do AWS tasks us9ing python
"""

import boto3


import subprocess
try:
    ans = subprocess.check_output(["python", "--version"], text=True)
    print(ans)

except subprocess.CalledProcessError as e:
    print(f"Command failed with return code {e.returncode}")