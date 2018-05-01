import Blockchain as bc
import os

_last_id = -1

def createWallet():
    global _last_id
    _last_id += 1
    return bc.Wallet(0, _last_id)

def main():
    bc.GLOBAL_BLOCKCHAIN._initial()
    print(bc.GLOBAL_BLOCKCHAIN.getInfo())
    os.system("cls")
    print("Debug Mode")
    while True:
        cmd = input(">> ")
        cmd = cmd.split()
        if len(cmd) > 0:
            if cmd[0] == "exit":
                exit(0)
            elif cmd[0] == "info":
                if len(cmd) > 1:
                    if cmd[1] == "--more":
                        print(bc.GLOBAL_BLOCKCHAIN.getMoreInfo())
                        continue
                print(bc.GLOBAL_BLOCKCHAIN.getInfo())
            elif cmd[0] == "create":
                if len(cmd) < 1:
                    print("Incorrect usage!")
                    continue
                elif cmd[1] == "wallet":
                    createWallet()
                    print("Created successfully!")
            else:
                print("Unknown command!")


if __name__ == '__main__':
    #This is startiong point
    main()
