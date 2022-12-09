# In Raspberry terminal, upgrade the system and install required libraries.

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install cmake
sudo apt-get install libssl-dev

# Git and python3 must be installed, so if you dont'have:

sudo apt-get install git

sudo apt install python3
sudo apt install python3-pip

# Install the AWS IoT Device SDK for Python too:

python3 -m pip install awsiotsdk
git clone https://github.com/aws/aws-iot-device-sdk-python-v2.git

# Before set the credentials, you must create them for your AWS user account
# Set credentias in enviorement variables. Put the credential files in the directory created in the device. Change the camps with your files names

export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
export AWS_SESSION_TOKEN=<AWS_SESSION_TOKEN>
