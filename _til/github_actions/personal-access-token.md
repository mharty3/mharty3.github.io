---
title: "Allow workflows to interact with other repos using Personal Access Tokens (github_actions)"
---
When running a workflow, the workflow has the rights to read, push, and commit changes to the repository that's running it. But what if your workflow needs to make changes to a different repository? In this case, you will need to provide a [Personal Access Token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) or PAT. The PAT is a way to authenticate yourself without using your password.

## Create the Token
Create the token following the [instructions on Github](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).

You can customize the scope of permissions available to the token and create multiple tokens with different levels of permissions. 

Once you generate the PAT, treat it as a password and save it in a save space. I keep mine in my password manager's vault.

## Add the token to the repository secrets
To allow the workflow to use the PAT, you need to add it to the repository's secrets. These are secure environment variables that can be accessed by the workflow. To add it, go to your repo's settings, select `Secrets`, and click `New Repository Secret`. Give your secret a name, like `PAT_FOR_PUSH` and paste the PAT in the box.

## Using the PAT in a workflow
In the workflow YAML file, you access repository secrets like this: `${{ secrets.PAT_FOR_PUSH }}`


```yaml
- name: Checkout other_repo
      uses: actions/checkout@v2
      with:
        repository: mharty3/other_repo
        path: til-db
        token: ${{ secrets.PAT_FOR_PUSH }}
```