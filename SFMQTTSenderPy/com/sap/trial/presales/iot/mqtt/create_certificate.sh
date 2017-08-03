#!/bin/bash

echo "Extract the Certificate and the Private Key (plain) from the Keystore file. Use the downloaded ZIP file as is. Run the program with this command 'create_certificate <name_of_the_downloaded_ZIP> <your_directory_with_the_downloaded_ZIP>'"

zip="$1"
thedir="$2"
mkdir $thedir
unzip $zip -d $thedir

# We use the same password given in the properties file for all the conversions
pushd $thedir
password=$(grep "password" pswd.properties|cut -d'=' -f2)
echo $password
echo "$password" | keytool -storepass $password -importkeystore -srckeystore client.ks  -destkeystore client.p12 -deststoretype pkcs12

echo "Create client.pem"
openssl pkcs12 -in client.p12 -out client.pem -passin "pass:$password" -passout "pass:$password"

echo "Extracting certificate"
openssl pkcs12 -in client.p12 -nokeys -out certificate.pem -passin "pass:$password"

echo "Extracting private key"
openssl pkcs12 -in client.p12 -nocerts -out privatekey.pem -passin "pass:$password" -passout "pass:$password"

echo "Extracting private key plain"
openssl rsa -in privatekey.pem -out plainkey.pem -passin "pass:$password"

popd
