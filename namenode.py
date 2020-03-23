import sys
import os
from os import path


NamenodeName=[]
NamenodeIP=[]
DataNodeName=[]
DataNodeIP=[]


def numNamefunc():
    try:
        numNameNodes=int(input("Enter the number of Name Nodes\n"))
        if(numNameNodes<0):
            print("Number of Name Nodes Cannot be Negative")
            numNamefunc()
    except ValueError:
        print("Error: Enter a valid Integer Number for Number of Name Nodes\n")
        numNamefunc()
    return numNameNodes
def numDatafunc():
    try:
        numDataNodes=int(input("Enter the number of Data Nodes\n"))
        if(numDataNodes<0):
            print("Number of Data Nodes Cannot be Negative")
            numDatafunc()
    except ValueError:
        print("Error: Enter a valid Integer Number for Number of Data Nodes\n")
        numDatafunc()
    return numDataNodes

def readFile():
    with open("input.txt") as fp:
        line=fp.readline()
        cnt=0
        while line:
            splitUser=line.split(':')
            splitData=splitUser[1].split('\t')
            if(splitUser[0]=='master'):
                NamenodeName.append(splitData[0])
                NamenodeIP.append(splitData[1])
            elif(splitUser[0]=='slave'):
                DataNodeName.append(splitData[0])
                DataNodeIP.append(splitData[1])
            line=fp.readline()
            cnt+=1



def NodeInput(numNameNodes,NumDataNodes):
    if(path.exists("/home/hduser/input.txt")==True):
        readFile()
    else:
        f=open("/home/hduser/input.txt","w")
        for x in range(0,numNameNodes):
            inputNameNode= input("Enter the name of Name Node "+str(x+1)+"\n")
            inputIPNameNode= input("Enter the Ip address of Name Node" +str(x+1)+"\n")
            NamenodeName.append(inputNameNode)
            NamenodeIP.append(inputIPNameNode)
            f.writelines(["master:",inputNameNode,"\t",inputIPNameNode,"\n"])
        for y in range(0,NumDataNodes):
            inputDataNode= input("Enter the name of Data Node "+str(y+1)+"\n")
            inputIPDataNode=input("Enter the Ip address of Data Node"+str(y+1)+"\n")
            DataNodeName.append(inputDataNode)
            DataNodeIP.append(inputIPDataNode)
            f.writelines(["slave:",inputDataNode,"\t",inputIPDataNode,"\n"])
        f.close()    
