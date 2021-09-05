import requests
import click

class SMS:
	def __init__(self, number, text):
		self.number = number
		self.text = text
		self.url = "https://textbelt.com/text"
		self.data = data = {"phone": number, "message": text, "key": "textbelt"}

	def sendSMS(self):
		res = requests.post(self.url, data=self.data).json()
		if res['success']:
			click.secho("[+] Sent Message Successfully!", fg="green")
		else:
			click.secho("[-] Couldn't Send Message!", fg="red")
			click.secho('[-] '+res['error'], fg="red")



if __name__ == '__main__':
	try:
		NUMBER = click.prompt('Enter Number (Include country code, e.g. +92)', type=str)
		TEXT = str(input("Enter Message: "))
	except:
		click.secho("\n[-] Good bye!", fg="red")
		exit()
	sms = SMS(NUMBER, TEXT)
	if click.confirm('Do you want to send the message?'):
		sms.sendSMS()
	else:
		click.secho("[-] Good bye!", fg="red")
		exit()