import urllib.request
import urllib.error

def check_internet():
	try:
		urllib.request.urlopen("http://www.google.com", timeout=10)
	except urllib.error.URLError:
		print("Internet Connection Failed.")
		return False
	except urllib.error.HTTPError:
		print("Internet Connection Failed.")
		return False
	else:
		print("Internet is Connected.")
		return True

check_internet()
