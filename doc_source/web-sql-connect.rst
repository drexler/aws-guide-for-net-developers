.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _web-sql-server-connect:

###################################
Connecting to a SQL Server Instance
###################################

.. meta::
   :description: Overview of .NET developer scenarios for AWS using SQL Server
    :keywords: .net, guide, help, tutorial, SQL Server, connect, develop, scenarios

You can connect to an existing SQL Server instance using :guilabel:`Server Explorer` and the
|tvs| in Visual Studio.

.. note::

   If your machine is behind a proxy/firewall, you might need to contact your network administrator.

In this procedure you connect to your sample DB instance by using |tvs| and Visual Studio
:guilabel:`Server Explorer`.

.. topic:: To connect to a SQL Server instance in Visual Studio

1. In :guilabel:`AWS Explorer`, expand the :guilabel:`Amazon RDS` node and the :guilabel:`Instances`
   node. Right-click your DB instance, and then choose :guilabel:`Add to Server Explorer`.

   If the |tvs| cannot connect, the :guilabel:`Unable to Connect` dialog box is  displayed. The dialog box
   gives you the option of adding your current CIPR/IP to the DB instance security group.
   Choose :guilabel:`OK` to add or :guilabel:`Cancel` to exit.

   If you cannot connect, you might need to contact your network network administrator.

2. In the :guilabel:`Add Connection` dialog box, choose :guilabel:`SQL Server Authentication` in
   the :guilabel:`Authentication` list, and then type your :guilabel:`User name` and
   :guilabel:`Password`.

3. To connect to a specific database, in the :guilabel:`Select or enter a database name`
   list, choose a database.

4. Choose :guilabel:`OK` to connect.
