# installs required programs, then runs with screen
sudo apt install screen python3

chars=abcd1234ABCDMSND
for i in {1..8} ; do
    mid+="${chars:RANDOM%${#chars}:1}"
done

echo "MACHINE_ID='$mid'" >> client/.env
echo "BACKEND='1.1.1.1'" >> client/.env

screen python3 client/listener.py