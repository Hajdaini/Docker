import os 
import subprocess


def cmd(cmd, listed=False):
    output = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    correct_output = output.communicate()[0].decode().replace('\'', '').splitlines()
    if listed:
        return correct_output
    else:
        return correct_output[0]




def get_bridge_name():
    bridge_name = cmd(['docker', 'network', 'inspect', 'bridge' ,"--format", "'{{.Options}}'"]).split( )
    for x in bridge_name:
        if 'name' in x:
            return (x.split(':')[-1])

subnet = cmd(['docker', 'network', 'inspect', 'bridge' ,"--format", "'{{range .IPAM.Config}}{{.Subnet}}{{end}}'"])
gateway = cmd(['docker', 'network', 'inspect', 'bridge' ,"--format", "'{{range .IPAM.Config}}{{.Gateway}}{{end}}'"])
bridge_name = get_bridge_name()
ids = cmd(["docker", "ps", "-q"], True)
images = cmd(["docker", "ps", "--format", "'{{.Image}}'"], True)
names = cmd(["docker", "ps", "--format", "'{{.Names}}'"], True)

print("\nGLOBAL DOCKER CONFIG :")
print("\tDocker network bridge name : {}".format(bridge_name))
print("\tSubnet : {}".format(subnet))
print("\tGateway : {}\n".format(gateway))

print("\nCONTAINERS DOCKER CONFIG :\n")
counter = 0
for id in ids:
    ip = cmd(['docker', 'inspect', "--format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'", id])
    mac_addr = cmd(['docker', 'inspect', "--format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}'", id])
    if ip or mac_addr: # only if they have ip or mac address
        print("\t{} ({}) from {}".format(names[counter], id, images[counter]))
        print("\t\t-IP: {}".format(ip))
        print("\t\t-MAC ADDRESSE: {}".format(mac_addr))
        counter += 1
        print("\n")
