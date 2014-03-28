import socket
import time

# This is an inspirational result from the book, Violent Python, written by - TJ OConner. 
# For anyone that enjoys hacking or wants to learn about hacking/programming, this is a great book. 
# Buy it. 
# This code is free to anyone who wants to modify it and use it. Remember, you are responsible
# for running this code, not anyone else. Test, run, enjoy...at your own discretion and risk.
# All I ask is credit for the work I've done. Creditware...pass the credit along.
# I am just starting out on my journey into hacking and programming, so any constructive criticism is welcome.
# Run using Python version 2.7.3

def da_connect(ip, port):
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send('Hello! This is EVIILLLE calling! Anyone home?')
        data = s.recv(1024)

        print 'We hit something! Received' + str(data)
        print 'Logging hit on the network.'

        fo = open("hits.txt", "a")
        now = time.strftime("%c")

        # date and time representation
        print "Current date & time " + time.strftime("%c")
        toFoOut = "We hit " + str(ip) + ": " + str(port) + ": " + time.strftime("%c")

        # write to file
        fo.write(toFoOut + '\n')
        fo.close()
        print 'Wrote to log file.'

        # We want to close the connection after we opened it.
        # This is for logging open ports and nothing more at the moment.
        # Muhahahahahahaha.
        s.close()
        s.shutdown()
    
    except:
        return

def main():
    print '#######################################################'
    print '#          Written by blueghosties 2014               #'
    print '#     Inspired by Violent Python author TJ OConnor    #'
    print '#    Not responsible for program use or any damage    #'
    print '#  to any system as a result of running this program  #'
    print '#######################################################' 
    print '                          --                   '
    print '                        / 00|       BOO!       '
    print '                       /    /                  '
    print '                      /      \\                '
    print '                      \/\/\/\/                 '
    
    print 'Enter first three numbers, then press enter...\nno dot after it...next three and so on. \nExample: 192 <enter> 168 <enter> 1 <enter> 100 <enter>'
    # concat_ip = input('Enter in the ip range ')
    num1 = input('Enter first set of IP num: ')
    num2 = input('Enter second set of IP num: ')
    num3 = input('Enter third set of IP num: ')
    num4 = input('Enter fourth set of IP num: ')
    port = input('Enter in port range: <from port 0 to ?> ')
    int(port)

    # Raise less suspicion by slowing down the scan rate
    # Was thinking about putting in a random() number generator to 
    # to really vary the times of hitting the ports, but thought it
    # was overkill.
    timeDelay = input('Enter a number if you want a time delay.\nOtherwise, just enter 0 \n<Example: 2 for 2 seconds between scans>')
    if timeDelay > 0:
        print 'Delay set for ' + str(timeDelay) + ' seconds.'
    else:
        print 'Delay not set...we want it to scream!'

    # this_num will increment after it has scanned the ip range
    this_num = num4

    # concat the entered ip address
    concat_ip = str(num1) + '.' + str(num2) + '.' + str(num3) + '.'

    # set x as this_num ip range number
    for x in range(this_num, 255):
        # concat full ip address
        ip = concat_ip + str(x)
        print '[+] ' + str(ip)
        # time to count the port range to see if we find an opening
        for port in range(0, 1000):
            print 'Scanning IP:' + str(ip) + ' Port: ' + str(port)
            # time for sleep?
            time.sleep(timeDelay)
            banner = da_connect(ip, port)
            # if we connectted call da_connect() method
            if banner:
                print '[+] ' + ip + ': ' + banner

if __name__ == '__main__':
    main()
