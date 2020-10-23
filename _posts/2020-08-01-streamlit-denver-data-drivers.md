---
title: "Intro to Streamlit, a Talk at Denver Data Drivers"
categories:
  - Blog

header:
  teaser: /assets/images/ddd-streamlit/streamlit.PNG
comments: true
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/6T6tLUeF_iw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Earlier this week I had the opportunity to give a talk at the Denver Data Drivers meetup. I covered the Python framework [Streamlit](https://www.streamlit.io). It makes building front-end data applications super easy. If you can write a Python script, then you can build an app.

![streamlit](/assets/images/ddd-streamlit/streamlit.PNG)

In the talk, I gave an overview of the framework and walked step-by-step through building an application for visualizing well logs stored in las files. You can use the finished app here: ([running app](https://streamlit-las-viewer.herokuapp.com/)) ([repo](https://github.com/mharty3/streamlit-las-viewer)). 

The Denver Data Drivers are a group of mostly geologists and engineers in the oil and gas industry who are interested in learning skills related to data-driven decision making. We have been having talks over Webex every week or so over the last few months on a variety of topics in this space.

Here are some of the talks we've had so far:
 * [Amazon Web Services](https://www.youtube.com/watch?v=OZJQk7GaAXc&t=1s) by Mark Bahorich
 * [Python and Google Colab](https://www.youtube.com/watch?v=cV39sK1uCo8&t=1s) by Thomas Martin
 * [SQL](https://www.youtube.com/watch?v=ohnbbOdh-yY) by Mark Ballard
 * [R](https://www.youtube.com/watch?v=qVy8dgS-sDE&t=1s) by Donny Keighley 
 * [Web Scraping](https://www.youtube.com/watch?v=cO8fWCPp_6k&t=8s) by Matt Bauer
 * Random Forests by Alec Walker


Here's a snapshot of the audience for my talk:

![audience word cloud](/assets/images/ddd-streamlit/menti1zoom.png)

## Streamlit

Streamlit claims to be the "fastest way to build data apps," and after trying out several alternatives, I agree. It's very easy to get an app up and running.  It is perfect for building simple apps, prototyping for more complicated applications, and even as an interactive coding environment for data analysis.


I've had a lot of success building Streamlit apps at work and hosting them in Docker containers on a VM for people on my team to use them. I went through a phase at work where I would do some interesting analysis or write some script to automate a task. When I would show it to a co-worker, they would of course ask, "How can *I* use this?" 

For a while, I had no way to share with a non-coder apart from installing Python on their machine (which can be quite a task in a corporate environment where people don't have full admin rights) and teaching them how to use it. This is a lot of work for me, and most people aren't interested in all of that hassle anyway.

In most cases, it only takes a few calls to Streamlit to take an existing script and turn it into an interactive application that can be hosted on the corporate network. To share these apps with co-workers, now all I need to do is send them a link, and they can access the app through their browser.

If you are looking for a way to build simple, user-facing applications in Python, I highly recommend checking out Streamlit.