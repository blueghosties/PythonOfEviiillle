import socket
import time
import random
import datetime

# written by Malin Hess. Wrote a simple scanner that logs everything that it hits.
# I am making this public so people CAN LEARN, modify and improve upon.
# Tis is a bit of fun...you use this file at your own risk...
# I am not responsible what you do with it. Enjoy.

def da_connection(ip, port):
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send("Hello there...")
        data = s.recv(1024)
        time_start = datetime.datetime.now()
        time_end = datetime.datetime.now()
        dur_time = time_end - time_start

        print 'We hit ' + ip + ' : Received data on port ', port
        print 'Received data: ' + str(data)
        fo = open("pyfoo.txt", "a+")
        fo.write('We definitely hit something...oh goodie! Playtime!         \n')
        fo.write('IP address ' + str(ip) + ' port ' + str(port) + '          \n')
        fo.write('Data received: ' + data + '\n')
        fo.write('Time duration : ' + dur_time + '\n')
        fo.write('-------------------------------------------------------------------------\n')
        # Close opened file
        fo.close()

    except:
        return


def main():
    time_delay = 0

    ipnum = raw_input('Enter in the IP address: ')

    # check to see if user is a silly person and trying to enter something other than ip address
    if ipnum.isalpha() or '.' not in ipnum:
        print 'Please enter valid IP address...silly person.'
        exit(0)

    # using split() to ip address into 4 separate parts to then loop through
    ipnum1, ipnum2, ipnum3, ipnum4 = ipnum.split('.')

    ip4rng = input('Enter fourth set range to scan to - Ex: 192.168.0.x ')
    startport = input('Enter port to start scan from: ')
    endport = input('Enter port to scan to: ')
    rand_delay = raw_input('Do you want a random delay for your scan? Enter \'y\' or \'n\': ')
    concat_ip = str(ipnum1) + '.' + str(ipnum2) + '.' + str(ipnum3)

    # fire off random probes to obfuscate anyone monitoring scan
    if rand_delay == 'y':
        print ('Setting random number generator for scanner: ')
        time_delay = random.randrange(1, 1000)  # eville
        time_delay = '0.' + str(time_delay)    # delay in milliseconds
        float(time_delay)
    elif rand_delay == 'n':
        print ('No random delay will be set...run full throttle!')
        time_delay = 0
    else:
        print ('Why you no listen? Either \'y\' or \'n\'...no scan for you. Bye.')
        exit(0)

    # get file ready for logging ip addresses
    my_date = datetime.datetime.now()
    fo = open('pyfoo.txt', 'a')
    fo.write('-------------------------------------------------------------------------\n')
    fo.write('Scanning IP address ' + ipnum + ' on ' + str(my_date) + '\n')
    fo.write('Scanning range to -> ' + concat_ip + '.' + str(ip4rng) + '\n')
    fo.write('Delay status for scan is ' + rand_delay + '                 \n')
    fo.close()

    this_num = ipnum4

    for x in range(int(this_num), int(ip4rng)):
        ip = concat_ip + '.' + str(x)
        print '[+] ' + str(ip)
        # start of second For Loop
        for port in range(startport, endport):
            print 'Scanning IP -> ' + str(ip) + ' Port: ' + str(port)
            da_connection(ip, port)
            # turn seconds into milliseconds
            if rand_delay == 'y':
                time.sleep(float(time_delay))
                time_delay = random.randrange(1, 999)
                time_delay = '0.' + str(time_delay)
            elif rand_delay == 'n':
                time_delay = 0
            else:
                print 'You are very silly...something went horribly wrong.'
            print float(time_delay), ' m/s'
            if port == endport:
                break


if __name__ == '__main__':
    main()
