#Phase 2

# Given a list of 4 2-character hex strings, return an ipv4 address string
def hex_to_ip(hexlist: list[str]) -> str:
    ip = ""
    for byte_hex in hexlist:
        byte_int = int(byte_hex, 16)# Convert hex string to decimal int, specifying base 16 (hexidecimal)
        ip += str(byte_int) + '.' # Append the decimal byte to the full ip string, along with a '.' to denote separation

    return ip[0:-1]# Return the ip string without the last character, as it is a uselsss '.'

def parse(raw_text: str) -> list[list[str]]:
    blocks = []
    current = []
    #Seperate lines in files by spaces
    fileread = open(raw_text, "r")
    for line in fileread:
        line.split(' ')
        if line.strip().isdigit() or (line and line[0].isdigit() and "ICMP" in line):
            if current:
                blocks.append(current)
                current = []
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
        blocks.append(current)
    return blocks


def main():
    print(hex_to_ip(['c0', 'a8', '64', '01']))
    parsed = parse("Node1_filtered.txt")
    #print(parsed[1][0:70]) --> 1 packet
    print("Source IP: " + hex_to_ip(parsed[1][26:30]))
    print("Destination IP: " + hex_to_ip(parsed[1][30:34]))
    print("Echo Request or reply/Host Unreachable if 3: " + hex_to_ip(parsed[1][34:35]))
    print("Frame size (bytes): " + hex_to_ip(parsed[1][17:18]))
    


if __name__ == '__main__':
    main()