def main():
    print("Welcome to Hadoop Installation Please run this python namenode side\n")
    if(path.exists("/home/hduser")!=True):
        os.system('sudo adduser hduser')
        os.system('sudo usermod -aG sudo hduser')
    numNameNodes=numNamefunc()
    numDataNodes=numDatafunc()
    NodeInput(numNameNodes,numDataNodes)
    cmd='sudo wget https://archive.apache.org/dist/hadoop/core/hadoop-2.7.3/hadoop-2.7.3.tar.gz -P /home/hduser'
    cmd1='sudo tar -xvf /home/hduser/hadoop-2.7.3.tar.gz -C /home/hduser'
    if(path.exists("/home/hduser/hadoop-2.7.3.tar.gz")!=True):
        os.system(cmd)
    if(path.exists("/home/hduser/hadoop-2.7.3")!=True):
        os.system(cmd1)
    if(path.exists("/home/hduser/jdk1.8.0_241")!=True):
        os.system('sudo tar -xvf jdk1.8.0_241.tar.xz -C /home/hduser')

    f=open("/home/hduser/.bashrc","a")
    f.writelines(["# User Specific aliases and functions\n",
    "export HADOOP_HOME=/home/hduser/hadoop-2.7.3\n",
    "export HADOOP_CONF_DIR=/home/hduser/hadoop-2.7.3/etc/hadoop\n",
    "export HADOOP_MAPRED_HOME=/home/hduser/hadoop-2.7.3\n",
    "export HADOOP_COMMON_HOME=/home/hduser/hadoop-2.7.3\n",
    "export HADOOP_HDFS_HOME=/home/hduser/hadoop-2.7.3\n",
    "export YARN_HOME=/home/hduser/hadoop-2.7.3\n",
    "export PATH=$PATH:/home/hduser/hadoop-2.7.3/bin\n",
    "# Set Java Home\n",
    "export JAVA_HOME=/home/hduser/jdk1.8.0_241\n",
    "export PATH=/home/hduser/jdk1.8.0_241/bin:$PATH\n"])
    f.close()
    os.system('sudo -s source /home/hduser/.bashrc')
    os.system('exit')
    for x in range(0,len(NamenodeName)):
        NamenodeIP[x]=NamenodeIP[x].strip('\n')
    for y in range(0,len(DataNodeName)):
        DataNodeIP[x]=DataNodeIP[x].strip('\n')
        
    f=open("/etc/hosts","w")
    for x in range(0,len(NamenodeName)):
        f.writelines([NamenodeIP[x]," ",NamenodeName[x],"\t",NamenodeIP[x],"\n"])
    for y in range(0,len(DataNodeName)):
        f.writelines([DataNodeIP[y]," ",DataNodeName[y],"\t",DataNodeIP[y],"\n"])
    f.writelines(["\n\n",
    "# The following lines are desirable for IPV6 capable Hosts\n",
    "::1\tip6-localhost ip6-loopback\n",
    "fe00::0 ip6-localnet\n",
    "ff00::0 ip6-mcastprefix\n",
    "ff02::1 ip6-allnodes\n",
    "ff02::2 ip6-allrouters\n"])
    f.close()


    f=open("/etc/hosts.allow","a")
    f.writelines(["ssh:192.168.0.1:allow\n",
    "ssh:192.168.0.2:allow\n"])
    f.close()
    f=open("/etc/hostname","w")
    for x in range(0,len(NamenodeName)):
        f.writelines([NamenodeName[x],"\n"])
    f.close()
    
    
    f=open("/home/hduser/hadoop-2.7.3/etc/hadoop/slaves","w")
    for x in range(0,len(NamenodeName)):
        f.writelines([NamenodeName[x]])
    for y in range(0,len(DataNodeName)):
        f.writelines([DataNodeName[y]])
    f.close()


    string1="<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
    string2="<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>"
    f=open("/home/hduser/hadoop-2.7.3/etc/hadoop/core-site.xml","w")
    f.writelines([string1,"\n",
    string2,"\n",
    "<configuration>\n",
    "<property>\n",
    "<name>fs.default.name</name>\n",
    "<value>hdfs://master:54310</value>\n",
    "</property>\n",
    "</configuration>\n"])
    f.close()


    f=open("/home/hduser/hadoop-2.7.3/etc/hadoop/mapred-site.xml","w")
    f.writelines([string1,"\n",
    string2,"\n",
    "<configuration>\n",
    "<property>\n",
    "<name>mapreduce.framework.name</name>\n",
    "<value>master:54311</value>\n",
    "</property>\n",
    "</configuration>\n"])
    f.close()


    f=open("/home/hduser/hadoop-2.7.3/etc/hadoop/hdfs-site.xml","w")
    f.writelines([string1,"\n",
    string2,"\n",
    "<configuration>\n",
    "<property>\n",
    "<name>dfs.replication</name>\n",
    "<value>2</value>\n",
    "</property>\n",
    "<property>\n",
    "<name>dfs.permission</name>\n",
    "<value>false</value>\n",
    "</property>\n",
    "</configuration>\n"])
    f.close()

    stringx="/home/hduser/hadoop-2.7.3/bin/hadoop namenode -format"
    os.system('su - hduser -c'+stringx)

    
    if(path.exists("/home/hduser/.ssh/id_rsa.pub")!=True):
        string="'ssh-keygen -t rsa'"
        stringx="'ssh-copy-id -i $HOME/.ssh/id_rsa.pub hduser@slave'"
        os.system('su - hduser -c '+string)
        os.system('su - hduser -c '+stringx)
    stringy="'ssh slave'"
    os.system('su - hduser -c '+stringy)
    

    

if __name__ == "__main__":
    main()    

