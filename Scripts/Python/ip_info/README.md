# Description
Show the global config of docker and ip and mac address of all containers **UP** status

# Usage
```
python3 info_ip.y
```

## Ouput Example :
```
GLOBAL DOCKER CONFIG :
        Docker network bridge name : docker0
        Subnet : 172.18.0.0/16
        Gateway : 172.18.0.1


CONTAINERS DOCKER CONFIG :

        debian (c5f6e3f67b85) from 414
                -IP: 172.18.0.4
                -MAC ADDRESSE: 02:42:ac:12:00:04


        mystifying_mestorf (80f710fc79b7) from registry
                -IP: 172.18.0.3
                -MAC ADDRESSE: 02:42:ac:12:00:03


        youthful_kowalevski (7a99e73e6874) from registry
                -IP: 172.18.0.2
                -MAC ADDRESSE: 02:42:ac:12:00:02
```
