

install(){
    loading &
    PID=$!
    pkg install git -y > /dev/null
    pkg install python -y > /dev/null
    git clone https://github.com/CyberTitus/Anonymous-SMS.git > /dev/null
    cd Anonymous-SMS
    pip install -r requirements.txt
    kill $PID
    exit
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
