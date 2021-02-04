---
title: "Beat the NYT Spelling Bee: Part 2, A front-end app hosted on Streamlit Sharing"
categories:
  - Blog
tags:
  - Deployment
  - Streamlit
  - Python

comments: true
---

[Try out the live app here!](https://share.streamlit.io/mharty3/spelling_bee/app/streamlit_app.py)

In [Part 1](https://mharty3.github.io/blog/spelling-bee/) of this series, I walked through the process of building a RESTful API using Python and Flask. I covered topics like unit testing, continuous integration with GitHub Actions, and deployment to my Raspberry Pi with Docker.

In the last post, I said I would build a front-end app that will make calls to the API. But in the time since I wrote that post, Streamlit, an open source library I have discussed [previously](/blog/streamlit-denver-data-drivers/), released [Streamlit Sharing](https://www.streamlit.io/sharing), a platform for deploying, managing and sharing apps.

With their initial public release last year, Streamlit made it dead simple to make front-end applications. Now, they have made sharing apps on the internet just as easy. The service is free for open source code hosted on GitHub. My spelling bee app seemed like the perfect thing to test out the new platform.

The only addition I had to make to the code was a single file: [streamlit_app.py](https://github.com/mharty3/spelling_bee/blob/master/app/streamlit_app.py), the streamlit app itself. Apart from the logic code I already had, it contains a few streamlit calls to create widgets that get user input and display the results.

Once that file was pushed to GitHub, I went to [share.streamlit.io/deploy](https://share.streamlit.io/deploy), configured three settings, clicked deploy, and the app went live!

![streamlit-deploy-screen](/assets/images/spelling_bee/st-share.png)

Streamlit continues to make things easy that used to be hard.