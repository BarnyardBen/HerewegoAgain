from datetime import datetime
from netmiko import ConnectHandler # type: ignore


UserName = "admin"

Switches = [
    {
        "SwitchName": "N-CoreA01-AC1-IT_Network",
        "IP": "10.10.1.30",
        "VlanName": "IT_Network",
        "VlanId": 10,
    },
    {
        "SwitchName": "N-CoreA01-AC1-MGMT_Network",
        "IP": "10.10.1.31",
        "VlanName": "MGMT_Network",
        "VlanId": 20,
    },
    {
        "SwitchName": "N-CoreA01-AC1-ACCT_Network",
        "IP": "10.10.1.32",
        "VlanName": "ACCT_Network",
        "VlanId": 30,
    },
    {
        "SwitchName": "N-CoreA01-AC1-USER_Network",
        "IP": "10.10.1.22",
        "VlanName": "User_Network",
        "VlanId": 40,
    },

]

AllVlans = {Sw["VlanId"]: Sw["VlanName"] for Sw in Switches}

def ConnectToSwitch(IP):
    Device = {
        "device_type": "extreme_exos",
        "host": IP,
        "username": "admin",
        "port": 22,
        "banner_timeout": 30,
        "conn_timeout": 20,
        "timeout": 30,
        "fast_cli": True,
        "use_keys": True,
        "key_file": "/home/student/.ssh/id_rsa",
    }

    return ConnectHandler(**Device)

def main():
    timestamp = datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
    OutputFile = f"AC1VlanDeployment-{timestamp}.txt"

    with open(OutputFile, "w", encoding="utf-8") as f:
        f.write("AC1 VLAN Deployment\n")
        f.write(f"Timestamp: {timestamp}\n")
        f.write("Creating VLANs 10 (IT_Network), 20 (MGMT_Network), 30 (ACCT_Network), 40 (User_Network) on all 4 switches.\n")
        f.write("=" * 80 + "\n\n")

        for Sw in Switches:
            SwName = Sw["SwitchName"]
            SwIp = Sw["IP"]

            print(f"Configuring {SwName} ({SwIp})")
            f.write(f"Switch: {SwName} ({SwIp})\n")
            f.write(f"Creating all VLANs")
            f.write("-" * 40 + "\n")

            try:
                Conn = ConnectToSwitch(SwIp)
                Conn.send_command("disable cli prompting")
                Conn.send_command("disable clipaging")

                for Vid, Vname in AllVlans.items():
                    CreateOut = Conn.send_command(f"create vlan {Vname} tag {Vid}")
                    f.write(f"  create vlan {Vname} tag {Vid}\n")
                    f.write(f"   --> {CreateOut.strip() or 'OK'}\n\n")

                SaveOut = Conn.send_command(f"save configuration primary")
                f.write(f"\nSave Configuration:\n{SaveOut}\n\n")

                f.write("Verification:\n")
                f.write("=" * 40 + "\n")
                f.write(Conn.send_command(f"show vlan") + "\n\n")

                Conn.disconnect()
                f.write("+" * 80 + "\n\n")
                print(f"[SUCCESS] {SwName} configured successfully")
                
            except Exception as e:
                ErrorMsg = f"[ERROR] Failed on {SwName}: {str(e)}\n"
                f.write(ErrorMsg)
                f.write("=" * 80 + "\n\n")
                print(ErrorMsg)

    print(f"Deployment complete! Full log saved to {OutputFile}")

if __name__ == "__main__":
    main()


