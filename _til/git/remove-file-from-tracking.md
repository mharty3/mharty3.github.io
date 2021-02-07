---
Stop tracking a file in version control
---
# Stop tracking a file in version control (git)
If you want to stop tracking a file (ie remove it from version control) while keeping it in the repository, run the following command on the file. Sometimes I need this when I accidentally commit files in a directory before I set up the .gitignore files.

`git rm --cached <file-name>`

[Stack Overflow](https://stackoverflow.com/questions/936249/how-to-stop-tracking-and-ignore-changes-to-a-file-in-git)