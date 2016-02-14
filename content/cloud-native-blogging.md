Title: Cloud Native Blogging
Date: 2016-02-14 14:01
Category: Blog
Tags: Python, Cloud Foundry, PaaS, Pelican
Slug: cloud-native-blogging

I've migrated the blog to run on
[Cloud Foundry](https://www.cloudfoundry.org/) using
[Pelican](http://blog.getpelican.com/) instead of
[Octopress](http://octopress.org/). Pelican is written in Python,
which I am much more fluent in than Ruby. Besides, Pelican supports an
important feature when blogging about data science: You can include
IPython notebooks into blog posts with the
[IPython plugin for Pelican](http://danielfrg.com/blog/2013/03/08/pelican-ipython-notebook-plugin/)
or Jake VanderPlas'
[liquid tags plugin ](https://github.com/jakevdp/pelican-plugins/tree/liquid_tags/liquid_tags
).

With Jake's plugin you can simply write 

    {% literal notebook path/to/notebook.ipynb [cells[i:j]] %}

and Pelican will insert and render the notebook for you.

{% notebook test.ipynb %}

We live in 2016: Setting up and maintaining a webserver for deploying
a website is not necessary anymore in a cloud native world. My PaaS of
choice is [Cloud Foundry](https://www.cloudfoundry.org/) (CF). It is
open source and infrastructure agnostic. That means I can deploy my
blog in seconds to any CF endpoint and not care about any of the
underlying infrastructure.

All I need to do to make this work is to write this short manifest.yml
file:


```yml
---
applications:
- name: everything-counts
  memory: 1024M
  instances: 1
  buildpack: https://github.com/ronert/heroku-buildpack-pelican.git
  timeout: 180
  env:
    PELICAN_SITEURL: "http://everything-counts.cfapps.io"
  domain: ronert-obst.com
```

Everything here should be fairly self-explanatory except the
buildpack
specification.

> [Buildpacks](http://docs.run.pivotal.io/buildpacks/)
provide framework and runtime support for your
applications. Buildpacks typically examine user-provided artifacts to
determine what dependencies to download and how to configure
applications to communicate with bound services.

That is quite a mouthful. Essentially there is a buildpack for every
programming language that is supported by CF. The buildpack fetches
all the dependencies (in the case of Python those specified in your
requirements.txt file) and runs your code for you. Buildpacks are a
very neat abstraction, because they free developers from caring about
any of the underlying infrastructure. The operating system layer is
completely abstracted away, so you can focus on your code.
I use a custom buildpack here since I also need to run Pandoc to
convert my old org-mode blog posts from Octopress to Pelican.

Once I have set up my CF endpoint, I can `cd` into the root of my
blog's directory and then simply run `cf push` and Cloud Foundry will
deploy my blog for me. Cloud Foundry provides some other useful
features I will go into in later posts. Besides health monitoring,
routing and logging, CF can also scale an applications from running on
1 instance to 20 instances in seconds. So if my blog ever goes viral
(very unlikely), I can now simply `cf scale -i 20` it to serve the
millions of new incoming requests.
