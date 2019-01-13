import os 
import subprocess


def cmd(cmd, listed=False):
    output = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    correct_output = output.communicate()[0].decode().replace('\'', '').splitlines()
    if listed:
        return correct_output
    else:
        return correct_output[0]


ids = cmd(["docker", "ps", "-q"], True)
images = cmd(["docker", "ps", "--format", "'{{.Image}}'"], True)
names = cmd(["docker", "ps", "--format", "'{{.Names}}'"], True)

counter = 0
print("\n")
for id in ids:
    source = cmd(['docker', 'inspect', "--format='{{ (index .Mounts 0).Source }}'", id])
    destination = cmd(['docker', 'inspect', "--format='{{ (index .Mounts 0).Destination }}'", id])
    if source and destination:
        print("{} ({}) from {} :".format(names[counter], id, images[counter]))
        print("\t-Source: {}".format(source))
        print("\t-Destination: {}".format(destination))
        counter += 1
        print("\n")