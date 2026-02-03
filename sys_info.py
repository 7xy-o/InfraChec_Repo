import platform 
import socket
def get_system_info():
    info = {}

    info["system"] = platform.system()
    info["release"] = platform.release()
    info["arch"] = platform.machine()
    info["hostname"] = socket.gethostname()
    info["python_version"] = platform.python_version()
    return info


def print_sys_info():
    data = get_system_info()

    print("\n[+] System information:")
    print(f"      Target OS:    {data['system']}    {data['release']}")
    print(f"      Archticture:  {data['arch']}")
    print(f"      Hostname:     {data['hostname']}")
    print(f"      python ver:   {data['python_version']}")

