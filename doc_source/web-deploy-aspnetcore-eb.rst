.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _web-deploy-aspnetcore-eb:

#####################################################
Deploying an ASP.NET Core 2.0 application to |EBlong|
#####################################################

.. meta::
    :description: How to deploy an ASP.NET Core app to |EB|
    :keywords: .net, guide, help, tutorial, serverless, scenarios

You can use the :guilabel:`Publish to AWS Elastic Beanstalk` wizard,
provided as part of the |TVS|, to deploy an ASP.NET Core 2.0 application targeting
Windows to |EB|.

.. _web-deploy-aspnetcore-eb-create-sample:

Create a Sample Web Application Starter Project
===============================================

1. In Visual Studio, choose :guilabel:`File`, :guilabel:`New`,
   :guilabel:`Project`.

2. In the navigation pane of the :guilabel:`New Project` dialog box, expand :guilabel:`Installed`,
   expand :guilabel:`Templates`, expand :guilabel:`Visual C#`, and then choose :guilabel:`Web`.

3. In the list of web project templates, choose :guilabel:`ASP.NET Core Web Application`.

4. In the :guilabel:`Name` box, type :code:`WebAppDemo`, and then choose
   :guilabel:`OK` to go to the next screen.

5. Confirm :guilabel:`NET Core` and :guilabel:`ASP.NET Core 2.0` are selected, and then select
   the :guilabel:`Web Application` application template.

6. Confirm the :guilabel:`Create directory for solution` box is selected. In the :guilabel:`Solution`
   list, confirm :guilabel:`Create new solution` is selected, and then choose
   :guilabel:`OK` to go to the next page.

7. Confirm :guilabel:`NET Core` and :guilabel:`ASP.NET Core 2.0` are selected, and then select
   the :guilabel:`Web Application` application template.


.. _web-deploy-aspnetcore-eb-wiz:

Deploy an ASP.NET Core 2.0 Application Using the Publish to AWS Elastic Beanstalk Wizard
========================================================================================

1. In :guilabel:`Solution Explorer`, open the context (right-click) menu for the :guilabel:`WebAppDemo` project,
   or open the context menu for the project for your own application. Then choose
   :guilabel:`Publish to AWS Elastic Beanstalk`.

   The :guilabel:`Publish to Elastic Beanstalk` wizard appears.

2. In :guilabel:`Profile`, from the :guilabel:`Account profile to use for deployment` list,
   choose the AWS account profile to use for the deployment. This account profile is used
   only for deployment. You specify other credentials separately in the wizard.

   Optionally, if you have an AWS account you want to use, but you haven't yet created an AWS
   account profile for it, you can choose the plus symbol (:guilabel:`+`) button to add an AWS
   account profile.

3. In the :guilabel:`Region` list, choose the AWS Region to which you want |EB| to deploy the
   application.

4. In :guilabel:`Deployment Target`, choose :guilabel:`Create a new application
   environment`. If you wanted to redeploy a previously deployed application, you
   would choose :guilabel:`Redeploy to an existing environment`.

5. Choose :guilabel:`Next`.

    On the :guilabel:`Application Environment` page, in the :guilabel:`Application` area, the
    :guilabel:`Name` defaults to :guilabel:`WebAppDemo`.

7. In the :guilabel:`Environment` area, in the :guilabel:`Name` list,
   choose :guilabel:`WebAppDemo-dev`. In this context, the term *environment* refers to the
   infrastructure |EB| provisions for your application.

8. Choose :guilabel:`Check availability` to ensure the default URL domain :guilabel:`EBWebAppDemo-dev`
   for your web application isn't already in use. If it is in use, try other names
   until the requested URL is available.

9. Choose :guilabel:`Next`.

10. In the :guilabel:`Key pair` list, choose an |EC2| instance key pair to use to sign in to
    the instances that will be used for your application. Select :guilabel:`<Create new key pair...>`
    and type in a key name. We have used "MyKeyPair" in this example.

    We recommend you launch your instance with a key pair so that you can connect to it with SSH or
    RDP in the future.

11. Ensure :guilabel:`Use non-default VPC`, :guilabel:`Single instance environment`, and
    :guilabel:`Enable Rolling Deployments` are not selected. You can add these options later.

    Optionally, if you have an |RDSlong| database security group with a database you want
    your application to access, select it in the :guilabel:`Relational Database Access`
    list. It will be modified to permit access from the |EC2| instances hosting
    your application.

    Choose :guilabel:`Next`.

12. On the :guilabel:`Permissions` page, choose :guilabel:`Next` to accept the defaults.

13. On the :guilabel:`Applications Options` page, choose :guilabel:`Next` to accept the defaults.

14. On the :guilabel:`Review` page, review the options you configured. Choose :guilabel:`Open
    environment status window when wizard closes` and :guilabel:`Save settings to aws-beanstalk-tools-defaults.json
    and configure project for command line deployment`. You can use the settings file
    to make future deployments from the command line using the .NET CLI.

15. If everything looks correct, choose :guilabel:`Deploy`.

    .. note::

       When you deploy the application, the active account will incur charges for the AWS
       resources used by the application.

    Information about the deployment will appear in the Visual Studio status bar and the
    :guilabel:`Events` window of the environment page. It might take several minutes to
    complete the deployment. When the complete, you'll see a green INFO event indicating that the environment
    launch succeeded.

    Choose the :guilabel:`URL` to view the website.

.. _web-deploy-aspnetcore-eb-capacity:

Expand Capacity
===============

Your |EB| environment includes an Auto Scaling group that manages the |EC2| instances in your
environment. In a single-instance environment, the Auto Scaling group ensures that there is
always one instance running. In a load-balanced environment, you configure the group with a
range of instances to run, and |EC2| Auto Scaling adds or removes instances as needed, based
on load.

You can configure how |EC2| Auto Scaling works by editing :guilabel:`Capacity` on the :guilabel:`Auto Scaling`
page for your application in :guilabel:`AWS Explorer`.

1. In Visual Studio 2017, select :guilabel:`View`, and then choose :guilabel:`AWS Explorer`
   if it is not already visible.

2. In AWS Explorer, expand the :guilabel:`Elastic Beanstalk` node, and then double-click the
   node for your application environment. In this example, it's :guilabel:`EBWebAppDemo-dev`.

3. Choose :guilabel:`Auto Scaling`.

4. Configure automatic scaling settings. To ensure there are a minimum of two instances of
   your application running, adjust :guilabel:`Minimum Instance Count` to 2. You can also increase
   or decrease :guilabel:`Maximum Instance Count` to suit demand.

   For more information on auto scaling settings and triggers, see
   :EB-dg:`Auto Scaling Group <using-features.managing.as>`.

5. Choose :guilabel:`Apply Changes`.

.. _web-deploy-aspnetcore-eb-delete:

Delete an AWS Elastic Beanstalk Deployment
==========================================

You can use the |TVS| to delete an application. In :guilabel:`AWS Explorer`, expand the :guilabel:`Elastic Beanstalk`
node, open the context (right-click) menu for the application you want to delete, and then choose :guilabel:`Delete`.

You can also terminate a deployment environment. In :guilabel:`AWS Explorer`, expand the :guilabel:`Elastic Beanstalk`
node, expand the node for your application, open the context (right-click) menu for the environment you want to
terminate, and then select :guilabel:`Terminate Environment`. The termination process might take a few minutes. You can monitor
termination status on the event tab of the environment view.
