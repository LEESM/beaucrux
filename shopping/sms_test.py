import sys
sys.path.append("..")
import coolsms

def main():
	api_key = 'NCS579874C921A39'
	api_secret = '1B0D7357C4BBA22DCFCACA13AEC4DFFA'
	to = '01095359567'
	sender = '01095359567'
	message = '테스트 메시지'
	cool = coolsms.rest(api_key, api_secret)
	status = cool.send(to,message,sender)
	print(status)

if __name__ == "__main__":
	main()
	sys.exit(0)