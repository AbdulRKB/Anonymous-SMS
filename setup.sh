

install(){
    loading &
    PID=$!
    pkg install git > /dev/null
    pkg install python > /dev/null
    git clone https://github.com/CyberTitus/Anonymous-SMS.git > /dev/null
    cd Anonymous-SMS
    pip install -r requirements.txt
    kill $PID
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
