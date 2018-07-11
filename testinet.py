#testinet.py - Test that internet connection exists.  Record exceptions to file.
"""
Check fix of our DSL connection with ATT
Code adapted from stackoverflow.com/questions/3764291/checking-network-connection
answer by 7h3rAm
Checks for error free socket connection to google-public-dns.a.google.com
Reference: Python 3.4 library: socket in
    https://docs.python.org/3.4/library/socket.html

"""
import socket, datetime, time

def internet(host="8.8.8.8",port=53,timeout=3):
    global testCount, errorCount
    try:
        testCount += 1
        nstr = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+ "  "
        socket.setdefaulttimeout(timeout) 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,port))
        s.shutdown(socket.SHUT_RDWR)  # Clean-up
        s.close()
        # for debugging...
        msg = "OK " + nstr + str(testCount) + "  " + str(errorCount)
        print(msg)
        return True
    except Exception as ex:
        errorCount += 1
        msg = nstr + " Network not reached."  #ex.strerror
        print( msg)
        fp=open("inettest.txt", "a")
        fp.write(msg + "/n")
        fp.close()
        return False
    

def main():
    print( "Start: ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    global testCount, errorCount
    testCount = 0
    errorCount = 0
    
    while True:
        internet()
        time.sleep(10)
        

if __name__=='__main__':
    main()
