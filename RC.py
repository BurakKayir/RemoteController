import time
import random


class RemoteController():


    def __init__(self,tv_status = "Off",tv_volume = 0,channel_list = ["BBC"],channel = "BBC"):

        self.tv_status = tv_status

        self.tv_volume = tv_volume

        self.channel_list = channel_list

        self.channel = channel

    def turnon_tv(self):

        if (self.tv_status == "turnedon"):
            print("Tv is already On....")
        else:
            print("Tv is on...")
            self.tv_status = "On"

    def turnoff_tv(self):

        if (self.tv_status == "Off"):
            print("Tv is already off..")
        else:
            print("Tv is off....")
            self.tv_status = "Off"

    def volume_settings(self):

        while True:
            answer = input("Decrease volume: '<'\nIncrease volume: '>'\nQuit: press q")

            if (answer == "<"):
                if (self.tv_volume != 0):
                    self.tv_volume -= 1
                    print("Volume:",self.tv_volume)
            elif (answer == ">"):
                if (self.tv_volume != 31):
                    self.tv_volume += 1
                    print("Volume:",self.tv_volume)
            else:
                print("Volume Updated:",self.tv_volume)
                break

    def add_channel(self,channel_name):

        print("Channel is being added...")
        time.sleep(1)

        self.channel_list.append(channel_name)
        print("Channel was added...")

    def random_channel(self):

        random1 = random.randint(0,len(self.channel_list)-1)

        self.channel = self.channel_list[random1]
        print("Current Channel:" ,self.channel)

    def __len__(self):

        return len(self.channel_list)

    def __str__(self):

        return "Tv Status: {}\nTv Volume: {}\nChannel List: {}\nCurrent Channel: {}\n".format(self.tv_status,self.tv_volume,self.channel_list,self.channel)

remotecontroller = RemoteController()


print("""
Television Application
1. Turn on the Tv
2. Turn off the Tv
3. Volume settings
4. Add channel
5. Number of channels
6. Switch to random channel
7. Tv Status
To quit please press 'q'.
""")



while True:

    operation = input("Select option:")

    if (operation == "q"):
        print("Program is being ended...")
        break

    elif (operation == "1"):
        remotecontroller.turnon_tv()

    elif (operation == "2"):
        remotecontroller.turnoff_tv()

    elif (operation == "3"):
        remotecontroller.volume_settings()

    elif (operation == "4"):
        channel_names = input("Please insert the channel names splitting by ','")
        channel_list = channel_names.split(",")
        for onestoadd in channel_list:
            remotecontroller.add_channel(onestoadd)

    elif (operation == "5"):
        print("Number of Channels:",len(remotecontroller))

    elif (operation == "6"):
        remotecontroller.random_channel()

    elif (operation == "7"):
        print(remotecontroller)

    else:
        print("Invalid Operation...")