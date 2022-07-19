# 🚀 Better BetterDiscord Plugins Installer
# 💬 All the download links are from discord, this is the best to keep the project stable

# ⚡ Import needs
from shutil import which
from colorama import Fore, Back, Style
import requests
import sys
import shutil
import os

# ⚡ Initialize colorama
from colorama import init
init()

# ⚡ Set up variables
prvdownloads = "NILL"


# 📝 This project is mostly made for windows 7 or above, please change this line to your current operating system to make it function properly.
def cls():
    os.system('cls')

# 🎉 Congrats, you are done here
def Done():
    print(Style.RESET_ALL)
    print("🎉 All done, enjoy!")

# 💬 It goes from windows to linux, this part should be fast.
def MoveToPluginsFolder():
    try:
        print("[..] Searching for plugins folder..")

        TestOne = str(os.getenv('APPDATA') + "\\BetterDiscord\\plugins")
        TestTwo = str(os.getenv('APPDATA') + "\\discord\\plugins")
        TestThree = str(os.getenv('APPDATA'))

        print("[..] Searching in " + TestOne)
        if os.path.exists(TestOne):
            print("[v] Plugins folder found, moving plugins")
            source_dir = 'cache/'
            target_dir = TestOne

            file_names = os.listdir(source_dir)

            for file_name in file_names:
                shutil.move(os.path.join(source_dir, file_name), target_dir)
            
            print("Plugins succesfully downloaded and installed!")
            
            os._exit(1)

        print("[x] Not found")

        print("[..] Searching in " + TestTwo)
        if os.path.exists(TestTwo):
            print("[v] Plugins folder found, moving plugins")
            source_dir = 'cache/'
            target_dir = TestTwo

            file_names = os.listdir(source_dir)

            for file_name in file_names:
                shutil.move(os.path.join(source_dir, file_name), target_dir)
            
            print("Plugins succesfully downloaded and installed!")
            
            os._exit(1)

        print("[x] Not found")

        print("[..] Checking if the AppData folder exists")
        if os.path.exists(TestThree):
            print("[*] If you are a windows user, please enter the path of the BetterDiscord plugin folder.")
            y = str(input("[" + Fore.BLUE + '>' + Fore.WHITE +"] Path: "))
            source_dir = 'cache/'
            target_dir = str(y)

            file_names = os.listdir(source_dir)

            for file_name in file_names:
                shutil.move(os.path.join(source_dir, file_name), target_dir)
            print("Plugins succesfully downloaded and installed!")
            os._exit(1)
        else:
            print("[*] If you are a linux user, please enter the path of the BetterDiscord plugin folder.")
            print("[*] Please note that u should run this code with 'sudo' to expect the highest results.")
            print("[!] If you are on MacOS, please drag the plugins in the cache folder to ur plugins folder manually.")
            z = str(input("[" + Fore.BLUE + '>' + Fore.WHITE +"] Path: "))
            source_dir = 'cache/'
            target_dir = str(z)

            file_names = os.listdir(source_dir)

            for file_name in file_names:
                shutil.move(os.path.join(source_dir, file_name), target_dir)
            print("Plugins succesfully downloaded and installed!")
            os._exit(1)

        print("[!,X,*,?] This part should be unreachable.")
        os._exit(0)
    except:
        pass
    
# ❤ Sorry, spam code ahead.
def BDF():
    print("[*] Downloading 0BDFDB")
    open('cache/0BDFDB.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998891012615307284/0BDFDB.plugin.js', allow_redirects=True).content)
def IXe():
    print("[*] Downloading 1XenoLib")
    open('cache/1XenoLib.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998714001280221194/1XenoLib.plugin.js', allow_redirects=True).content)
def BSP():
    print("[*] Downloading BetterSearchPage")
    open('cache/BetterSearchPage.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998714001523474432/BetterSearchPage.plugin.js', allow_redirects=True).content)
def BRH():
    print("[*] Downloading BugReportHelper")
    open('cache/BugReportHelper.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998714001766752367/BugReportHelper.plugin.js', allow_redirects=True).content)
def CTC():
    print("[*] Downloading CallTimeCounter")
    open('cache/CallTimeCounter.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998714002022613062/CallTimeCounter.plugin.js', allow_redirects=True).content)
