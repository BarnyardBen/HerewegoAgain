import configparser

SwitchInventory = [
	{
		"Name" : "N-CoreA01-AC1-Local_Switch",
		"Ram" : "512 MB",
		"vCPUs" : "1",
		"QEMU_binary" : "qemu-system-x86 (v4.2.1)",
		"Boot_Priority" : "CD/DVD-ROM or HDD",
		"On_close" : "Power off the VM",
		"Console_type" : "telnet",
		"Adapters" : "13",
		"Base_MAC" : "0c:c0:5e:66:00:00",
		"Type" : "Realtek 8139 Ethernet (rtl8139)",
		"Replicate_network_connection_states_in_QEMU" : "Enabled"
	},
	{
		"Name" : "N-CoreA01-AC1-IT_Network",
		"Ram" : "512 MB",
		"vCPUs" : "1",
		"QEMU_binary" : "qemu-system-x86 (v4.2.1)",
		"Boot_Priority" : "CD/DVD-ROM or HDD",
		"On_close" : "Power off the VM",
		"Console_type" : "telnet",
		"Adapters" : "13",
		"Base_MAC" : "0c:1c:b2:85:00:00",
		"Type" : "Realtek 8139 Ethernet (rtl8139)",
		"Replicate_network_connection_states_in_QEMU" : "Enabled"
	},
	{
	
		"Name" : "N-CoreA01-AC1-MGMT_Network",
		"Ram" : "512 MB",
		"vCPUs" : "1",
		"QEMU_binary" : "qemu-system-x86 (v4.2.1)",
		"Boot_Priority" : "CD/DVD-ROM or HDD",
		"On_close" : "Power off the VM",
		"Console_type" : "telnet",
		"Adapters" : "13",
		"Base_MAC" : "0c:cc:78:5d:00:00",
		"Type" : "Realtek 8139 Ethernet (rtl8139)",
		"Replicate_network_connection_states_in_QEMU" : "Enabled"
	},
	{
	
		"Name" : "N-CoreA01-AC1-ACCT_Network",
		"Ram" : "512 MB",
		"vCPUs" : "1",
		"QEMU_binary" : "qemu-system-x86 (v4.2.1)",
		"Boot_Priority" : "CD/DVD-ROM or HDD",
		"On_close" : "Power off the VM",
		"Console_type" : "telnet",
		"Adapters" : "13",
		"Base_MAC" : "0c:40:34:07:00:00",
		"Type" : "Realtek 8139 Ethernet (rtl8139)",
		"Replicate_network_connection_states_in_QEMU" : "Enabled"
	},
	{
	
		"Name" : "N-CoreA01-AC1-USER_Network",
		"Ram" : "512 MB",
		"vCPUs" : "1",
		"QEMU_binary" : "qemu-system-x86 (v4.2.1)",
		"Boot_Priority" : "CD/DVD-ROM or HDD",
		"On_close" : "Power off the VM",
		"Console_type" : "telnet",
		"Adapters" : "13",
		"Base_MAC" : "0c:e0:f2:0b:00:00",
		"Type" : "Realtek 8139 Ethernet (rtl8139)",
		"Replicate_network_connection_states_in_QEMU" : "Enabled"
	}
]

OutputFile = "N-CoreA01-AC1-SwitchInventory.ini"

def main():
	config = configparser.ConfigParser()

	for sw in SwitchInventory:
		section_name = sw["Name"]
	
		config[section_name] = {
			"ram" : sw["Ram"],
			"vCPUs" : sw["vCPUs"],
			"QEMU binary" : sw["QEMU_binary"],
			"Boot Priority" : sw["Boot_Priority"],
			"On close" : sw["On_close"],
			"Console type" : sw["Console_type"],
			"Adapters" : sw["Adapters"],
			"Base MAC": sw["Base_MAC"],
			"Type" : sw["Type"],
			"Replicate network connection states in QEMU" : sw["Replicate_network_connection_states_in_QEMU"]
			}

	with open(OutputFile, "w") as configfile:
		config.write(configfile)
		
	print(f"Switch Inventory generated: {OutputFile}")
	
if __name__ == "__main__":
	main()
	


