# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
from CentralLogging import CentralLogging

# Lambda handler triggered by a CloudWatch Event whenever a new log group is created.  Calls the core code to add new subscription to the newly created log group


def lambda_handler(event, context):
    central_logger = CentralLogging()
    print(event)
    print("In add_new_subscription Lambda - requestParameters: ")

    # Retrieves the request parameters from the event that was called to create the log group
    request_parameters = event['detail']['requestParameters']
    print(request_parameters)

    # Extract the log group name from the request parameters to create the log group
    if request_parameters:
        print("     Inspecting request parameters for log_group_name:")
        log_group_name = request_parameters['logGroupName']
        print(log_group_name)

        # Call code to add the subscription to the log group
        central_logger.add_subscription_filter(log_group_name)
