import configparser
from datetime import datetime

HostInventory = [
    {
        "Name": "N-CoreA01-AC1-IT_Network-DomainController",
        "Ram": "4096 MB",
        "vCPUs": "2",
        "QEMU_binary": "qemu-system-x86 (v4.2.1)",
        "Boot_Priority": "HDD",
        "On_close": "Send the shutdown signal (ACPI)",
        "Console_type": "vnc",
        "Adapters": "1",
        "Base_MAC": "0c:4f:61:d5:00:00",
        "Type": "Intel Gigabit Ethernet (e1000)",
        "Replicate_network_connection_states_in_QEMU": "Enabled"
    },
    {
        "Name": "N-CoreA01-AC1-MGMT_Network-TestBox2",
        "Ram": "4096 MB",
        "vCPUs": "2",
        "QEMU_binary": "qemu-system-x86 (v4.2.1)",
        "Boot_Priority": "HDD",
        "On_close": "Send the shutdown signal (ACPI)",
        "Console_type": "vnc",
        "Adapters": "1",
        "Base_MAC": "0c:50:a2:8a:00:00",
        "Type": "Intel Gigabit Ethernet (e1000)",
        "Replicate_network_connection_states_in_QEMU": "Enabled"
    },
    {
        "Name": "N-CoreA01-AC1-ACCT_Network-TestBox1",
        "Ram": "4096 MB",
        "vCPUs": "2",
        "QEMU_binary": "qemu-system-x86 (v4.2.1)",
        "Boot_Priority": "HDD",
        "On_close": "Send the shutdown signal (ACPI)",
        "Console_type": "vnc",
        "Adapters": "1",
        "Base_MAC": "0c:cb:a8:90:00:00",
        "Type": "Intel Gigabit Ethernet (e1000)",
        "Replicate_network_connection_states_in_QEMU": "Enabled"
    },
    {
        "Name": "N-CoreA01-AC1-USER_Network-WindowsDesktop1",
        "Ram": "512 MB",
        "vCPUs": "1",
        "QEMU_binary": "qemu-system-x86 (v4.2.1)",
        "Boot_Priority": "CD/DVD-ROM or HDD",
        "On_close": "Power off the VM",
        "Console_type": "telnet",
        "Adapters": "13",
        "Base_MAC": "0c:c0:5e:66:00:00",
        "Type": "Realtek 8139 Ethernet (rtl8139)",
        "Replicate_network_connection_states_in_QEMU": "Enabled"
    },
    {
        "Name": "N-CoreA01-AC1-USER_Network-WindowsDesktop2",
        "Ram": "4096 MB",
        "vCPUs": "2",
        "QEMU_binary": "qemu-system-x86 (v4.2.1)",
        "Boot_Priority": "HDD",
        "On_close": "Send the shutdown signal (ACPI)",
        "Console_type": "vnc",
        "Adapters": "1",
        "Base_MAC": "0c:59:fd:86:00:00",
        "Type": "Intel Gigabit Ethernet (e1000)",
        "Replicate_network_connection_states_in_QEMU": "Enabled"
    },
    {
        "Name": "N-CoreA01-AC1-USER_Network-WindowsDesktop3",
        "Ram": "4096 MB",
        "vCPUs": "2",
        "QEMU_binary": "qemu-system-x86 (v4.2.1)",
        "Boot_Priority": "HDD",
        "On_close": "Send the shutdown signal (ACPI)",
        "Console_type": "vnc",
        "Adapters": "1",
        "Base_MAC": "0c:e2:07:f3:00:00",
        "Type": "Intel Gigabit Ethernet (e1000)",
        "Replicate_network_connection_states_in_QEMU": "Enabled"
    },
    {
        "Name": "N-CoreA01-AC1-USER_Network-WindowsDesktop4",
        "Ram": "4096 MB",
        "vCPUs": "2",
        "QEMU_binary": "qemu-system-x86 (v4.2.1)",
        "Boot_Priority": "HDD",
        "On_close": "Send the shutdown signal (ACPI)",
        "Console_type": "vnc",
        "Adapters": "1",
        "Base_MAC": "0c:46:74:35:00:00",
        "Type": "Intel Gigabit Ethernet (e1000)",
        "Replicate_network_connection_states_in_QEMU": "Enabled"
    }
]

OutputFile = "N-CoreA01-AC1-HostInventory.ini"

def main():
    config = configparser.ConfigParser()
    
    timestamp = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    config['Metadata'] = {
        'Generated_On': timestamp,
        'Description': 'Host inventory'
    }

    for host in HostInventory:
        section_name = host["Name"]
        
        config[section_name] = {
            "ram": host["Ram"],
            "vCPUs": host["vCPUs"],
            "QEMU binary": host["QEMU_binary"],
            "Boot Priority": host["Boot_Priority"],
            "On close": host["On_close"],
            "Console type": host["Console_type"],
            "Adapters": host["Adapters"],
            "Base MAC": host["Base_MAC"],
            "Type": host["Type"],
            "Replicate network connection states in QEMU": host["Replicate_network_connection_states_in_QEMU"]
        }

    with open(OutputFile, "w") as configfile:
        config.write(configfile)
        
    print(f"Host Inventory generated: {OutputFile}")

if __name__ == "__main__":
    main()
	


