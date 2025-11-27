#Phase 2

#Input file

# Given a list of 4 2-character hex strings, return an ipv4 address string
def hex_to_ip(hexlist: list[str]) -> str:
    ip = ""
    for byte_hex in hexlist:
        byte_int = int(byte_hex, 16)# Convert hex string to decimal int, specifying base 16 (hexidecimal)
        ip += str(byte_int) + '.' # Append the decimal byte to the full ip string, along with a '.' to denote separation

    return ip[0:-1]# Return the ip string without the last character, as it is a uselsss '.'

def parse() :
    #Seperate files by lines, split by commas if needed

    #Parse the filtered raw text files and read packet fields

    #Choose to parse the summary line text or the hex

    #Only output the data needed for the metrics
    print()

def main():
    print(hex_to_ip(['c0', 'a8', '64', '01']))

if __name__ == '__main__':
    main()
