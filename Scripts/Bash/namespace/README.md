# Description
Information of namespaces

# Usage
```
./namespace.sh [CONTAINER ID|NAME]
```

# Output
```
[root@docker ~]# ./namespace.sh 2c
total 0
dr-x--x--x 2 root root 0 Oct 20 20:17 .
dr-xr-xr-x 9 root root 0 Oct 20 20:17 ..
lrwxrwxrwx 1 root root 0 Oct 20 20:21 cgroup -> cgroup:[4026531835]
lrwxrwxrwx 1 root root 0 Oct 20 20:21 ipc -> ipc:[4026532251]
lrwxrwxrwx 1 root root 0 Oct 20 20:21 mnt -> mnt:[4026532249]
lrwxrwxrwx 1 root root 0 Oct 20 20:17 net -> net:[4026532254]
lrwxrwxrwx 1 root root 0 Oct 20 20:21 pid -> pid:[4026532252]
lrwxrwxrwx 1 root root 0 Oct 20 20:21 user -> user:[4026531837]
lrwxrwxrwx 1 root root 0 Oct 20 20:21 uts -> uts:[4026532250]
```
