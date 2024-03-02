# Configuration file to ensure the config private key

augeas { 'ssh_config_file':
  context => '~/.ssh/school',
  changes => [
    'set PasswordAuthentication no',
    'set IdentifyFile ~/.ssh/school',
  ],
}
