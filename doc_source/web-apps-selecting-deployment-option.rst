.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _web-apps-selecting-deployment-options:

#####################################
Choosing Where to Deploy Your Web App
#####################################

.. meta::
   :description: Overview of .NET developer scenarios for AWS
    :keywords: .net, guide, help, tutorial, develop, scenarios

You have several deployment options on |AWSlong|. You can choose the mostly automatic approach,
answering a few initial configuration questions and letting AWS do the rest.
Or you can choose to go hands on and fully configurable, adjusting DNS,
automatic scalers, and other aspects of your deployment environment.


|EBlong|
========

|EBlong| is an easy-to-use service for deploying and scaling web applications
developed with .NET.

Simply deploy your application, and |EB| automatically handles the details of deployment provisioning,
load balancing, scaling, and application health monitoring. You retain full control over
the AWS resources powering your application, and can access the underlying resources at any time.

|EB| supports several platforms for different versions of the .NET programming framework and 
Windows Server. It also supports Docker containers.

|ECSlong|
=========

|ECSlong| is a highly scalable, high-performance container management service that makes
it easy to run, manage, and stop Docker containers on a cluster of |EC2| instances.

|ECS| is a good option if you have a containerized .NET Core application.

|LAMlong|
=========

|LAMlong| enables you to run .NET Core functions or serverless applications without provisioning or
managing servers. You get flexible scaling and high availability, and have no
idle capacity because there is no charge when your code isn't running.

|LAM| is a good option if you want to really benefit from serverless computing.
