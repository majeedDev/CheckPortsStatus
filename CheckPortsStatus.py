import socket

def scan_open_ports(host, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            open_ports.append(port)
    
    return open_ports

def run_test_cases():
    test_cases = [
        {
            "host": "localhost",
            "start_port": 1,
            "end_port": 100
        },
        {
            "host": "example.com",
            "start_port": 80,
            "end_port": 85
        },
        {
            "host": "127.0.0.1",
            "start_port": 8000,
            "end_port": 8010
        }
    ]

    for i, test_case in enumerate(test_cases):
        host = test_case["host"]
        start_port = test_case["start_port"]
        end_port = test_case["end_port"]

        print(f"Running test case {i+1}:")
        print(f"Host: {host}")
        print(f"Scanning ports {start_port} to {end_port}...")

        open_ports = scan_open_ports(host, start_port, end_port)

        if open_ports:
            print("Open ports:")
            for port in open_ports:
                print(f"Port {port} is open.")
        else:
            print("No open ports found in the specified range.")

        print("")

def main():
    run_test_cases()

if __name__ == '__main__':
    main()