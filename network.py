from netifaces import interfaces, ifaddresses, AF_INET
import subprocess

def get_ip(interface):
    return ifaddresses(interface).setdefault(AF_INET,  [{'addr':'No IP addr'}] )[0]['addr']

def do_speedtest(interface):
    ip = get_ip(interface)
    if ip == "addr" or ip == "No IP addr":
        data = ""
    else:
        data = str(subprocess.check_output(f"speedtest-cli --csv --source {ip}", shell=True))
    
    if data == b'' or data == "" or len(data.split(",")) <= 1:
        print (f"{interface} not connected")
    else:
        bits = data.split(",")
        dl = bits[6]
        ul = bits[7]
        
        print (f"{interface} - {ip}: {dl} {ul}")



do_speedtest("eth0")
do_speedtest("wlan0")

# ip = get_ip("eth0")

# print (f"eth0: {ip}")

# print (f"speedtest-cli --csv --source {ip}")

# call = os.system(f"speedtest-cli --csv --source {ip}")
# print (call)


# ip = get_ip("wlan0")
# print (f"eth0: {ip}")
# call = os.system(f"speedtest-cli --csv --source {ip}")
# print (call)





#for ifaceName in interfaces():
#    addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
#    print ('%s: %s' % (ifaceName, ', '.join(addresses)))
