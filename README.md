# Topology Change Detector

## About

This project is done using Mininet and POX controller to understand how network behaves when topology changes. Basically, we check what happens when a link between switches goes down.

## Tools Used

Mininet

POX Controller

Ubuntu

## Topology

h1 --- s1 --- s2 --- h2

Two hosts are connected through two switches.

## How to Run

### Start controller

```
cd ~/pox
./pox.py forwarding.l2_learning
```

### Run topology

```
cd ~/topo_project
sudo mn --custom topology.py --topo mytopo --controller remote
```

## Testing

### Normal case

```
h1 ping -c 3 h2
```

Output: Ping works, 0% packet loss

### After link failure

```
link s1 s2 down
h1 ping -c 3 h2
```

Output: Ping fails, 100% packet loss

## Result

When the link between switches is removed, hosts cannot communicate. This shows how topology change affects the network.

## Screenshots

### Normal Ping
![Normal](Desktop/normal_ping.png)

### Link Down
![Link Down](Desktop/link_down.png)

### Packet Loss
![Packet Loss](Desktop/packet_loss.png)

## Conclusion

This project helped in understanding SDN basics and how controller reacts when network topology changes.

