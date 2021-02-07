---
title: 'Set vertical rulers for git commit messages in vs code (vs_code)'
---
Git commit messages follow a style where the first line should be less than 50 characters and the rest of the lines should be less then 72 characters. You can add a setting to the vscode `settings.json` file to set vertical rulers when writing commit messages.

Add this to the settings.json file.

```
"[git-commit]": {
    "editor.rulers": [72, 50],
    "editor.wordWrap": "off"
```

If vs code is your default editor for git, then typing `git commit` in the terminal will open a new tab in vs code with the rulers in place.