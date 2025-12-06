#Phase 2

# Given a list of 4 2-character hex strings, return an ipv4 address string
def hex_to_ip(hexlist: list[str]) -> str:
    ip = ""
    for byte_hex in hexlist:
        byte_int = int(byte_hex, 16)# Convert hex string to decimal int, specifying base 16 (hexidecimal)
        ip += str(byte_int) + '.' # Append the decimal byte to the full ip string, along with a '.' to denote separation

    return ip[0:-1]# Return the ip string without the last character, as it is a uselsss '.'

HEADER_TIMEINDEX, SOURCE_IP_START, SOURCE_IP_END, DESTINATION_IP_START, DESTINATION_IP_END,\
        ICMP_TYPE, ICMP_PAYLOAD_START, ICMP_PAYLOAD_END, DATA_TIMEINDEX = 1, 26, 30, 30, 34, 34, 16, 18, -1 

def parse(raw_text: str) -> list[list[str]]:
    blocks = []
    current = []
    #Seperate lines in files by spaces
    fileread = open(raw_text, "r")
    time = None
    for line in fileread:
        line.split(' ')
        if line.strip().isdigit() or (line and line[0].isdigit() and "ICMP" in line):
            if current:
                current.append(time)
                blocks.append(current)
                current = []
            time = line.split()[HEADER_TIMEINDEX]# I know this line probably doesnt make sense but this whole for loop is so fucked but at least it works so im not touching it
            continue
    #Parse the filtered raw text files and read packet fields
        if len(line) > 4 and line[:4].isdigit():
            # Extract only 2-char hex
            parts = line[4:].strip().split()
            for p in parts:
                #ignore the parts in the file that are ...C....2.U@..E. etc
                if len(p) == 2:
                    current.append(p.lower())
    
    #Only output the data needed for the metrics
    if current:
        blocks.append(current)# Ensures the last packet is captured (i think?)
         
    return blocks
# Take packet data (list of hex strs) and store as needed metrics in the form of a dictionary
def get_metrics(data: list[str]) -> dict:
    metrics = {}
    # Source ip
    metrics['Source IP'] = hex_to_ip(data[SOURCE_IP_START:SOURCE_IP_END])
    # Dest ip
    metrics['Destination IP'] = hex_to_ip(data[DESTINATION_IP_START:DESTINATION_IP_END])
    # icmp type
    metrics['Type'] = int(data[ICMP_TYPE])
    # icmp payload size
    metrics['Payload Size'] = int(''.join(data[ICMP_PAYLOAD_START:ICMP_PAYLOAD_END]),16)
    # frame size
    metrics['Frame Size'] = int(len(data)) - 1# -1 to account for time metric
    # time
    metrics['Time'] = float(data[-1])
    
    return metrics

if __name__ == '__main__':
    #hex_to_ip(['c0', 'a8', '64', '01'])
    parsed = parse("Node1_filtered.txt")
    print(parsed[0])
    print(get_metrics(parsed[0]))

