# - Notes:
# Time.sleep commands are for preventing eye shock for some users' health.
# This project is managed in Jira®
# This project is available in Github


# - SOT variables
sot_lv1 = "Debian, Ubuntu, Pardus, Linux LITE, Fedora"
sot_lv2 = "Debian, Fedora, Ubuntu, Pardus, Linux LITE, Arch Linux, Linux Mint, Fuduntu, CentOS, Linux XP, Lubuntu, Xubuntu, Edubuntu"
sot_lv3 = "Debian, Fedora, Ubuntu, Pardus, Linux LITE, Arch Linux, Linux Mint, Fuduntu, CentOS, Linux XP, Lubuntu, Xubuntu, Edubuntu, Parrot Architect, Zorin OS, Parrot Home"
sot_lv4 = "Debian, Fedora, Ubuntu, Pardus, Linux LITE, Arch Linux, Linux Mint, Fuduntu, CentOS, Linux XP, Lubuntu, Xubuntu, Edubuntu, Parrot Architect, Zorin OS, Parrot Home, ParrotSEQ, Kali Linux, Parrot HTB, Astra OS, Devuan, BOSS Linux, Sacix, Vyatta, Blackarch, Manjaro, KaOS, ChromeOS, ChromiumOS, Fire OS, Oracle Linux, Redhat Enterprise, Redhat"
# - SOT MOBILE variables
sot_lv2MOBILE = "Ubuntu Touch, Fedora, Flash Linux, PostmarketOS, Sailfish, Mobian, Pure OS, Plasma Mobile"
sot_lv3MOBILE = "Ubuntu Touch, Fedora, Flash Linux, PostmarketOS, Sailfish, Mobian, Pure OS, Plasma Mobile"
sot_lv4MOBILE = "Ubuntu Touch, Fedora, Flash Linux, PostmarketOS, Sailfish, Mobian, Pure OS, Plasma Mobile, Nethunter"
# - Coding variables
coding_lv1 = "Ubuntu, Parrot Architect, Parrot Home, Fedora, Linux MINT"
coding_lv2 = "Ubuntu, Parrot Architect, Parrot Home, Fedora, Linux MINT, Arch Linux, Xubuntu, Lubuntu, OpenSUSE, Redhat, Debian" 
coding_lv3 = "Ubuntu, Parrot Architect, Parrot Home, Fedora, Linux MINT, Arch Linux, Xubuntu, Lubuntu, OpenSUSE, Redhat, Debian, Asianux, Oracle Linux, Kali Linux, ParrotSEC, Red Flag Linux"
coding_lv4 = "Ubuntu, Parrot Architect, Parrot Home, Fedora, Linux MINT, Arch Linux, Xubuntu, Lubuntu, OpenSUSE, Redhat, Debian, Asianux, Oracle Linux, Kali Linux, ParrotSEC, Red Flag Linux, BlackArch, Miracle Linux, Scientific Linux, Fuduntu, Trustix"
# - Hosting variables
hosting = "AlmaLinux, Rocky Linux, Ubuntu Server, Debian, Fedora Server, Red Hat Enterprise Linux, Ubuntu"
# - Pentesting variables
pentesting_lv1 = "Ubuntu, Lubuntu, Xubuntu, Debian, Kubuntu, Ubuntu MATE, Ubuntu Studio"
pentesting_lv2 = "Ubuntu, Lubuntu, Xubuntu, Debian, Kubuntu, Ubuntu MATE, Ubuntu Studio, Parrot Home, Parrot Architect, Gobuntu, Cub Linux, gOS"
pentesting_lv3 = "Ubuntu, Lubuntu, Xubuntu, Debian, Kubuntu, Ubuntu MATE, Ubuntu Studio, Parrot Home, Parrot Architect, Gobuntu, Cub Linux, gOS, ParrotSEC, Parrot HTB, Kali Linux, BlackArch"
pentesting_lv4 = "Ubuntu, Lubuntu, Xubuntu, Debian, Kubuntu, Ubuntu MATE, Ubuntu Studio, Parrot Home, Parrot Architect, Gobuntu, Cub Linux, gOS, ParrotSEC, Parrot HTB, Kali Linux, BlackArch, Arch Linux, Backbox, Bodhi Linux, Joli OS, KDE Neon, Nova"
pentesting_MOBILE = "Ubuntu Touch, Fedora, Flash Linux, PostmarketOS, Sailfish, Mobian, Pure OS, Plasma Mobile, Nethunter"


