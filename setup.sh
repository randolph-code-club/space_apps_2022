#!/bin/bash

wetty_layer=$HOME/wetty

echo "Generate OpenSSL certificates"
mkdir -p $wetty_layer/.ssl
openssl req -x509 -nodes -days 1095 -newkey ec:<(openssl ecparam -name secp384r1) -subj "/C=GB/ST=None/L=None/O=None/OU=None/CN=None" -out $wetty_layer/.ssl/wetty.crt -keyout $wetty_layer/.ssl/wetty.key
chmod 700 $wetty_layer/.ssl
chmod 644 $wetty_layer/.ssl/wetty.crt
chmod 600 $wetty_layer/.ssl/wetty.key

echo "Generate the ssh key file"
mkdir -p $wetty_layer/.ssh
ssh-keygen -q -C "wetty-keyfile" -t ed25519 -N '' -f $wetty_layer/.ssh/wetty 2>/dev/null <<< y >/dev/null
cat $wetty_layer/.ssh/wetty.pub >> $wetty_layer/.ssh/authorized_keys
chmod 700 $wetty_layer/.ssh
chmod 644 $wetty_layer/.ssh/authorized_keys
chmod 600 $wetty_layer/.ssh/wetty

force_command="${WEB_TTY_CMD:-"bash"}"

cat << EOF > $wetty_layer/.ssh/sshd_config
HostKey $wetty_layer/.ssh/wetty
AuthorizedKeysFile $wetty_layer/.ssh/authorized_keys
ForceCommand bash -c "HOME=$HOME $force_command"
EOF

cat <<BASH > wetty.sh
#!/bin/bash

/usr/sbin/sshd -f $wetty_layer/.ssh/sshd_config -o "Port 2222"

port=\${WEB_TTY_PORT:-\$PORT}

yarn start --host 0.0.0.0 -port \${port:-3000} --title wetty -base / \
  --ssh-key $wetty_layer/.ssh/wetty \
  --ssh-host localhost \
  --ssh-user \$(whoami) \
  --ssh-port 2222 \
  --ssh-auth publickey
BASH
chmod +x wetty.sh
