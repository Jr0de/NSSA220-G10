from filter_packets import *
from packet_parser import *
from compute_metrics import *

NODE_IPS = ['192.168.100.1', '192.168.100.2', '192.168.200.1', '192.168.200.2']

filter(['provided_files/Captures/Node1.txt',\
        'provided_files/Captures/Node2.txt',\
        'provided_files/Captures/Node3.txt',\
        'provided_files/Captures/Node1.txt'])

# List of nodes with list of packets with list of data
filtered_nodes: list[list[list[str]]] = []

for i in range(1,5):
    filtered_nodes.append(parse(f"Node{i}_filtered.txt"))

#print(filtered_nodes) #im warning you its a lot of text
with open('output.csv', 'w') as f:
    for i, node in enumerate(filtered_nodes):
        data_metrics = get_data_size_metrics(node, NODE_IPS[i])
        time_metrics = get_time_metrics(node, NODE_IPS[i])

        f.write(f"Node {i+1}\n\n")
        #Data metrics
        f.write("Echo Requests Sent,Echo Requests Recieved,Echo Replies Sent,Echo Replies Received\n")
        f.write(f"{data_metrics[0]},{data_metrics[1]},{data_metrics[2]},{data_metrics[3]}\n")
        f.write("Echo Request Bytes Sent (bytes),Echo Requent Data Sent (bytes)\n")
        f.write(f"{data_metrics[4]},{data_metrics[6]}\n")
        f.write("Echo Request Bytes Recieved (bytes),Echo Requent Data Recieved (bytes)\n")
        f.write(f"{data_metrics[5]},{data_metrics[7]}\n\n")
        #Time metrics
        f.write(f"Average RTT (milliseconds),{time_metrics[0]}\n")
        f.write(f"Echo Request Throughput (kB/sec),{time_metrics[1]}\n")
        f.write(f"Echo Request Goodput (kB/sec),{time_metrics[2]}\n")
        f.write(f"Average Reply Delay (microseconds),{time_metrics[3]}\n\n")
