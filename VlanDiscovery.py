from datetime import datetime
from netmiko import ConnectHandler

Switches = [
	{"Name": "N-CoreA01-AC1-IT_Network", "ip": "10.10.1.30"},
	{"Name": "N-CoreA01-AC1-MGMT_Network", "ip": "10.10.1.31"},
	{"Name": "N-CoreA01-AC1-ACCT_Network", "ip": "10.10.1.32"},
	{"Name": "N-CoreA01-AC1-USER_Network", "ip": "10.10.1.22"},
	{"Name": "N-CoreA01-AC1-Local_Switch", "ip": "10.10.1.24"},
]

Username = "admin"

def main():
	timestamp = datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
	
	for sw in Switches:
		print(f"Discovering Vlans on {sw['Name']} ({sw['ip']})")
		
		Device = {
			"device_type": "extreme_exos",
			"host": sw["ip"],
			"username": "admin",
			"port": 22,
			"banner_timeout": 30,
			"conn_timeout": 20,
			"timeout": 30,
			"fast_cli": True,
			"use_keys": True,
			"key_file": "/home/student/.ssh/id_rsa",
    	}
		
		conn = ConnectHandler(**Device)
		conn.send_command("disable cli prompting")
		conn.send_command("disable clipaging")
			
		output = conn.send_command("show vlan")
		conn.disconnect()
			
		print(output)
			
		filename = f"Vlan Discovery {sw['Name']} {timestamp}.txt"
		filename = filename.replace(":", " ")

		with open(filename, "w", encoding="utf-8") as f:
			f.write(f"VLAN Discovery - {sw['Name']}\n")
			f.write(f"IP: {sw['ip']}\n")
			f.write(f"Timestamp: {timestamp}\n")
			f.write("=" * 60 + "\n\n")
			f.write(output)
			
		print(f"[saved] {filename}")
		
	print("\n1-C Vlan Discovery completed")
	
if __name__ == "__main__":
	main()