def CRD():
    print("[*] Downloading CreationDate")
    open('cache/CreationDate.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998714002504941658/CreationDate.plugin.js', allow_redirects=True).content)
def DFE():
    print("[*] Downloading DiscordFreeEmojis64px")
    open('cache/DiscordFreeEmojis64px.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713970816991334/DiscordFreeEmojis64px.plugin.js', allow_redirects=True).content)
def DCE():
    print("[*] Downloading DoubleClickToEdit")
    open('cache/DoubleClickToEdit.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713971118977024/DoubleClickToEdit.plugin.js', allow_redirects=True).content)
def ESS():
    print("[*] Downloading EmojiStatistics")
    open('cache/EmojiStatistics.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713971584548895/EmojiStatistics.plugin.js', allow_redirects=True).content)
def FVR():
    print("[*] Downloading FileViewer")
    open('cache/FileViewer.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713971924291626/FileViewer.plugin.js', allow_redirects=True).content)
def TRO():
    print("[*] Downloading ThemeRepo")
    open('cache/ThemeRepo.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713912813953125/ThemeRepo.plugin.js', allow_redirects=True).content)
def TPI():
    print("[*] Downloading TypingIndicator")
    open('cache/TypingIndicator.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713913774444684/TypingIndicator.plugin.js', allow_redirects=True).content)
def HCI():
    print("[*] Downloading HideChatIcons")
    open('cache/HideChatIcons.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713972247236738/HideChatIcons.plugin.js', allow_redirects=True).content)
def IIG():
    print("[*] Downloading InvisibleTyping")
    open('cache/InvisibleTyping.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713972549239004/InvisibleTyping.plugin.js', allow_redirects=True).content)
def MLV():
    print("[*] Downloading MessageLoggerV2")
    open('cache/MessageLoggerV2.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713972884787351/MessageLoggerV2.plugin.js', allow_redirects=True).content)
def OTB():
    print("[*] Downloading OldTitleBar")
    open('cache/OldTitleBar.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713973157404692/OldTitleBar.plugin.js', allow_redirects=True).content)
def PVR():
    print("[*] Downloading PermissionsViewer")
    open('cache/PermissionsViewer.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713973706850374/PermissionsViewer.plugin.js', allow_redirects=True).content)
def RMS():
    print("[*] Downloading RedditMentions")
    open('cache/RedditMentions.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713974054989885/RedditMentions.plugin.js', allow_redirects=True).content)
def SHC():
    print("[*] Downloading ShowHiddenChannels")
    open('cache/ShowHiddenChannels.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713911383699486/ShowHiddenChannels.plugin.js', allow_redirects=True).content)
def SLM():
    print("[*] Downloading SplitLargeMessages")
    open('cache/SplitLargeMessages.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713911736025199/SplitLargeMessages.plugin.js', allow_redirects=True).content)
def SFT():
    print("[*] Downloading StaffTag")
    open('cache/StaffTag.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713912075747328/StaffTag.plugin.js', allow_redirects=True).content)
def TEX():
    print("[*] Downloading TeX")
    open('cache/TeX.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713912507764806/TeX.plugin.js', allow_redirects=True).content)
def TRS():
    print("[*] Downloading Translator")
    open('cache/Translator.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713913497616464/Translator.plugin.js', allow_redirects=True).content)
def UBY():
    print("[*] Downloading UrbanDictionary")
    open('cache/UrbanDictionary.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713913774444684/TypingIndicator.plugin.js', allow_redirects=True).content)
def ZPL():
    print("[*] Downloading ZeresPluginLibrary")
    open('cache/ZeresPluginLibrary.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998714000323907604/0PluginLibrary.plugin.js', allow_redirects=True).content) 
    
    # ⚙ Start downloading user needs

    if "1" in prvdownloads:
        BDF()
    if "2" in prvdownloads:
        IXe()
    if "3" in prvdownloads:
        BSP()
    if "4" in prvdownloads:
        BRH()
    if "5" in prvdownloads:
        CTC()
    if "6" in prvdownloads:
        CRD()
    if "7" in prvdownloads:
        DFE()
    if "8" in prvdownloads:
        DCE()
    if "9" in prvdownloads:
        ESS()
    if "0" in prvdownloads:
        FVR()
    MoveToPluginsFolder()


