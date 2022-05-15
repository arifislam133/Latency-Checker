import os
os.system('color 5F')
import colorama
from tqdm import tqdm, trange
from colorama import Fore,Back
import maskpass
from netmiko import ConnectHandler
from getpass import getpass
from paramiko.ssh_exception import AuthenticationException
from netmiko.ssh_exception import NetmikoAuthenticationException

colorama.init(autoreset=True)

import os
os.system("Title Latency checker")
def main(): #defines the area in indents that will be triggered with main()#
  
  yn = input('Check current latency,  write (yes/no) : ')
  if yn == 'yes' or yn == 'y' or yn == 'Yes' or yn == 'Y':
     print("\nPress 1 for IG-1 and Press 2 for IG-2\n")
     val = input("SELECT ROUTER: ")
     
     if val=='1' : 
    
        cisco1 = { 
             "device_type": "cisco_ios",
             "host": "103.7.251.253",
             "username": "python",
             "password": maskpass.askpass(prompt='\nPassword: ', mask="*"),
             }
         
        #print("LOGGED IN TO IG-1 ROUTER")
         # Show command that we execute.
        command = ""
        cmd2= "ping 103.7.249.46 sou 103.7.249.45 rep 10"
        cmd3= "ping 103.7.248.142 sou 103.7.248.141 rep 10"
        cmd4= "ping 59.144.34.109 sou 59.144.34.110 rep 10"
        cmd5= "ping 125.19.27.25 sou 125.19.27.26 rep 10"
        cmd6= "ping 180.87.39.205 sou 180.87.39.206 rep 10"
    
        cmd7= "ping 103.27.170.64 source 103.27.171.74 rep 10 "
        cmd8= "ping 103.27.170.65 source 103.27.171.74 rep 10"
        cmd9= "ping 157.240.81.162 sou 157.240.81.163 rep 10"
        cmd10= "ping 184.104.210.37 sou 184.104.210.38 rep 10"
        cmd11= "ping 163.47.80.141 source 163.47.80.142 rep 10"
        
        try :
            print("CONNECTING TO IG-1 ROUTER")

            with ConnectHandler(**cisco1) as net_connect:
                output = net_connect.send_command(command)
                output1 = net_connect.send_command(cmd2)
                output2 = net_connect.send_command(cmd3)
                output3 = net_connect.send_command(cmd4)
                output4 = net_connect.send_command(cmd5)
                output5 = net_connect.send_command(cmd6)
    
                output6 = net_connect.send_command(cmd7)
                output7 = net_connect.send_command(cmd8)
                output8 = net_connect.send_command(cmd9)
                output9 = net_connect.send_command(cmd10)
                output10 = net_connect.send_command(cmd11)

        
            print(f"{Back.RED}### GOOGLE MUMBAI AIRTEL ###")
        # Automatically cleans-up the output so that only the show output is returned
        #print(f"{Back.WHITE}\n\033[1;32m### GOOGLE AIRTEL ###\033[0;0m")
            print("\033[1;33m#EXPETCTED LATENCY:35ms\033[0;0m\n")
            print("#ping 103.7.249.46 sou 103.7.249.45 rep 10" + output1+"\n\n")
    
            print(f"{Back.RED}### GOOGLE CHENNAI TATA [20G] ###")
            print("\033[1;33m#EXPETCTED LATENCY: 35ms\033[0;0m\n")
            print("#ping 103.7.248.142 sou 103.7.248.141 rep 10"+output2+"\n\n")
    
            print(f"{Back.RED}### AIRTEL PETRAPOLE NEW [50G] ###")
            print("\033[1;33m#EXPETCTED LATENCY:3ms\033[0;0m\n")
            print("#ping 59.144.34.109 sou 59.144.34.110 rep 10"+output3+"\n\n")
        
            print(f"{Back.RED}### AIRTEL PETRAPOLE [10G] ###")
            print("\033[1;33m#EXPETCTED LATENCY:5ms\033[0;0m\n")
            print("#ping 125.19.27.25 sou 125.19.27.26 rep 10"+output4+"\n\n")
        
            print(f"{Back.RED}### TATA-MUMBAI-CDN ###")
            print("\033[1;33m#EXPETCTED LATENCY:35ms\033[0;0m\n")
            print("#ping 180.87.39.205 sou 180.87.39.206 rep 10"+output5+"\n\n")
        
            print(f"{Back.RED}### DECIX TATA MUMBAI [20G] ###")
            print("\033[1;33m#EXPETCTED LATENCY:35ms\033[0;0m\n")
            print("#ping 103.27.170.64 source 103.27.171.74 rep 10"+output6+"\n")
            print("#ping 103.27.170.65 source 103.27.171.74 rep 10"+output7+"\n\n")

            print(f"{Back.RED}### FACEBOOK KOLKATA [20G] ###")
            print("\033[1;33m#EXPETCTED LATENCY:8ms\033[0;0m\n")
            print("#ping 157.240.81.162 sou 157.240.81.163 rep 10"+output8+"\n\n")
    
            print(f"{Back.RED}### HE SMW4 ORANGE [20G] ###")
            print("\033[1;33m#AVERAGE LATENCY:45ms\033[0;0m\n")
            print("#ping 184.104.210.37 sou 184.104.210.38 rep 10"+output9+"\n\n")
    
            print(f"{Back.RED}### BSCCL IPT COXSBAZAR [18G] ###")
            print("\033[1;33m#EXPETCTED LATENCY:4ms\033[0;0m\n")
            print("#ping 163.47.80.141 source 163.47.80.142 rep 10"+output10+"\n\n")
    
    
    
            print(output)
            print(f"{Back.RED}RED ")
            input("PRESS ENTER TO RETURN")
        
        except (AuthenticationException, NetmikoAuthenticationException):
            print("Login failed! Enter valid password or check your VPN.")
        
        
     elif val == '2' : 
            #print("Work In Process")
        cisco1 = { 
                "device_type": "cisco_ios",
                "host": "103.7.251.241",
                "username": "python",
                "password": maskpass.askpass(prompt='\nPassword: ', mask="*"),
                }
        print("CONNECTING TO IG-2 ROUTER")
    
        command = ""
    
        cmd12 = "ping 142.250.165.118 sou 142.250.165.119"
        cmd13 = "ping 180.87.39.45 source 180.87.39.46"
        cmd14 = "ping 157.240.71.4 source 157.240.71.5"
        cmd15 = "ping 157.240.64.176 source 157.240.64.177"
        cmd16 = "ping 103.7.250.50 sou 103.7.250.49"
        cmd17 = "ping 163.47.83.5 sou 163.47.83.6"
        cmd18 = "ping 128.241.7.96 source 128.241.7.97"
    
        with ConnectHandler(**cisco1) as net_connect:
            output = net_connect.send_command(command)
            output11 = net_connect.send_command(cmd12)
            output12 = net_connect.send_command(cmd13)
            output13 = net_connect.send_command(cmd14)
            output14 = net_connect.send_command(cmd15)
            output15 = net_connect.send_command(cmd16)
            output16 = net_connect.send_command(cmd17)
            output17 = net_connect.send_command(cmd18)
                
        print(f"{Back.RED}### TATA GOOGLE DELHI [10G] ###")
        print("\033[1;33m#EXPETCTED LATENCY: 27ms\033[0;0m\n")
        print("#ping 142.250.165.118 sou 142.250.165.119"+output11+"\n\n")
    
        print(f"{Back.RED}### SMW4 GOOGLE CHENNAI [10G] ###")
        print("\033[1;33m#EXPETCTED LATENCY: 22ms\033[0;0m\n")
        print("#ping 103.7.250.50 sou 103.7.250.49"+output15+"\n\n")
    
    
        print(f"{Back.RED}### TATA MUMBAI [20G] ###")
        print("\033[1;33m#EXPETCTED LATENCY: 35ms\033[0;0m\n")
        print("#ping 180.87.39.45 source 180.87.39.46"+output12+"\n\n")
    
        print(f"{Back.RED}###  AIRTEL CHENNAI FACEBOOk [20G] ###")
        print("\033[1;33m#EXPETCTED LATENCY: 35ms\033[0;0m\n")
        print("#ping 157.240.71.4 source 157.240.71.5"+output13+"\n\n")
    
    
        print(f"{Back.RED}### SMW4 FACEBOOk SINGAPORE [10G] ###")
        print("\033[1;33m#EXPETCTED LATENCY: 54-56ms\033[0;0m\n")
        print("#ping 157.240.64.176 source 157.240.64.177"+output14+"\n\n")
    
        print(f"{Back.RED}### BSCCL IPT KUAKATA [65G] ###")
        print("\033[1;33m#EXPETCTED LATENCY: 5ms\033[0;0m\n")
        print("#ping 163.47.83.5 sou 163.47.83.6"+output16+"\n\n")
    
    
        print(f"{Back.RED}### NTT SMW5 [20G] ###")
        print("\033[1;33m#AVERAGE LATENCY: 45ms\033[0;0m\n")
        print("#ping 128.241.7.96 source 128.241.7.97"+output17+"\n\n")
     
        print(f"{Back.RED}END")
        input("PRESS ENTER TO RETRUN")

    
     else:
    
        import time

        # iterable based
        for i in tqdm([1, 2, 3, 4, 5]):
            time.sleep(0.2)
        
        print("Access Denied!")
           
  elif yn == 'no' or yn == 'n' or yn == 'No' or yn == 'N' or yn == 'NO' :
      import time

        # iterable based
      for i in tqdm([1, 2, 3, 4, 5]):
            time.sleep(0.2)
        
        
      exit()


  
  main() #loops back to where we defined main#
    
main() #This starts the main loop, without this, main would just be defined but not run#


