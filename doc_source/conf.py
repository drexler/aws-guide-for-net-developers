# -*- coding: utf-8 -*-
#
# AWS Sphinx configuration file.
#
# For more information about how to configure this file, see:
#
# https://w.amazon.com/index.php/AWSDevDocs/Sphinx
#

#
# General information about the project.
#

# The long version of the service or SDK name, such as "Amazon Simple Workflow
# Service", "AWS Flow Framework for Ruby" or "AWS SDK for Java"
service_name_long = u'AWS .NET SDK'
service_docs_home = u'http://aws.amazon.com/documentation/sdk-for-net/'

project = u'AWS Guide for .NET Developers'
project_desc = u'AWS Guide for .NET Developers'
project_basename = u'sdk-for-net/ndg'

# This name is used as the manual / PDF name. Don't include the extension
# (.pdf) here.
man_name = u'aws-net-ndg'

# Optional forum ID. If there's a relevant forum at forums.aws.amazon.com, then
# set the ID here. If not set, then no forum ID link will be generated.
forum_id = u'0'

# For the url docs.aws.amazon.com/docset-root/version/guide-name
docset_path_slug = u'sdk-for-net'
version_path_slug = u'v3'
guide_path_slug = u'ndg'

build_html = True
build_pdf = True
build_mobi = False #Or the Kindle ASIN if you need a Kindle build

feedback_folder_id = u'bce16e71-f8fd-4d40-a778-c5c5ece46bd2'

extra_navlinks = []

# The link to the top of the doc source tree on GitHub. This allows generation
# of per-page "Edit on GitHub" links.
github_doc_url = 'https://github.com/awsdocs/aws-guide-for-net-developers/tree/master/doc_source'

# EXTRA_CONF_CONTENT -- don't change, move or remove this line!
