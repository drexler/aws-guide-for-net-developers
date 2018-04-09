.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _web-deploy-ts-aspnet-version:

#############################################
Creating an |eblong| Version in Team Services
#############################################

.. meta::
    :description: How to deploy an ASP.NET Core app to |EB|
    :keywords: .net, guide, help, tutorial, serverless, scenarios

You can use |EBlong| deployment tasks, provided as part of the |TTSLong|,
to build an ASP.NET application to deploy to multiple existing |EB| applications.

.. topic:: To deploy an ASP.NET Application from Team Services to |EB|

1. In Team Services, choose the :guilabel:`Projects` tab. Select the project to deploy,
   and then choose :guilabel:`Build & Release`.

   The process is the same for Visual Studio Team Services.

2. On the :guilabel:`Build Definitions` page, choose :guilabel:`+ New definition`.

3. On the :guilabel:`Select a template` page, choose :guilabel:`ASP.NET`, and then
   choose :guilabel:`Apply`.

4. Add the |EB| deployment task. Choose :guilabel:`Add Task`. In the :guilabel:`Add tasks`
   pane on the right, type :code:`aws` into the search bar, scroll down to
   :guilabel:`AWS Elastic Beanstalk Create Version`, and then choose :guilabel:`Add`.

5. On the :guilabel:`Process` page, choose :guilabel:`AWS Elastic Beanstalk Create Version` to
   configure deployment details. Choose :guilabel:`AWS Credentials`, and then choose credentials
   that the build agent will use to access |EB|.

6. Choose the :guilabel:`AWS Region` for your |EB| deployment.

7. Provide an :guilabel:`Application Name` for the deployment. It must be an existing application.

8. In the :guilabel:`Deployment Bundle Type` list, choose :guilabel:`ASP.NET (Source: Web Deploy Archive)`,
   and then specify the :guilabel:`Web Deploy Archive` location. It's a .zip file named after your
   application. For example :code:`$(build.artifactstagingdirectory)\ContosoUniversity.zip`.

   To find the web deployment archive (the output package) folder, choose :guilabel:`Build Solution`
   in the :guilabel:`Process list`, and then look at :code:`PackageLocation` in the
   :guilabel:`MSBuild Arguments` entry.

9. In the :guilabel:`Version Label` box, type :guilabel:`$(Build.BuildNumber)`. If you don't
   provide a version label, one based on date and time is automatically generated.

10. Choose :guilabel:`Save & queue`. In the :guilabel:`Queue build` dialog box, choose
    :guilabel:`Queue`. You can see task progress in the build console.
