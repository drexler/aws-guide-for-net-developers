.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _web-deploy-tfs:

#############################
AWS Tools for .NET Developers
#############################

.. meta::
    :description: Overview of .NET developer scenarios and tools for AWS
    :keywords: .net, guide, help, tutorial, tfs, vsts, aws, credentials


Amazon provides the following tools to help .NET developers work with |awslong|.

|TVSlong|
---------

The |tvs| is a plugin for the Visual Studio IDE that makes it easier for you to develop, debug, and deploy .NET applications
that use Amazon Web Services. The |tvs| provides Visual Studio templates for AWS services and deployment
wizards for web applications and serverless applications. You can use the AWS Explorer to manage |EC2long| instances,
work with |DDBlong| tables, publish messages to |snslong| queues, and more.

And you don't have to leave Visual Studio.

For details about how to download and install the toolkit, see `Setting up the AWS Toolkit for Visual Studio <https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/setup.html>`_.


|TTSlong|
---------

|TTSlong| (VSTS) adds tasks to easily enable build and release pipelines in VSTS and
Team Foundation Server (TFS) to work with AWS services. You can work with |S3|, |AEBlong|,
|CDlong|, |LAMlong|, |CFNlong|, |SQSlong| (|SQS|), and
|SNSlong| (|SNS|). You can also run commands using the Windows PowerShell
module and the AWS CLI. 

To get started with |TTSlong|, see  `AWS Tools for Microsoft Visual Studio Team Services <https://aws.amazon.com/vsts/>`_.


AWS Tools for Windows PowerShell and PowerShell Core
----------------------------------------------------

The |TWPlong| and AWS Tools for PowerShell Core are PowerShell 
modules that are built on the functionality exposed by the AWS SDK for .NET. The AWS 
PowerShell Tools enable you to script operations on your AWS resources from the 
PowerShell command line. Although the cmdlets are implemented using the service clients 
and methods from the SDK, the cmdlets provide an idiomatic PowerShell experience for 
specifying parameters and handling results. 

See `AWS Tools for Windows PowerShell <https://aws.amazon.com/powershell>`_ to get started. You can 
download the tools, check out sample scenarios, and more. You can download AWS Tools for PowerShell Core
from the `PowerShell Gallery <https://www.powershellgallery.com/packages/AWSPowerShell.NetCore>`_.

|sdk-net|
---------

The |sdk-net| makes it easier for Windows developers to build .NET applications that tap in to the
cost-effective, scalable, and reliable AWS infrastructure services such as |S3long|, |EC2long|,
|LAMlong|, and more.

The |sdk-net| supports development on any platform that supports the .NET Framework 3.5 or later.

The |sdk-net| targets .NET Standard 1.3. You can use it with .NET Core 1.x or .NET Core 2.0.

See the `AWS SDK for .NET Developer Guide <https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/welcome.html>`_
to get started.
