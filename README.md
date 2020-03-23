#Multi-Node-Hadoop-Installation
#Instruction in terminal
```
Create a user
Enter number of Namenodes
Enter number of Datanodes
Enter the name of Namenode
Enter the ipaddress of Namenode
Enter the name of Datanode
Enter the ipaddress of Datanode
```
#Changes in file at Namenode side
```
/home/hduser/.bashrc
/etc/hosts
/etc/hostname
/home/hduser/hadoop-2.7.3/etc/hadoop/slaves
/home/hduser/hadoop-2.7.3/etc/hadoop/core-site.xml
/home/hduser/hadoop-2.7.3/etc/hadoop/mapred-site.xml
/home/hduser/hadoop-2.7.3/etc/hadoop/hdfs-site.xml
```
#Changes in file at Datanode side
```
/home/hduser/.bashrc
/etc/hosts
/etc/hostname
/home/hduser/hadoop-2.7.3/etc/hadoop/core-site.xml
/home/hduser/hadoop-2.7.3/etc/hadoop/mapred-site.xml
/home/hduser/hadoop-2.7.3/etc/hadoop/hdfs-site.xml
```
#Code Flow
```
Creating a hduser
Download and extract hadoop 2.7.3
Extract Java JDK
Enter the Inputs
Make changes in file
Create a ssh file and copy to datanode
Start connection with datanode
```
#To begin with the installation: Download this git file and Download the JAVA JDK to git fie folder:https://drive.google.com/open?id=1V0Y_HXTtfBcSVRb5rJ58EbRAzJ-3rBFA
First run datanode.py on all datanodes and follow the instruction in terminal:```sudo python3 datanode.py```
after completing the setup type the following commands:
```
su - hduser
cd hadoop-2.7.3/bin
./hadoop namenode -format
```
Second run namenode.py on all namenodes and follow the instruction in terminal:```sudo python3 namenode.py```
after completing the setup type the following commands:
```
su - hduser
cd hadoop-2.7.3/bin
./hadoop namenode -format
```
Installation is complete now run the jar file in master node
