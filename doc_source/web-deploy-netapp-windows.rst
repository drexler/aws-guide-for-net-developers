.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _web-deploy-netapp-windows:

###################################
Deploying an ASP.NET App to Windows
###################################

.. meta::
    :description: Developing serverless AWS apps with .NET
    :keywords: .net, guide, help, tutorial, serverless, scenarios

You can use the :guilabel:`Publish to Elastic Beanstalk` wizard, provided as part of the
|tvs|, to deploy an application to |eb|. To practice, you can use an instance of a web application starter
project that is built into Visual Studio or you can use your own project.

Create a Sample Web Application Starter Project
===============================================

1. In Visual Studio, choose :guilabel:`File`, :guilabel:`New`,
   :guilabel:`Project`.

2. In the navigation pane of the :guilabel:`New Project` dialog box, expand :guilabel:`Installed`,
   expand :guilabel:`Templates`, expand :guilabel:`Visual C#`, and then choose :guilabel:`Web`.

3. In the list of web project templates, choose any template containing the words :code:`Web` and
   :code:`Application` in its description. For this example, choose :guilabel:`ASP.NET Web Application (.NET Framework)`.

4. In the :guilabel:`Name` box, type :code:`WebAppDemo`. Choose a :guilabel:`Location` and confirm
   that the :guilabel:`Create directory for solution` box is selected. Then choose
   :guilabel:`OK`.

5. In the :guilabel:`New ASP.NET Web Application` dialog box, choose :guilabel:`Web Forms` or
   :guilabel:`MVC`, and then choose :guilabel:`OK`.

   Visual Studio creates a solution and project based on the Application project template you
   selected. Visual Studio then displays the :guilabel:`Solution Explorer`, where the new
   solution and project appear.


Deploy an Application by Using the Publish to Elastic Beanstalk Wizard
======================================================================

1. In :guilabel:`Solution Explorer`, open the context (right-click) menu for the :guilabel:`WebAppDemo` project,
   or open the context menu for the project for your own application, and then choose
   :guilabel:`Publish to AWS Elastic Beanstalk`.

   The :guilabel:`Publish to Elastic Beanstalk` wizard appears.

2. In :guilabel:`Profile`, in the :guilabel:`Account profile to use for deployment` list,
   choose the AWS account profile to use for the deployment. This account profile is
   used only for deployment. You can specify your application credentials separately, if needed.

   Optionally, if you have an AWS account you want to use, but haven't yet created an AWS
   account profile for it, you can choose the plus symbol (:guilabel:`+`) button to add an AWS
   account profile.

3. In the :guilabel:`Region` list, choose the AWS Region to which you want |EB| to deploy the
   application.

4. In :guilabel:`Deployment Target`, choose :guilabel:`Create a new application
   environment`. If you wanted to redeploy a previously deployed application,
   you would choose :guilabel:`Redeploy to an existing environment`.

5. Choose :guilabel:`Next`.

    On the :guilabel:`Application Environment` page, in the :guilabel:`Application` area, the
    :guilabel:`Name` defaults to :guilabel:`WebAppDemo`.

6. In :guilabel:`Environment`, in the :guilabel:`Name` list,
   choose :guilabel:`WebAppDemo-dev`. In this context, the term *environment* refers to the
   infrastructure |EB| provisions for your application.

7. Choose :guilabel:`Check availability` to ensure the default URL domain :guilabel:`EBWebAppDemo-dev`
   for your web application isn't already in use. If it is in use, try other names
   until the requested URL is available.

8. Choose :guilabel:`Next`.

9. In the :guilabel:`Key pair` list, choose an |EC2| instance key pair to use to sign in to
    the instances that will be used for your application. Select :guilabel:`<Create new key pair>`
    and type in a key name. We have used "MyKeyPair" in this example.

    We recommend you launch your instance with a key pair so that you can connect to it with SSH or
    RDP in the future.

10. Ensure :guilabel:`Use non-default VPC`, :guilabel:`Single instance environment`, and
    :guilabel:`Enable Rolling Deployments` are not selected. You can add these options later.

    Optionally, if you have an |RDSlong| database security group with a database you want
    your application to access, select it in the :guilabel:`Relational Database Access`
    list. It will be modified to permit access from the |EC2| instances hosting
    your application.

    Choose :guilabel:`Next`.

12. On the :guilabel:`Permissions` page, choose :guilabel:`Next` to accept the defaults.

13. On the :guilabel:`Applications Options` page, choose :guilabel:`Next` to accept the defaults.

14. On the :guilabel:`Review` page, select :guilabel:`Open environment status window when wizard closes`
    and :guilabel:`Generate AWSDeploy configuration`. Click :guilabel:`Choose`, type in
    :guilabel:`WebAppDemo`, and then choose :guilabel:`Save`.

15. Choose :guilabel:`Deploy` to deploy to |EB|.

    .. note::

       When you deploy the application, the active account will incur charges for the AWS
       resources used by the application.

    Information about the deployment will appear in the Visual Studio status bar and the
    :guilabel:`Events` window of the environment page. It might take several minutes to
    complete the deployment. When complete, you'll see a green INFO event indicating that
    the environment launch succeeded.

    Choose the :guilabel:`URL` to view the website.

Delete an |EBlong| Deployment
=============================

Terminate an environment, delete the app.

You can use the |TVS| to delete a deployment. In AWS Explorer, expand the :guilabel:`Elastic Beanstalk`
node, open the context (right-click) menu for the subnode for the deployment, and then choose
:guilabel:`Terminate Environment`. The termination process might take a few minutes. You can monitor
termination status on the event tab of the environment view.

Once the deployment is terminated, expand the :guilabel:`Elastic Beanstalk`
node in AWS Explorer, open the context (right-click) menu for the subnode for the deployment, and then choose
:guilabel:`Delete`.
