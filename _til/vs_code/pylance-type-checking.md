---
Enabling the type checking feature in vscode
---
# Enabling the type checking feature in vscode (vs_code)
The Pylance extension has many tools for helping write Python better and faster. By defalult, it's type checking functionality is turned off.

There are three options you can set it to: off, basic, and strict. Each has increasing levels of severity. 

Change the vs code settings with the interactive dialog in the application, or add the following lines to your settings json file with your desired level of strictness.

`"python.analysis.typeCheckingMode": "basic"`