# - Modules
import time
import timeit


print("Currently running deepfind Linux distribution chooser Beta-1.0.")
print("WARNING: IF YOU INSTALLED ONE OF THESE OPERATING SYSTEMS AND YOUR PC COULDN'T HANDLE IT, IT IS NOT OUR PROBLEM.")
# - (Added time.sleep for the user to read the warning and the version.)
time.sleep(5)

quest1 = input("Which activities do you do the most? Type the number. 1: Surfing on the internet 2: Coding  3: Hosting 4: Penetration Testing: ")
# - (Added time.sleep to prevent eye shock for some users.)
time.sleep(3)

# - SURFING ON THE INTERNET (CONDITIONS)

if quest1 == "1":
     sot1 = input("How would you describe your internet knowledge level? Type the number. 1: Beginner 2: Intermediate 3: Advanced 4: Wise: ")
     time.sleep(3)

     if sot1 == "1":
          print("The recommended Linux distributions for you are: Debian, Ubuntu, Pardus, Linux LITE, Fedora.")
          time.sleep(120)
     

     if sot1 == "2":
          mobileopt = input("There are mobile versions available for you. Would you like to view them? |1: Yes|2: No|")
          if mobileopt == "2":
               print("The recommended Linux distributions for you are: Debian, Fedora, Ubuntu, Pardus, Linux LITE, Arch Linux, Linux Mint, Fuduntu, CentOS, Linux XP, Lubuntu, Xubuntu, Edubuntu.")
               time.sleep(120)
          if mobileopt == "1":
               print("The recommended mobile versions for you are: ", sot_lv2MOBILE)
               time.sleep(120)
               

     if sot1 == "3":
          mobileopt = input("There are mobile versions available for you. Would you like to view them? |1: Yes|2: No|")
          if mobileopt == "2":
               print("The recommended Linux distributions for you are: Debian, Fedora, Ubuntu, Pardus, Linux LITE, Arch Linux, Linux Mint, Fuduntu, CentOS, Linux XP, Lubuntu, Xubuntu, Edubuntu, Parrot Architect, Zorin OS, Parrot Home.")
               time.sleep(120)
          if mobileopt == "1":
               print("The recommended mobile versions for you are: ", sot_lv3MOBILE)
               time.sleep(120)

     if sot1 == "4":
          time.sleep(120)
          mobileopt = input("There are mobile versions available for you. Would you like to view them? |1: Yes|2: No|")
          if mobileopt == "2":
               print("The recommended Linux distributions for you are: Debian, Fedora, Ubuntu, Pardus, Linux LITE, Arch Linux, Linux Mint, Fuduntu, CentOS, Linux XP, Lubuntu, Xubuntu, Edubuntu, Parrot Architect, Zorin OS, Parrot Home, ParrotSEQ, Kali Linux, Parrot HTB, Astra OS, Devuan, BOSS Linux, Sacix, Vyatta, Blackarch, Manjaro, KaOS, ChromeOS, ChromiumOS, Fire OS, Oracle Linux, Redhat Enterprise, Redhat.")
               time.sleep(120)
          if mobileopt == "1":
               print("The recommended mobile versions for you are: ", sot_lv4MOBILE)
               time.sleep(120)


# - CODING (CONDITIONS)

if quest1 == "2":
     coding1 = input("How would you describe your experience level? Type the number. 1: Beginner 2: Intermediate 3: Student 4: Developer: ")
     time.sleep(3)

     if coding1 == "1":
          print("The recommended Linux distributions for you are: Ubuntu, Parrot Architect, Parrot Home, Fedora, Linux MINT")
          time.sleep(120)

     if coding1 == "2":
          print("The recommended Linux distributions for you are: Ubuntu, Parrot Architect, Parrot Home, Fedora, Linux MINT, Arch Linux, Xubuntu, Lubuntu, OpenSUSE, Redhat, Debian.")
          time.sleep(120)

     if coding1 == "3":
          print("The recommended Linux distributions for you are: Ubuntu, Parrot Architect, Parrot Home, Fedora, Linux MINT, Arch Linux, Xubuntu, Lubuntu, OpenSUSE, Redhat, Debian, Asianux, Oracle Linux, Kali Linux, ParrotSEC, Red Flag Linux")
          time.sleep(120)

     if coding1 == "4":
          print("The recommended Linux distributions for you are: Ubuntu, Parrot Architect, Parrot Home, Fedora, Linux MINT, Arch Linux, Xubuntu, Lubuntu, OpenSUSE, Redhat, Debian, Asianux, Oracle Linux, Kali Linux, ParrotSEC, Red Flag Linux, BlackArch, Miracle Linux, Scientific Linux, Fuduntu, Trustix")
          time.sleep(120)


