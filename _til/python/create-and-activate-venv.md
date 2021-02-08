---
title: "Create and activate a virtual environment in Python (python)"
---
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Whosoever makes a static webpage that just has two things on it:<br><br>1. Unix/Mac/Windows command for creating a new venv environment<br>2. Unix/Mac/Windows command for activating new venv environment<br><br>will achieve super-high search rankings almost instantaneously.</p>&mdash; Vicki Boykis (@vboykis) <a href="https://twitter.com/vboykis/status/1181381908493672449?ref_src=twsrc%5Etfw">October 8, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 


https://venv.netlify.app/

Bash code:
```
cd project_folder
python -m venv venvname
source venvname/bin/activate 
```


Activating the venv in other shells ([see here](https://docs.python.org/3/library/venv.html)):

<table class="docutils align-default">
<colgroup>
<col style="width: 18%">
<col style="width: 24%">
<col style="width: 58%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Platform</p></th>
<th class="head"><p>Shell</p></th>
<th class="head"><p>Command to activate virtual environment</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>POSIX</p></td>
<td><p>bash/zsh</p></td>
<td><p>$ source &lt;venv&gt;/bin/activate</p></td>
</tr>
<tr class="row-odd"><td></td>
<td><p>fish</p></td>
<td><p>$ source &lt;venv&gt;/bin/activate.fish</p></td>
</tr>
<tr class="row-even"><td></td>
<td><p>csh/tcsh</p></td>
<td><p>$ source &lt;venv&gt;/bin/activate.csh</p></td>
</tr>
<tr class="row-odd"><td></td>
<td><p>PowerShell Core</p></td>
<td><p>$ &lt;venv&gt;/bin/Activate.ps1</p></td>
</tr>
<tr class="row-even"><td><p>Windows</p></td>
<td><p>cmd.exe</p></td>
<td><p>C:\&gt; &lt;venv&gt;\Scripts\activate.bat</p></td>
</tr>
<tr class="row-odd"><td></td>
<td><p>PowerShell</p></td>
<td><p>PS C:\&gt; &lt;venv&gt;\Scripts\Activate.ps1</p></td>
</tr>
</tbody>
</table>