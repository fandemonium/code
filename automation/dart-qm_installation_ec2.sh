echo "install softwares needed for high through-put primer design on a 64bit debian based linux"
echo "Creating a directory to store all software packages needed ..."
mkdir ~/softwares
test -e ~/.bash_profile || touch ~/.bash_profile
cd ~/softwares
echo "Done!!!"

## clustal omega
echo "Installing 64bit Clustal omega ... "
curl -O http://www.clustal.org/omega/clustalo-1.2.0-Ubuntu-x86_64
chmod 755 clustalo-1.2.0-Ubuntu-x86_64
mv clustalo-1.2.0-Ubuntu-x86_64 clustalo_1.2.0
echo "export PATH=~/softwares/:$PATH" >> ~/.bash_profile
echo "Done!!!"

## hmmer3
echo "Installing 64bit HMMER3.1 ..."
curl -O ftp://selab.janelia.org/pub/software/hmmer3/3.1b2/hmmer-3.1b2-linux-intel-x86_64.tar.gz
tar -zxvf hmmer-3.1b2-linux-intel-x86_64.tar.gz
mv hmmer-3.1b2-linux-intel-x86_64 hmmer_3.1
rm hmmer-3.1b2-linux-intel-x86_64.tar.gz
echo "export PATH=~/softwares/hmmer_3.1/binaries/:$PATH" >> ~/.bash_profile
echo "Done!!!"

## java
echo "Installing 64 bit java jdk and ant ..."
sudo apt-get update
sudo apt-get install ant openjdk-7-jdk
echo "export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-amd64" >> ~/.bash_profile
source ~/.bash_profile
echo "Done!!!"

## RDPtools
echo "Installing RDPtools ..."
sudo apt-get install git make
git clone https://github.com/rdpstaff/RDPTools
cd RDPTools
git submodule init
git submodule update
make
echo "Done!!"

