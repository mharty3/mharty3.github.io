---
title: 'How to avoid SSLError [SSL: CERTIFICATE_VERIFY_FAILED] (pip)'
---
Ignore SSL errors by setting pypi.org and files.pythonhosted.org as trusted hosts.

```
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <package_name>
```

[Stack Overflow Post](https://stackoverflow.com/questions/25981703/pip-install-fails-with-connection-error-ssl-certificate-verify-failed-certi)