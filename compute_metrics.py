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

def get_data_size_metrics(data: list[list[str]], sourceIP: str) :
    #Create loop to do the following Data size metrics:
    num_echoreq_sent = 0
    num_echoreq_recieved = 0
    num_echoreply_sent = 0
    num_echoreply_recieved = 0
    echoreq_bytes_sent = 0
    echoreq_bytes_recieved = 0
    echoreq_data_sent = 0
    echoreq_data_recieved = 0
    metrics = []
    
    for i in range(len(data)):
    #1. Number of Echo Requests sent
        if packet_parser.hex_to_ip(data[i][34:35]) == '8' and packet_parser.hex_to_ip(data[i][26:30]) == sourceIP:
            num_echoreq_sent += 1
    #2. Number of Echo Requests received
        elif packet_parser.hex_to_ip(data[i][34:35]) == '8' and packet_parser.hex_to_ip(data[i][26:30]) != sourceIP:
            num_echoreq_recieved += 1
    #3. Number of Echo Replies sent
        elif packet_parser.hex_to_ip(data[i][34:35]) == '0' and packet_parser.hex_to_ip(data[i][26:30]) == sourceIP:
            num_echoreply_sent += 1
    #4. Number of Echo Replies received
        elif packet_parser.hex_to_ip(data[i][34:35]) == '0' and packet_parser.hex_to_ip(data[i][26:30]) != sourceIP:
            num_echoreply_recieved += 1
        
        for j in range(len(data[i])):
    
    #5. Total Echo Request bytes sent: In bytes, based on the size of the “frame”
            if packet_parser.hex_to_ip(data[i][34:35]) == '8' and packet_parser.hex_to_ip(data[i][26:30]) == sourceIP:
                echoreq_bytes_sent += len(data[i][j])-1
    
    #6. Total Echo Request bytes received: In bytes, based on the size of the “frame”
            elif packet_parser.hex_to_ip(data[i][34:35]) == '8' and packet_parser.hex_to_ip(data[i][26:30]) != sourceIP:
                echoreq_bytes_recieved += len(data[i][j])-1
        
        #7. Total Echo Request data sent: In bytes, based on amount of data in the ICMP payload
        if packet_parser.hex_to_ip(data[i][34:35]) == '8' and packet_parser.hex_to_ip(data[i][26:30]) == sourceIP:
            echoreq_data_sent += int(packet_parser.hex_to_ip(data[i][17:18]))
        
        #8. Total Echo Request data received: In bytes, based on amount of data in the ICMP payload
        elif packet_parser.hex_to_ip(data[i][34:35]) == '8' and packet_parser.hex_to_ip(data[i][26:30]) != sourceIP:
            echoreq_data_recieved += int(packet_parser.hex_to_ip(data[i][17:18]))
    
    metrics.append(num_echoreq_sent)
    metrics.append(num_echoreq_recieved)
    metrics.append(num_echoreply_sent)
    metrics.append(num_echoreply_recieved)
    metrics.append(echoreq_bytes_sent)
    metrics.append(echoreq_bytes_recieved)
    metrics.append(echoreq_data_sent)
    metrics.append(echoreq_data_recieved)
    return metrics

ECHO_REQUEST, ECHO_REPLY = 8, 0

def get_time_metrics(data: list[list[str]], source_ip: str) :
    req_time = None
    rpl_time = None
    looking_for_matching_reply = False
    round_trip_sum = 0
    round_trip_count = 0
    frame_size_sum = 0
    payload_size_sum = 0
    

    #Create loop to do the following Time based metrics:
    for packet in data:
        packet = packet_parser.get_metrics(packet)
        #1. Average Ping Round Trip Time (RTT): Measured in milliseconds
        #Get the echo request and corresponding reply times of packets sourced from this node
        if packet['Type'] == ECHO_REQUEST and packet['Source IP'] == source_ip:
            req_time = packet['Time']
            looking_for_matching_reply = True
            print(f"Request: {packet['Time']}")
        if packet['Type'] == ECHO_REPLY and looking_for_matching_reply:
            rpl_time = packet['Time']
            print(f"Reply: {packet['Time']}")
            #Once times gathered, calculate Round Trip Time and reset time vars
            rtt = (rpl_time - req_time) * 1000# convert to ms
            print(f"Round Trip Time: {rtt:.2f} ms\n")#format for rounding
            round_trip_sum += rtt
            round_trip_count += 1
            req_time = None
            rpl_time = None
            looking_for_matching_reply = False
        
        #2. Echo Request Throughput (in kB/sec): 
        frame_size_sum += packet['Frame Size'] 

        #3. Echo Request Goodput (in kB/sec):
        payload_size_sum += packet['Payload Size']

        #4. Average Reply Delay (in microseconds): 
        

    #Output
    print(f"Average RTT:\t{(round_trip_sum / round_trip_count):.4f} ms")    
    print(f"Throughput:\t{(frame_size_sum / round_trip_sum):.4f} kB/s")
    print(f"Goodput:\t{(payload_size_sum / round_trip_sum):.4f} kB/s")

if __name__ == '__main__':
    get_time_metrics(parsed1, NODE1)
    #nod1_met= get_data_size_metrics(parsed1, NODE1)
    #print("Echo Requests Sent: "+ str(nod1_met[0]))
    #print("Echo Requests Received: "+str(nod1_met[1]))
    #print("Echo Replies Sent: "+str(nod1_met[2]))
    #print("Echo Replies Received: "+str(nod1_met[3]))
    #print("Echo Request Bytes Sent: "+str(nod1_met[4]))
    #print("Echo Request Bytes Received: "+str(nod1_met[5]))
    #print("Echo Request Data Sent: "+str(nod1_met[6]))
    #print("Echo Request Data Received: "+str(nod1_met[7]))
