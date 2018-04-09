.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _web-sql-server-paramstore:

##################################
Using Encrypted Connection Strings
##################################

.. meta::
   :description: Overview of .NET developer scenarios for AWS
    :keywords: .net, guide, help, tutorial, develop, scenarios

AWS Systems Manager provides a centralized store to manage your configuration data, whether plain-text
data such as database strings or secrets such as passwords. This enables you to separate your secrets and
configuration data from your code. Parameters can be tagged and organized into hierarchies, helping you
manage parameters more easily. For example, you can use the same parameter name, "constr", with a
different hierarchical path, "/MyWebApp/Development/constr" or "/MyWebApp/Production/constr", to store
different values. Values can be encrypted and you can control user and resource access.

If your |IAM| user account, group, or role is assigned administator permissions, you have access
to Systems Manager. If you don't, an administrator must update your |IAM| account, group,
or role.

Create an Encrypted Connection String
======================================

To create an encrypted SQL Server connection string using the |console|:

1. Open https://console.aws.amazon.com/systems-manager/, and under :guilabel:`Shared Reources` in the navigation pane,
   choose :guilabel:`Parameter Store`.

2. Choose :guilabel:`Create Parameter`.

3. In the :guilabel:`Name` box, type a hierarchy and a name. You can use the hierarchy to
   create a unique connection string for different deployment environments. For example,
   :code:`/MyWebApp/Development/constr`, :code:`/MyWebApp/Test/constr`, and :code:`/MyWebApp/Production/constr`.

4. Provide a guilabel:`Description`. For example,
   :code:`Dev environment SQL Server connection string.`

5. Select :guilabel:`Secure String`.

6. Type in the SQL Server connection string. At a minimum, you will usually specify :code:`server`,
   :code:`initial catalog`, :code:`user id`, and :code:`password` in the connection string. For example,
   :code:`server=myserver.com;Initial Catalog=mydb;User ID=myid;Password=mypwd`.

7. Choose :guilabel:`Create parameter`.

You can also create a parameter and perform other operations using |PSTlong|.

.. code-block:: cli

   # Create a new connection string; returns parameter version
   Write-SSMParameter -Name "/MyWebApp/Development/constr" -Value "server=<server>;initial catalog=<db>;user id=<id>;password=<pwd>" -Type SecureString -Overwrise $true

   # Retrieve all the keys for this app
   Get-SSMParametersByPath -Path "/MyWebApp" -Recursive $true

   # Get latest version of a parameter
   Get-SSMParameter -Name "/MyWebApp/Development/constr"

   # Get version of a parameter
   Get-SSMParameter -Name "/MyWebApp/Development/constr:1"

   # Get parameter value with decryption
   Get-SSMParameter -Name "/MyWebApp/Development/constr" -WithDecryption $true

To learn more about |PST|, see XXX.

.. _web-sql-server-paramstrore-code:

Read the Encrypted Connection String from .NET
==============================================

You can get the value from Parameter Store by using the |sdk-net|.

.. code-block:: c#

   // Add the AWSSDK.SimpleSystemsManagement NuGet package to your project
   using Amazon.SimpleSystemsManagement;
   using Amazon.SimpleSystemsManagement.Model;

   class DbHelper
   {
       public static string GetDBConnectionString()
       {
           // The parameter name is customized based on the ASPNETCORE_ENVIRONMENT
           //
           // You can change this to a fixed string or use a different mechanism
           // to customize.
           String parameterName = String.Format("/MyWebApp/{0}/constr", Environment.GetEnvironmentVariable("ASPNETCORE_ENVIRONMENT"));

           // Using USEast1
           var ssmClient = new AmazonSimpleSystemsManagementClient(Amazon.RegionEndpoint.USEast1);
           var response = ssmClient.GetParameter(new GetParameterRequest
           {
               Name = parameterName,
               WithDecryption = true
           });
           return response.Parameter.Value;
       }
   }
