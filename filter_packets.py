#!/bin/python3

#Phase 1

import os

def filter(filenames: list[str]):
    for filename in filenames:
        # Using grep, get a list of line numbers matching ICMP packets
        # Grep's -n option allows us to output line numbers, use the cut command to isolate those numbers
        # Write the output to a temporary files called "linenumsNode#.txt"
        tempfile = 'linenums' + os.path.basename(filename)
        os.system(f"grep -n 'ICMP' {filename} | cut -d ':' -f 1 > /tmp/{tempfile}")
        
        # Create output file Node#_filtered.txt
        outputfilename = os.path.basename(filename).replace('.txt', '_filtered.txt')
        os.system(f"touch {outputfilename}")
        
        # Open the capture file and its specified temporary file containing target line numbers
        # Open the empty output file for writing
        try:
            with open(filename, 'r') as capturefile,\
                open(f"/tmp/{tempfile}", 'r') as target_icmp_lines,\
                open(outputfilename, 'w') as outputfile:

                # Reading through every target line number, when the line number matches in the capture file, write that chunk of data to the output file
                line = capturefile.readline().strip()
                linenum = 1
                linenum_target = int(target_icmp_lines.readline().strip())
                print(linenum_target)
                
                while linenum_target:# If a target line still exists, find it
                    if linenum == linenum_target:# When target line is found, write data and continue to next target line
                        
                        lines_to_write = []
                        # Bool to determine if the first empty line in the packet's data has been passed
                        # This is to ensure compatibility with packets of varrying sizes, as otherwise we wouldnt be able to use a while loop to check for the end of a packet
                        first_emptyline_passed = False
                        # Populate lines_to_write, write lines until reach empty line
                        while line.strip() != '' or not first_emptyline_passed:
                            lines_to_write.append(line) 
                            if line.strip() == '':# This is the empty line
                                first_emptyline_passed = True
                            line = capturefile.readline()# Dont strip for formatting
                            linenum += 1
                        
                        # Write data
                        outputfile.writelines(lines_to_write)
                        outputfile.write('\n')# Separate data
                        # Set new line number target
                        try:
                            linenum_target = int(target_icmp_lines.readline().strip())
                        except:# End of file
                            linenum_target = None
                    else:
                        # Increment line num and update line var
                        line = capturefile.readline().strip()
                        linenum += 1

        except FileNotFoundError:
            print(f"File \"{filename}\" not found")
    
        # Remove temporary file
        os.remove(f"/tmp/{tempfile}")

def main():
    filter(['provided_files/Captures/Node1.txt', 'provided_files/Captures/Node2.txt', 'provided_files/Captures/Node3.txt', 'provided_files/Captures/Node4.txt'])

if __name__ == '__main__':
    main()
