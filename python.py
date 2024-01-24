import asyncio
import logging
import os
import time

log_file_path = "watchdog.log"
logging.basicConfig(filename=log_file_path, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def load_plugins():
    plugins = []
    for filename in os.listdir("plugins"):
        if filename.endswith(".py") and filename != "__init__.py":
            plugin_name = filename[:-3]
            module = __import__(f"plugins.{plugin_name}", fromlist=["execute"])
            if hasattr(module, "execute") and callable(getattr(module, "execute")):
                plugins.append((plugin_name, getattr(module, "execute")))
            else:
                logging.warning(f"Error: Plugin '{plugin_name}' does not have a valid 'execute' function.")
                print(f"Error: Plugin '{plugin_name}' does not have a valid 'execute' function.")
    return plugins


async def main():
    import art
    import model_ssh
    import model_telnet
    import model_ssh_get_res
    import model_calc
    from rich.progress import track

    start_info = """
        KevinlelsToolkit alpha1.1.0
        Code by KevinChang
        """
    Alpha_Warning = """
        WARNING！！！ 
        This version is only for internal test developers to compile and use, if this version is made public, 
        the labor contract will be terminated immediately
        """
    print(Alpha_Warning)
    art.tprint("KevinlelsToolkit")
    print(start_info)
    for _ in track("KevinChang", description="Loading:"):
        time.sleep(1)

    print("A Word For Today:Life is short.You need python.")
    print()
    logging.info("KevinlelsToolkit program started")
    plugins = load_plugins()
    if not plugins:
        logging.info("No plugins available.")
        print("No plugins available.")
    else:
        print("Loaded plugins:")
        for idx, (plugin_name, _) in enumerate(plugins, start=1):
            logging.info(f"Loaded Plugin {plugin_name}")
            print(f"{idx}. {plugin_name}")

    while True:
        command = input("KevinlelsToolkit>>>")
        if command == "ssh":
            logging.info("SSH command executed")
            model_ssh.ssh()
        elif command == "telnet":
            logging.info("Telnet command executed")
            await model_telnet.telnet()
        elif command == "calc":
            logging.info("Calculator command executed")
            model_calc.calc()
        elif command == "resget":
            logging.info("Resource get command executed")
            model_ssh_get_res.resget()
        elif command == "shutdown":
            logging.info("KevinlelsToolkit program shutting down")
            exit(0)
        elif command in [plugin[0] for plugin in plugins]:
            for plugin_name, plugin_func in plugins:
                if command == plugin_name:
                    if plugin_func:
                        logging.info("Executing plugin: %s", plugin_name)
                        plugin_func()
        else:
            print("Unknown Command")


if __name__ == "__main__":
    a = input("Launch code:")
    if a == "007":
        os.system("pip3 install art")
        os.system("pip3 install rich")
        os.system("pip install paramiko")
        os.system("pip3 install telnetlib3")
        exit(114514)
    elif a == "488":
        asyncio.run(main())
    else:
        print("Code error, enter to exit")
        input()
        exit(1)
