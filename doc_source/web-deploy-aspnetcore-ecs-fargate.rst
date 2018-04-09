.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _web-deploy-aspnetcore-ecs-fargate:

##############################################
Deploying an ASP.NET Core 2.0 App to |ECSlong|
##############################################

.. meta::
   :description: Deploying ASP.NET Core 2.0 applications to Elastic Container Service with the Fargate launch type.
   :keywords: .net, guide, help, tutorial, Fargate, scenarios, EC2 Container Service, .NET Core, Docker

This section describes how to use the :guilabel:`Publish Container to AWS` wizard,
provided as part of the |TVS|, to deploy a containerized ASP.NET Core 2.0 application targeting
Linux to |ECS| using the Fargate launch type. Because a web application is meant to run continuously,
it will be deployed as a service.

Access the Publish Container to AWS Wizard
==========================================

To deploy an ASP.NET Core 2.0 containerized application targeting Linux, right-click the project
in :guilabel:`Solution Explorer`, and then choose :guilabel:`Publish Container to AWS`.

You can also choose :guilabel:`Publish Container to AWS` on the Visual Studio :guilabel:`Build` menu.

Create a Sample Web Application Starter Project
===============================================

1. In Visual Studio, choose :guilabel:`File`, :guilabel:`New`,
   :guilabel:`Project`.

2. In the navigation pane of the :guilabel:`New Project` dialog box, expand :guilabel:`Installed`,
   expand :guilabel:`Templates`, expand :guilabel:`Visual C#`, and then choose :guilabel:`Web`.

3. In the list of web project templates, choose :guilabel:`ASP.NET Core Web Application`.

4. In the :guilabel:`Name` box, type :code:`WebAppDemo`, and then choose
   :guilabel:`OK` to go to the next page.

5. Confirm :guilabel:`NET Core` and :guilabel:`ASP.NET Core 2.0` are selected, then choose
   the :guilabel:`Web Application` application template.

6. Choose :guilabel:`Enable Docker Support`, choose :guilabel:`Linux` as the operating system, and then choose
   :guilabel:`OK`. Visual Studio 2017 generates the project.

Use the Publish Container to AWS Wizard
=======================================

1. In :guilabel:`Solution Explorer`, open the context (right-click) menu for the :guilabel:`WebAppDemo` project
   folder for the project you created in the previous section, or open the context menu for the
   project folder for your own application, and then choose :guilabel:`Publish Container to AWS`.

   The :guilabel:`Publish Container to AWS...` wizard appears.

2. In :guilabel:`Profile`, in the :guilabel:`Account profile to use for deployment` list,
   choose the AWS account profile to use for the deployment. This account profile is
   used only for deployment. You can specify other credentials separately in the wizard.

   Optionally, if you have an AWS account you want to use, but you haven't yet created an AWS
   account profile for it, you can choose the plus symbol (:guilabel:`+`) button to add an AWS
   account profile.

3. In the :guilabel:`Region` list, choose :guilabel:`US East (N. Virginia)` or
   another `region offering Fargate <https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services>`_.

4. Choose :guilabel:`Service on an ECS Cluster` as the :guilabel:`Deployment Target`. Ensure
   :guilabel:`Save settings to aws-ecs-tools-defaults.json and configure project for command line deployment`
   is selected. You can use the settings file
    to make future deployment from the command line using the .NET CLI.

5. On the :guilabel:`Launch Configuration` page, in the :guilabel:`ECS Cluster` list,
   choose :guilabel:`Create an empty cluster`, and then name the cluster :guilabel:`WebAppDemo`.
   Verify :guilabel:`Launch Type` is set to :guilabel:`FARGATE`.

6. In the :guilabel:`Network Configuration` area, choose :guilabel:`Create New` to create a new
   security group, and then choose :guilabel:`Next`.

7. On the :guilabel:`Service Configuration` page, in the :guilabel:`Service` list,
   choose :guilabel:`Create New`. The wizard provides a default service name.

8. Update the :guilabel:`Number of Tasks` to 2. Each task maps to an instance of your container.
   If one goes down, the other can be available. Choose :guilabel:`Next`

9. On the :guilabel:`Application Load Balancer Configuration` page,
   choose :guilabel:`Configure Application Load Balancer`. In the :guilabel:`Load Balancer` list,
   choose :guilabel:`Create New`. The wizard provides defaults for related fields.
   Choose :guilabel:`Next`.

10. On the :guilabel:`Application Load Balancer Configuration` page, in the :guilabel:`Task Definition`
    list, choose :guilabel:`Create New`. The :guilabel:`Container` list should also be
    set to :guilabel:`Create New`. Accept the default names and other values.

11. Choose :guilabel:`Publish`.

    .. note::

       When you deploy the application, the active account will incur charges for the AWS
       resources used by the application.

    Events are displayed during deployment. The wizard is automatically closed on successful completion. You can override this by unchecking the box at the bottom of the page.

    You can find the URL of your new instances in the AWS Explorer. Expand :guilabel:`Amazon ECS`,
    then expand :guilabel:`Clusters`, and then click on your cluster.