# 💬 It is almost the same code as in function DownloadZONE()
def downloadAll():
        # 🚮 Remove the previous one to remove the old versions if updated.
        if os.path.exists("cache"):
            print("[-] Removing previous cache")
            shutil.rmtree("cache")
        
        # 💬 It is best if we create a cache folder first and after that we move the plugins.
        print("[+] Creating cache folder")
        os.mkdir("cache")
        print("[*] Downloading 0BDFDB")
        open('cache/0BDFDB.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998891012615307284/0BDFDB.plugin.js', allow_redirects=True).content)
        print("[*] Downloading 1XenoLib")
        open('cache/1XenoLib.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713788054376448/1XenoLib.plugin.js', allow_redirects=True).content)
        print("[*] Downloading BetterSearchPage")
        open('cache/BetterSearchPage.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998714001523474432/BetterSearchPage.plugin.js', allow_redirects=True).content)
        print("[*] Downloading BugReportHelper")
        open('cache/BugReportHelper.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998714001766752367/BugReportHelper.plugin.js', allow_redirects=True).content)
        print("[*] Downloading CallTimeCounter")
        open('cache/CallTimeCounter.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998714002022613062/CallTimeCounter.plugin.js', allow_redirects=True).content)
        print("[*] Downloading CreationDate")
        open('cache/CreationDate.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998714002504941658/CreationDate.plugin.js', allow_redirects=True).content)
        print("[*] Downloading DiscordFreeEmojis64px")
        open('cache/DiscordFreeEmojis64px.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713970816991334/DiscordFreeEmojis64px.plugin.js', allow_redirects=True).content)
        print("[*] Downloading DoubleClickToEdit")
        open('cache/DoubleClickToEdit.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713971118977024/DoubleClickToEdit.plugin.js', allow_redirects=True).content)
        print("[*] Downloading EmojiStatistics")
        open('cache/EmojiStatistics.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713971118977024/DoubleClickToEdit.plugin.js', allow_redirects=True).content)
        print("[*] Downloading FileViewer")
        open('cache/FileViewer.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713971924291626/FileViewer.plugin.js', allow_redirects=True).content)
        print("[*] Downloading ThemeRepo")
        open('cache/ThemeRepo.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713912813953125/ThemeRepo.plugin.js', allow_redirects=True).content)
        print("[*] Downloading TypingIndicator")
        open('cache/TypingIndicator.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713913774444684/TypingIndicator.plugin.js', allow_redirects=True).content)
        print("[*] Downloading HideChatIcons")
        open('cache/HideChatIcons.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713972247236738/HideChatIcons.plugin.js', allow_redirects=True).content)
        print("[*] Downloading InvisibleTyping")
        open('cache/InvisibleTyping.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713972549239004/InvisibleTyping.plugin.js', allow_redirects=True).content)
        print("[*] Downloading MessageLoggerV2")
        open('cache/MessageLoggerV2.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713972884787351/MessageLoggerV2.plugin.js', allow_redirects=True).content)
        print("[*] Downloading OldTitleBar")
        open('cache/OldTitleBar.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713973157404692/OldTitleBar.plugin.js', allow_redirects=True).content)
        print("[*] Downloading PermissionsViewer")
        open('cache/PermissionsViewer.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713973706850374/PermissionsViewer.plugin.js', allow_redirects=True).content)
        print("[*] Downloading RedditMentions")
        open('cache/RedditMentions.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713974054989885/RedditMentions.plugin.js', allow_redirects=True).content)
        print("[*] Downloading ShowHiddenChannels")
        open('cache/ShowHiddenChannels.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713911383699486/ShowHiddenChannels.plugin.js', allow_redirects=True).content)
        print("[*] Downloading SplitLargeMessages")
        open('cache/SplitLargeMessages.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713911736025199/SplitLargeMessages.plugin.js', allow_redirects=True).content)
        print("[*] Downloading StaffTag")
        open('cache/StaffTag.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713912075747328/StaffTag.plugin.js', allow_redirects=True).content)
        print("[*] Downloading TeX")
        open('cache/TeX.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713912507764806/TeX.plugin.js', allow_redirects=True).content)
        print("[*] Downloading Translator")
        open('cache/Translator.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713913497616464/Translator.plugin.js', allow_redirects=True).content)
        print("[*] Downloading UrbanDictionary")
        open('cache/UrbanDictionary.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998713914063855616/UrbanDictionary.plugin.js', allow_redirects=True).content)
        print("[*] Downloading ZeresPluginLibrary")
        open('cache/ZeresPluginLibrary.plugin.js', 'wb').write(requests.get('https://cdn.discordapp.com/attachments/970075719310929940/998714000323907604/0PluginLibrary.plugin.js', allow_redirects=True).content)  
        print("[v] Downloads completed, please wait while we move the files to the plugin folder.")
        MoveToPluginsFolder()

