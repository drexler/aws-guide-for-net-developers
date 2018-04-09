
   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _web-connecting-windows:

#################################
Connecting to Your Linux instance
#################################

.. meta::
    :description: Installing AWS VSTS and TFS toolkit and configuring credentials for AWS
    :keywords: .net, guide, help, tutorial, tfs, vsts, aws, credentials

You can connect to your Linux instance within Visual Studio by using the |tvs|.

The |tvs| uses the SSH client Putty to connect to |EC2| instances. It's a free
SSH client available from `https://www.chiark.greenend.org.uk/~sgtatham/putty/ <https://www.chiark.greenend.org.uk/~sgtatham/putty/>`_.

.. topic:: To connect to your Linux instance

1. In :guilabel:`AWS Explorer`, expand :guilabel:`Instances` under :guilabel:`Amazon EC2`,
   right-click your Linux instance, and then choose :guilabel:`Open SSH Session`.

2. In the :guilabel:`Open SSH Session` dialog box, choose :guilabel:`Use EC2 keypair to log on`
   to use a keypair associated with the instance.

   If the keypair isn't stored in the |tvs|, you can copy the private key for the
   instance and paste it in the :guilabel:`Private Key` box. Choose
   :guilabel:`Save Private Key` to save the private key to the |tvs|. It will be
   associated with the instance and used for future connections.

   You can also use a password. Choose :guilabel:`Enter password` and type
   in the password for the instance. To save your credentials,
   choose :guilabel:`Save Credentials`. Your credentials will be used for
   future connections.

3. Verify the :guilabel:`Location of Putty`.

4. Choose :guilabel:`OK` to connect.

   A Putty window opens and you are connected.

   If you experience problems connecting, see
   `Troubleshooting Connecting to Your Instance <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.html>`_.
