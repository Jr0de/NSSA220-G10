#Phase 3

import packet_parser

parsed1 = packet_parser.parse("Node1_filtered.txt")
parsed2 = packet_parser.parse("Node2_filtered.txt")
parsed3 = packet_parser.parse("Node3_filtered.txt")
parsed4 = packet_parser.parse("Node4_filtered.txt")


NODE1_SRC = "192.168.100.1"
NODE2_SRC = "192.168.100.2"
NODE3_SRC = "192.168.200.1"
NODE4_SRC = "192.168.200.2"

def compute(data: list[list[str]]) :
    #Create loop to do the following Data size metrics:
    
    #1. Number of Echo Requests sent

    #2. Number of Echo Requests received

    #3. Number of Echo Replies sent

    #4. Number of Echo Replies received

    #5. Total Echo Request bytes sent: In bytes, based on the size of the “frame”

    #6. Total Echo Request bytes received: In bytes, based on the size of the “frame”

    #7. Total Echo Request data sent: In bytes, based on amount of data in the ICMP payload

    #8. Total Echo Request data received: In bytes, based on amount of data in the ICMP payload
    print()

def time(data: list[list[str]]) :
    #Create loop to do the following Time based metrics:

    #1. Average Ping Round Trip Time (RTT): Measured in milliseconds

    #2. Echo Request Throughput (in kB/sec): 

    #3. Echo Request Goodput (in kB/sec):

    #4. Average Reply Delay (in microseconds): 


    #Create loop to do the following Distance metric:

    #Output
    print()


def main():
    compute()

    
if __name__ == '__main__':
    main()