# - HOSTING (CONDITIONS)
if quest1 == "3":
     hosting1 = input("What is you job title? Type the number. 1: Server Manager 2: Master in SQL/SSH 3: Advanced 4: Wise: ")
     time.sleep(3)

     if hosting1 == "1" or "2" or "3" or "4":
          print("The recommended Linux distributions for you / your company are: AlmaLinux, Rocky Linux, Ubuntu Server, Debian, Fedora Server, Red Hat Enterprise Linux, Ubuntu")
          time.sleep(120)

# - PENTESTING (CONDITIONS)
if quest1 == "4":
     pts1 = input("What is your job? Type the number. 1: Backend Developer 2: Freelance Developer 3: Cybersecurity Engineer 4: IT Manager: ")
     time.sleep(3)

     if pts1 == "1":
          mobileopt = input("There are mobile versions available for you. Would you like to view them? |1: Yes|2: No|")
          if mobileopt == "2":
               print("The recommended Linux distributions for you are: Ubuntu, Lubuntu, Xubuntu, Debian, Kubuntu, Ubuntu MATE, Ubuntu Studio")
               time.sleep(120)
          if mobileopt == "1":
               print("The recommended mobile versions for you are: ", pentesting_MOBILE)
               time.sleep(120)

     if pts1 == "2":
          mobileopt = input("There are mobile versions available for you. Would you like to view them? |1: Yes|2: No|")
          if mobileopt == "2":
               print("The recommended Linux distributions for you are: Ubuntu, Lubuntu, Xubuntu, Debian, Kubuntu, Ubuntu MATE, Ubuntu Studio, Parrot Home, Parrot Architect, Gobuntu, Cub Linux, gOS")
               time.sleep(120)
          if mobileopt == "1":
               print("The recommended mobile versions for you are: ", pentesting_MOBILE)
               time.sleep(120)

     if pts1 == "3":
          time.sleep(120)
          mobileopt = input("There are mobile versions available for you. Would you like to view them? |1: Yes|2: No|")
          if mobileopt == "2":
               print("The recommended Linux distributions for you are: Ubuntu, Lubuntu, Xubuntu, Debian, Kubuntu, Ubuntu MATE, Ubuntu Studio, Parrot Home, Parrot Architect, Gobuntu, Cub Linux, gOS, ParrotSEC, Parrot HTB, Kali Linux, BlackArch")
               time.sleep(120)
          if mobileopt == "1":
               print("The recommended mobile versions for you are: ", pentesting_MOBILE)
               time.sleep(120)

     if pts1 == "4":
          time.sleep(120)
          mobileopt = input("There are mobile versions available for you. Would you like to view them? |1: Yes|2: No|")
          if mobileopt == "2":
               print("The recommended Linux distributions for you are: Ubuntu, Lubuntu, Xubuntu, Debian, Kubuntu, Ubuntu MATE, Ubuntu Studio, Parrot Home, Parrot Architect, Gobuntu, Cub Linux, gOS, ParrotSEC, Parrot HTB, Kali Linux, BlackArch, Arch Linux, Backbox, Bodhi Linux, Joli OS, KDE Neon, Nova")
               time.sleep(120)
          if mobileopt == "1":
               print("The recommended mobile versions for you are: ", pentesting_MOBILE)
               time.sleep(120)

exitquestion = input("Do you want to quit this app?| 1: Yes | 2: No |")
if exitquestion == "1":
     exit()

if exitquestion == "2":
     while True:
          time.sleep(30)
          exit2 = input("Do you want to quit this app?| 1: Yes | 2: No |")
          if exit2 == "1":
               exit()
               

