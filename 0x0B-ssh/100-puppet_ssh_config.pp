# Configuration file to ensure the config private key

file_line {'Turn off passwd auth':
    ensure => 'present',
    path   => '~/.ssh/school',
    line   => 'PasswordAuthentication no'
}

file_line {'Declare Identify file':
    ensure => 'present',
    path   => '~/.ssh/school',
    line   => 'IdentifyFile ~/.ssh/school',
}
