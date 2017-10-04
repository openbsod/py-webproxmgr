from proxmoxer import ProxmoxAPI
proxmox = ProxmoxAPI('10.10.230.61', user='root@pam',
                     password='passw0rd', verify_ssl=False)

for node in proxmox.nodes.get():
    for vm in proxmox.nodes(node['node']).qemu.get():
        print "{0}. {1} => {2}" .format(vm['vmid'], vm['name'], vm['status'])
