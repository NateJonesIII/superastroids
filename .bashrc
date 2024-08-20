export PULSE_SERVER=tcp:$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}')