# 💬 Main UI
def main():
    print(Style.RESET_ALL)

    print(Fore.WHITE + '         A better ' + Fore.BLUE + 'Better' + Fore.WHITE + "Discord Plugins Installer")
    print("               Last updated " + Fore.CYAN + "2022 July 19")

    print(Fore.WHITE + " ")

    print("Bunch of plugins listed below, please choose what u want")
    print("             Type '" + Fore.CYAN + "ALL" + Fore.WHITE + "' to install everything")

    print(Style.RESET_ALL)

    print("(1) 0BDFDB                                  (h) HideChatIcons         ")
    print("(2) 1XenoLib                                (i) InvisibleTyping       ")
    print("(3) BetterSearchPage                        (m) MessageLoggerV2       ")
    print("(4) BugReportHelper                         (o) OldTitleBar           ")
    print("(5) CallTimeCounter                         (p) PermissionsViewer     ")
    print("(6) CreationDate                            (r) RedditMentions        ")
    print("(7) DiscordFreeEmojis64px                   (s) ShowHiddenChannels    ")
    print("(8) DoubleClickToEdit                       (l) SplitLargeMessages    ")
    print("(9) EmojiStatistics                         (f) StaffTag              ")
    print("(0) FileViewer                              (t) TeX                   ")
    print("(r) ThemeRepo                               (b) Translator            ")
    print("(c) TypingIndicator                         (u) UrbanDictionary       ")
    print("(z) ZeresPluginLibrary                      ")

    print(Style.RESET_ALL)
    
    x = str(input("[>] Choices: "))
    if x == "ALL":
        x = "install.all"
    if x == "alL":
        x = "install.all"
    if x == "all":
        x = "install.all"
    if x == "All":
        x = "install.all"
    if x == "aLl":
        x = "install.all"
    if x == "ALl":
        x = "install.all"
    if x == "aLL":
        x = "install.all"

    cls()

    print(Style.RESET_ALL)  
    print(Fore.WHITE + '         A better ' + Fore.BLUE + 'Better' + Fore.WHITE + "Discord Plugins Installer")
    print("               Last updated " + Fore.CYAN + "2022 July 19")  
    print(Fore.WHITE + " ")

    if x == "install.all":
        downloadAll()
    else: 
        # ✨ Start of actual check
        if "1" in x:
            BDF()
        if "2" in x:
            IXe()
        if "3" in x:
            BSP()
        if "4" in x:
            BRH()
        if "5" in x:
            CTC()
        if "6" in x:
            CRD()
        if "7" in x:
            DFE()
        if "8" in x:
            DCE()
        if "9" in x:
            ESS()
        if "0" in x:
            FVR()
        if "r" in x:
            BDF()
        if "c" in x:
            BDF()
        if "z" in x:
            ZPL()
        if "h" in x:
            HCI()
        if "i" in x:
            IIG()
        if "m" in x:
            MLV()
        if "o" in x:
            OTB()
        if "p" in x:
            PVR()
        if "r" in x:
            RMS()
        if "s" in x:
            SHC()
        if "l" in x:
            SLM()
        if "f" in x:
            SFT()
        if "t" in x:
            TEX()
        if "b" in x:
            TRS()
        if "u" in x:
            UBY()
        print("[v] Downloads completed, please wait while we move the files to the plugin folder.")
        MoveToPluginsFolder()

# 🔧 If you are here to change code, this is the best thing u can change
main()