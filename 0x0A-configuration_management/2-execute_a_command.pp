# Kill proccess
exec { 'killmenow':
    command => '/usr/bin/pkill -f killmenow',
}
