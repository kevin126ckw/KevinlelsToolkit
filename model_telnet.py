# model_telnet.py
import logging


async def telnet():
    import telnetlib3
    print("Telnet Connect")
    Telnet_ip = input("IP:")
    Telnet_username = input("User Name:")
    Telnet_password = input("Password:")
    try:
        tn = await telnetlib3.open_connection(Telnet_ip, 23)
        await tn.login(Telnet_username, Telnet_password)
        logging.info("Telnet connect success")
        while True:
            command = input(b'$')
            if command != "exit":
                await tn.shell(command)
                response = await tn.read_until(b'$')
                logging.info(f"Telnet command execute:{command}")
                print(response.decode())
            else:
                logging.info("Telnet Connect Close.")
                await tn.close()  # 使用 await 来关闭连接
    except:
        logging.warning("Telnet Connect Error")
        print("Connect Error")
