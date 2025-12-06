#Phase 3

import packet_parser

parsed1 = packet_parser.parse("Node1_filtered.txt")
parsed2 = packet_parser.parse("Node2_filtered.txt")
parsed3 = packet_parser.parse("Node3_filtered.txt")
parsed4 = packet_parser.parse("Node4_filtered.txt")


NODE1 = "192.168.100.1"
NODE2 = "192.168.100.2"
NODE3 = "192.168.200.1"
NODE4 = "192.168.200.2"

def get_data_size_metrics(data: list[list[str]]) :
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

ICMP_TYPE = 34
TIME = -1

def get_time_metrics(data: list[list[str]]) :
    req_time = None
    rpl_time = None
    looking_for_matching_reply = False
    round_trip_sum = 0
    round_trip_count = 0

    #Create loop to do the following Time based metrics:
    for packet in data:
        #1. Average Ping Round Trip Time (RTT): Measured in milliseconds
        #1a. Get the echo request and corresponding reply times
        
        # If packet is an icmp echo request/reply
        if packet[ICMP_TYPE] == '08' and not looking_for_matching_reply:
            req_time = float(packet[TIME])
            looking_for_matching_reply = True
            print(f"Req time: {req_time}")
        if packet[ICMP_TYPE] == '00' and looking_for_matching_reply:
            rpl_time = float(packet[TIME])
            looking_for_matching_reply = False
            round_trip_count += 1
            # Find round trip time and add to sum
            round_trip_sum += (rpl_time - req_time)
            print(f"Reply time: {rpl_time}")
            print(f"RTT: {rpl_time - req_time}\n")
            
        #2. Echo Request Throughput (in kB/sec): 

        #3. Echo Request Goodput (in kB/sec):

        #4. Average Reply Delay (in microseconds): 


    #Create loop to do the following Distance metric:

    #Output
    print()

if __name__ == '__main__':
    get_time_metrics(parsed1)
