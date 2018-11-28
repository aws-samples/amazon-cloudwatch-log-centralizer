## Amazon CloudWatch Log Centralizer

Centralized logging infrastructure for multiple AWS accounts using CloudFormation and Python

## License Summary

This sample code is made available under a modified MIT license. See the LICENSE file.

## Overview
Please see the AWS Architecture Blog (https://aws.amazon.com/blogs/architecture/) article _Stream Amazon CloudWatch Logs to a Centralized Account for Audit and Analysis_ for instructions and more context.

While some AWS customers use the built-in ability to push Amazon CloudWatch Logs directly into Amazon Elasticsearch Service for analysis, others would prefer to move all logs into a centralized Amazon Simple Storage Service (Amazon S3) bucket location for access by custom and third-party tools. Setting up this solution assumes some knowledge of CloudFormation, Python3 and the boto3 AWS SDK.

You will need to have or configure an AWS working account and logging account, an IAM access and secret key for those accounts, and a working environment containing Python and the boto3 SDK. For assistance, see the Getting Started Resource Center at https://aws.amazon.com/getting-started/ and Start Building with SDKs and Tools at https://aws.amazon.com/getting-started/tools-sdks/.
