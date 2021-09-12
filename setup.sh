

install(){
    loading &
    PID=$!
    pkg install git -y > /dev/null 2>&1 &
    pkg install python -y > /dev/null 2>&1 &
    git clone https://github.com/CyberTitus/Anonymous-SMS.git > /dev/null 2>&1 &
    cd Anonymous-SMS
    pip install -r requirements.txt > /dev/null
    python3 sms.py
    kill $PID
    echo "\n"
    clear
}


loading(){
    loads=('.  ' '.. ' '...')
    while :; do
        for x in "${loads[@]}"; do
            echo -ne "\r[+] Installing Packages$x"
            sleep 0.2
        done
    done
}
install
