import time
import subprocess
from UPS_HAT_C.INA219 import INA219
ina219 = INA219(addr=0x43)

def get_system_stats(): 

    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:   # 
        content = f.readlines()
        cpu_unconverted_temp = content[0]
        CPU_TEMP = int(cpu_unconverted_temp) / 1000 # gets that from mili celsius to Celsuis
        
    

    with open("/proc/meminfo", "r") as f:   # 	
            content = f.readlines()
            TOTAL_MEM_SPACE = content[0]
            MEM_AVAILABLE = content[2]
            

    with open("/proc/stat", "r") as f:
         content_stat = f.readlines()
         allcores = content_stat[0]
         core1 = content_stat[1]
         core2 = content_stat[2]
         core3 = content_stat[3]
         core4 = content_stat[4]
    

    with open("/proc/stat", "r") as f:
         content_stats = f.readlines()

         test1 = (content_stats[0]).split()

         allcoresresult1 = []

         for i in test1[1:]:
              allcoresresult1.append(int(i))
                   

    time.sleep(1)

    with open("/proc/stat", "r") as f:
         content_stats = f.readlines()

         test2 = (content_stats[0]).split()

         allcoresresult2 = []

         for i in test2[1:]:
              allcoresresult2.append(int(i))
             
                
    allcoresresult = [b - a for a, b in zip(allcoresresult1, allcoresresult2)]

    idlediff1 = allcoresresult1[3]
    idlediff2 = allcoresresult2[3]

    total_idle_diff = idlediff2 - idlediff1
    totaldiff = sum(allcoresresult)

    

    CPU_USAGE = round((totaldiff - total_idle_diff) / totaldiff * 100, 2)

    
    bus_voltage = ina219.getBusVoltage_V()             # voltage on V- (load side)
    shunt_voltage = ina219.getShuntVoltage_mV() / 1000 # voltage between V+ and V- across the shunt
    current = ina219.getCurrent_mA()                   # current in mA
    power = ina219.getPower_W()                        # power in W
    P = (bus_voltage - 3)/1.2*100
    if(P > 100):P = 100
    if(P < 0):P = 0

    IP = subprocess.check_output(["hostname", "-I"]).decode().strip().split()[0]

    return CPU_TEMP,CPU_USAGE,P,IP,TOTAL_MEM_SPACE,MEM_AVAILABLE,

    # print("_______________________________________________________________")
    # print(f"CPU TEMP: {CPU_TEMP}")
    # print(f"CPU USAGE: {CPU_USAGE}")
    # print(f"BATTERY: {p:.1f}%")
    # print(IP)
    # print(f"Total space: {TOTAL_MEM_SPACE}.  MemAvailable {MEM_AVAILABLE}", end="")
    # print(f"ALL CORES: {allcores}")
    # print(core1,core2,core3, core4)
    # print("_______________________________________________________________")
               
