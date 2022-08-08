import click, requests, os, http.server, socketserver, socket
from datetime import datetime
from webbrowser import open

def sendsms():
    number = click.prompt('[+] Enter the number (Include country code e.g. +1): ')
    message = click.prompt('\n[+] Enter the message: ')
    URL = "https://textbelt.com/text"
    DATA = {'phone': number, 'message': message, 'key': 'textbelt'}
    response = requests.post(URL, DATA).json()
    if response['success']:
        click.secho("[+] Sent Message Successfully!", fg="green")
    else:
        click.secho("[-] There was an error!", fg="red")
    return None

def share_files():
    path = str(input('[+] Enter PATH to directory which you want to share (current directory is default): '))
    path = '.' if len(path) == 0 else path
    os.chdir(path)
    ip = socket.gethostbyname(socket.gethostname())
    Handler = http.server.SimpleHTTPRequestHandler
    try:
        print(f"Serving files at http://{ip}:5003")
        with socketserver.TCPServer(("", 5003), Handler) as httpd:
            click.secho('[+] Press CTRL+C to Exit', fg="red")
            httpd.serve_forever()
    except KeyboardInterrupt:
        click.secho("[-] Thanks for using this tool.", fg="red")
        exit(0)

def spoof_email():
    URL = "http://cntreon.000webhostapp.com/email/"
    open(URL)
    click.secho('[+] Email Website Opened', dim=True)
    

def header():
    h=f'''
   _____ ____  ___    __    __ __
  / ___// __ \/   |  / /   / //_/
  \__ \/ /_/ / /| | / /   / ,<
 ___/ / ____/ ___ |/ /___/ /| |
/____/_/   /_/  |_/_____/_/ |_|   [{datetime.now().date().strftime('%d/%m/%Y')}]          
{'-'*32}           
[1] Send SMS Anonymously
[2] Share Files (Same WiFi Network)
[3] Email Spoofer

[0] Exit
    '''.center(50)
    click.secho(h, fg="green")
    try:
        option = click.prompt('[+] Select an Option', type=int)
    except click.exceptions.Abort:
        click.secho("\n[-] Good bye!", fg="red")
        exit(0)
    return option

def confirm_option(option):
    match option:
        case 0:
            click.secho("[-] Thanks for using this tool.", fg="red")
            exit(0)
        case 1:
            sendsms()
        case 2:
            share_files()
        case 3:
            spoof_email()
        case _:
            exit(0)


confirm_option(header())