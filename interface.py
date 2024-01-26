import netifaces as ni

def get_private_ip():
	for iface in ni.interfaces():
		try:
			addrs = ni.ifaddresses(iface)
			if ni.AF_INET in addrs:
				ip = addrs[ni.AF_INET][0]['addr']
				if ip.startswith(('10.','172.', '192.168')):
					return ip
		except Exception:
			pass
	return None

private_ip = get_private_ip()
print(f"Private IP address: {private_ip}")
