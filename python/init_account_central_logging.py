#!/usr/bin/env python

# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from __future__ import print_function, absolute_import
import boto3
from CentralLogging import CentralLogging


def add_log(destination_arn):
    central_logger = CentralLogging()
    # Initializes the account for centralized logging by adding the logging destination to the Parameter Store and then adding a subscription to the destination for each existing log group

    # Create an SSM SDK client to handle Parameter Store actions
    ssm_client = boto3.client('ssm')

    # Put the destination (currently hard-coded and needs to be changed if the destination ever changes) into the Parameter Store
    destination_response = ssm_client.put_parameter(
        Name='LogDestination',
        Description='Centralized logging account destination ARN for subscription filters',
        Value=destination_arn,
        Type='String',
        Overwrite=True
    )

    print(destination_response)
    # Call the code to add a subscription to all existing log groups
    central_logger.add_subscriptions_to_existing_log_groups()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--destination", help="logs:destination ARN to send logs to")

    args = parser.parse_args()
    if(args.destination):
        add_log(args.destination)
    else:
        parser.print_help()
        raise ValueError('Must provide LogDestination ARN. See help')
