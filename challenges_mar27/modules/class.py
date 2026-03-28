import ipaddress

def generate_class_a_hosts(octet):
    """
    Generates all 16,777,214 usable host IPs for a Class A octet.
    Accepts input as an integer (10) or string ('10').
    """
    try:
        # Convert input to a string and ensure it's a full 4-octet network address
        # Example: '10' becomes '10.0.0.0/8'
        clean_octet = str(octet).split('.')[0]
        network_str = f"{clean_octet}.0.0.0/8"
        
        network = ipaddress.IPv4Network(network_str, strict=False)
        
        # Yields each usable host one by one
        for ip in network.hosts():
            yield str(ip)
            
    except ValueError as e:
        print(f"Invalid input: {octet}. Please provide a number between 1 and 223.")

def count_ips(octet):
    """Simple utility to verify the count without printing all 16M lines."""
    print(f"Calculating total usable hosts for Class A ({octet}.0.0.0/8)...")
    
    # We use the network object properties to get the count instantly
    network = ipaddress.IPv4Network(f"{octet}.0.0.0/8", strict=False)
    # Total addresses - 2 (Network and Broadcast)
    total_hosts = network.num_addresses - 2
    print(f"Total usable hosts: {total_hosts:,}")

if __name__ == "__main__":
    # 1. Verify the count first
    count_ips(10)
    
    # 2. Example: Print only the last 5 IPs of the 16.7 million
    print("\nFinal 5 IPs in the range:")
    all_hosts = generate_class_a_hosts(10)
    
    # Using a list slice on 16M items is slow, so we just skip to the end 
    # for demonstration purposes in this example:
    last_ips = []
    for ip in all_hosts:
        last_ips.append(ip)
        if len(last_ips) > 5:
            last_ips.pop(0)
    
    for ip in last_ips:
        print(ip)