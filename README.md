# py-webproxmgr
Web Proxmox API VE manager ( python flask mysql )

Dependencies
------------
* Proxmox VE 4.1
* Python 2.7

---------------

Set environment:

.. code-block:: bash

    $pip install virtualenv
    $export PATH="/home/user/.local/bin:$PATH"
    $virtualenv env
    $pip install proxmoxer
    $pip install proxmox-deploy
    $pip install requests
    $pip install paramiko


* [proxmoxer](https://github.com/swayf/proxmoxer) as Proxmox API client
* [proxmox-deploy](https://github.com/LordGaav/proxmox-deploy)
* `openssh-wrapper`_ for communicating with the Proxmox API and
  executing commands.
* `Jinja2`_ for generating the ``user-data`` and ``meta-data`` files.
* `configobj`_ for reading configuration files.
* `pytz`_ for timezone names.
* ``genisoimage`` (Linux) or ``mkisofs`` (FreeBSD) command.
