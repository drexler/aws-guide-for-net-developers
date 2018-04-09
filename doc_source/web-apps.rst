.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _web-apps:

################
Web Applications
################

.. meta::
    :description: Hosting .NET applications on AWS
    :keywords: .net, guide, help, tutorial, hosting, scenarios

|AWSlong| offers cloud web hosting solutions for delivering websites and web applications.
AWS provides development support for .NET and other popular platforms, has data centers
worldwide, and can dynamically grow and shrink resources with fluctuating website traffic.
With flexible pricing models, AWS only charges you for the resources you use.

Types of Websites
==================

Static Website Hosting
----------------------

Static websites deliver HTML, JavaScript, images, video, and other files to your website visitors. They
contain no server-side application code, like ASP.NET or PHP. They typically are used to
deliver personal or marketing sites. ASP.NET and ASP.NET Core web applications typically
require simple or enterprise website hosting.

Consider using static website hosting when your website doesn't contain server-side
scripting, changes infrequently, and needs to scale for intervals of high traffic. Static
websites are best for customers who don't want to manage infrastructure.

Simple Website Hosting
----------------------

Simple websites typically consist of a single Linux, Unix, or Windows web server with a development
stack, such as ASP.NET. They provide a simple starting point for a website that might grow in
the future. Simple websites require IT administration of the web server and aren't built
to be highly available or scalable beyond a few servers.

Consider using simple website hosting when your website is unlikely to scale beyond five servers,
and you want to manage your own web server and resources.

Enterprise Website Hosting
--------------------------

Enterprise websites use multiple servers and AWS services and often span multiple data centers
(or Availability Zones). They dynamically scale resources based on demand and need to be
highly available. There are often different development stacks used for different portions
of the application.

Consider using enterprise website hosting when your website needs web servers across at least two
data centers, needs to scale, or requires sustained high CPU utilization. Enterprise
website hosting is great for those who need maximum control and flexibility configuring and
administrating their web server.

.. toctree::
   :titlesonly:
   :maxdepth: 1

   web-apps-selecting-deployment-option
   web-deploy-vs
   web-deploy-ts
   web-connecting-to-instance
   web-sql-server
   web-dynamodb
