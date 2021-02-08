---
title: "Github actions basics and syntax (github_actions)"
---
Github Actions is a continuous integration and continuous deployment platform built into GitHub. It can be used to automate all kinds of workflows like building, testing, and deploying apps, or really anything else you can think of. 

Workflows are defined in YAML files and can be scheduled to run at certain intervals or triggered by events like pull requests or pushes to certain branches.

## Getting started
Create a folder in the root of your repository called `.github/workflows`. This is where all of the workflow instruction yaml files will be stored. Here is an example of workflow YAML syntax that will print "Hello, World!" anytime the repo receives a push.

```yaml
name: hello-world
on: push
jobs:
  my-job:
    runs-on: ubuntu-latest
    steps:
      - name: my-step
        run: echo "Hello, World!"
```

### Key Definitions and Terms
For more details: [see here](https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions#the-components-of-github-actions)

**Workflow** - An automated procedure added to a repo defined using YAML syntax. Workflows are made up of jobs and are scheduled to run at regular intervals or triggered by events. In the example above, the workflow is represented by the entire YAML file.

**Event** - A specific activity that triggers a workflow to run. For a list of potential triggers see [Events that trigger workflows](https://docs.github.com/en/actions/reference/events-that-trigger-workflows). The event in the hello world example is a `push` and defined by `on: push`.

**Job** - A set of steps that are executed on a runner. By default all jobs in a workflow run in parallel, but they can be configured to run sequentially.

**Step** - The individual tasks that make up jobs in a workflow. They can either be an action or a shell command.

**Runner** - A server that runs jobs. They can be hosted by github, or you can use your own. GitHub runners can be based on Ubuntu Linux, Microsoft Windows, and macOS.

**Action** - Standalone commands that are combined into steps to create a job. Actions are the smallest portable building block of a workflow. You can create your own actions, or use actions created by the GitHub community. To use an action in a workflow, you must include it as a step.


## Useful Links

[Getting Started With Github Actions ](https://itnext.io/getting-started-with-github-actions-fe94167dbc6d#7e36)

[Understanding the Workflow File](https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions#understanding-the-workflow-file)

[Events that trigger workflows](https://docs.github.com/en/actions/reference/events-that-trigger-workflows)