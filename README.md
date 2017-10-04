# py-webproxmgr
Web Proxmox API VE manager ( python flask mysql )

Dependencies:

------------

* Proxmox VE 4.1
* Python 2.7
* [Flask](http://flask.pocoo.org/)

------------

* [proxmoxer](https://github.com/swayf/proxmoxer) as Proxmox API client
* [proxmox-deploy](https://github.com/LordGaav/proxmox-deploy)
* `openssh-wrapper`_ for communicating with the Proxmox API and
  executing commands.
* `Jinja2`_ for generating the ``user-data`` and ``meta-data`` files.
* `configobj`_ for reading configuration files.
* `pytz`_ for timezone names.
* ``genisoimage`` (Linux) or ``mkisofs`` (FreeBSD) command.

-------------

Set environment:

    $pip install virtualenv
    $export PATH="/home/user/.local/bin:$PATH"
    $virtualenv env
    $pip install proxmoxer
    $pip install proxmox-deploy
    $pip install requests
    $pip install paramiko

-----------

Deploy:

    $ssh-copy-id root@proxmox-host-ip
    $mkdir images
    $cd images/
    $wget https://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-amd64-disk1.img
    $proxmox-deploy --proxmox-host proxmox-host-ip --cloud-images-dir images
    - answer interactive questions

-----------

Install required packages with pip:

    $sudo apt install default-libmysqlclient-dev
    $pip install -r requirements.txt
    
------------
