import logging

import paramiko


def ssh():
    print("SSH Connect")
    SSH_IP = input("IP:")
    SSH_User = input("User Name:")
    SSH_Password = input("Password:")
    # 创建一个ssh的客户端，用来连接服务器
    SSHClient = paramiko.SSHClient()
    # 创建一个ssh的白名单
    know_host = paramiko.AutoAddPolicy()
    # 加载创建的白名单
    SSHClient.set_missing_host_key_policy(know_host)
    # 连接服务器
    try:
        SSHClient.connect(
            port=22,
            username=SSH_User,
            hostname=SSH_IP,
            password=SSH_Password
        )
        logging.info("SSH Connect susses")
        while True:
            command = input(SSH_User + "@" + SSH_IP + ">>>")
            if command != "exit":
                stdin, stdout, stderr = SSHClient.exec_command(command)
                # stdin  标准格式的输入，是一个写权限的文件对象
                # stdout 标准格式的输出，是一个读权限的文件对象
                # stderr 标准格式的错误，是一个写权限的文件对象
                print(stdout.read().decode())
                logging.info(f"SSH command execute:{command}")
            else:
                SSHClient.close()  # 关闭连接
                logging.info("SSH Connect closed")
                break
    except:
        logging.info("SSH Connect error")
        print("Connect Error")
