#现将info文件夹更名
sudo mv /var/lib/dpkg/info /var/lib/dpkg/info.bk
#新建一个新的info文件夹
sudo mkdir /var/lib/dpkg/info
#安装修复
sudo apt-get update
sudo apt-get install -f 
#执行完上一步操作后，在info文件夹下生成一些文件，现将这些文件全部移到info.bk文件夹下
sudo mv /var/lib/dpkg/info/* /var/lib/dpkg/info.bk
#把自己新建的info文件夹删掉
sudo rm -rf /var/lib/dpkg/info
#恢复原有info文件夹，修改名字
sudo mv /var/lib/dpkg/info.bk /var/lib/dpkg/info
