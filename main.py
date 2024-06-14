import os
import sys
import time
import pystyle
import webbrowser
import ctypes

# @author JohON0

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

new_title = "Centric Loader (gbxm soso)"
set_console_title(new_title)

banner = ("""

    ░█████╗░███████╗███╗░░██╗████████╗██████╗░██╗░█████╗░
    ██╔══██╗██╔════╝████╗░██║╚══██╔══╝██╔══██╗██║██╔══██╗
    ██║░░╚═╝█████╗░░██╔██╗██║░░░██║░░░██████╔╝██║██║░░╚═╝
    ██║░░██╗██╔══╝░░██║╚████║░░░██║░░░██╔══██╗██║██║░░██╗
    ╚█████╔╝███████╗██║░╚███║░░░██║░░░██║░░██║██║╚█████╔╝
    ░╚════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░╚════╝░
""")
author = ("made with love by JohON0"
          "")

print(pystyle.Col.purple + banner)
print(author)

nickname = input(pystyle.Col.white + "Введите ваш ник: ")

if 3 <= len(nickname) <= 16:
    print(pystyle.Col.gray + "Ваш никнейм:", nickname)
else:
    print(pystyle.Col.red + "Никнейм должен содержать от 3 до 16 символов. Лоадер закроется через 5 секунд...")
    time.sleep(5)
    sys.exit()

ozu = input(pystyle.Col.white + "Введите кол-во оперативной памяти (пример 2): ")

if len(ozu) <= 8:
    print(pystyle.Col.gray + "Вы выделили:", ozu + "GB")
else:
    print(pystyle.Col.red + "Максимальное выделение ОЗУ 8GB! Лоадер закроется через 5 секунд...")
    time.sleep(5)
    sys.exit()

print(pystyle.Col.green + "Запускаю чит. Лоадер можно закрыть :-)")

command = fr'.\start\jdk\bin\javaw.exe "-Dos.name=Windows 10" -Dos.version=10.0 -Djava.library.path=natives -cp .\start\libraries\*;minecraft.jar; -Xmx{ozu}G -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M -Dfml.ignoreInvalidMinecraftCertificates=true -Dfml.ignorePatchDiscrepancies=true -Djava.net.preferIPv4Stack=true -Dminecraft.applet.TargetDirectory=\ net.minecraft.client.main.Main --username {nickname} --version paragoneobfuscator --gameDir \ --assetsDir assets --assetIndex 1.16.5 --uuid ce01a476407d4287bef896330abe919e --accessToken 0 --userType mojang --versionType release --width 925 --height 530'


tg = 't.me/centricclient'
ds = 'discord.gg/JHYHqMUsYT'

webbrowser.open(tg)
webbrowser.open(ds)

os.system(command)
