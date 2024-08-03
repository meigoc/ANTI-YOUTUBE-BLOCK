import os
import time
import sys

def print_main(text):
    red_code = "\033[38;2;255;0;0m"
    reset_code = "\033[0m"
    print(f"{red_code}{text}{reset_code}")

def print_done(text):
    red_code = "\033[38;2;255;0;0m"
    reset_code = "\033[0m"
    print(f"{red_code}{text}{reset_code}")

def print_choice1(text):
    red_code = "\033[38;2;255;0;0m"
    reset_code = "\033[0m"
    print(f"{red_code}{text}{reset_code}")

def print_choice3(text):
    red_code = "\033[38;2;255;0;0m"
    reset_code = "\033[0m"
    print(f"{red_code}{text}{reset_code}")

def print_choice4(text):
    red_code = "\033[38;2;255;0;0m"
    reset_code = "\033[0m"
    print(f"{red_code}{text}{reset_code}")



def main():
    sys.stdout.write('\033c')
    sys.stdout.flush()
    print_main("""

              ▄████████ ███▄▄▄▄       ███      ▄█  ▀█████████▄   ▄█        ▄██████▄   ▄████████    ▄█   ▄█▄ 
             ███    ███ ███▀▀▀██▄ ▀█████████▄ ███    ███    ███ ███       ███    ███ ███    ███   ███ ▄███▀ 
             ███    ███ ███   ███    ▀███▀▀██ ███▌   ███    ███ ███       ███    ███ ███    █▀    ███▐██▀   
             ███    ███ ███   ███     ███   ▀ ███▌  ▄███▄▄▄██▀  ███       ███    ███ ███         ▄█████▀    
           ▀███████████ ███   ███     ███     ███▌ ▀▀███▀▀▀██▄  ███       ███    ███ ███        ▀▀█████▄    
             ███    ███ ███   ███     ███     ███    ███    ██▄ ███       ███    ███ ███    █▄    ███▐██▄   
             ███    ███ ███   ███     ███     ███    ███    ███ ███▌    ▄ ███    ███ ███    ███   ███ ▀███▄ 
             ███    █▀   ▀█   █▀     ▄████▀   █▀   ▄█████████▀  █████▄▄██  ▀██████▀  ████████▀    ███   ▀█▀ 
                                                                       ▀                                 ▀      
                      
                      
                                                   ✦ Создатель - MrFa ✦                                                                                                                                                                                                                                                                                                   
""")
     
    choice = input("""
                                          Выберите действие:
                                          1. Обойти блокировку Ai (DNS)
                                          2. Обход замедления YouTube (DNS)
                                          3. Обход замедления YouTube (Скрипт)
                                          4. Выход
                                          """)

    if choice == "1":
        ai_dns()
    elif choice == "2":
        youtube_dns()
    elif choice == "3":
        youtube_script()
    elif choice == "4":
        exit()
    else:
        print("Неверный выбор.")

def ai_dns():
    print("Скоро...")
    time.sleep(3)
    main()

def youtube_dns():
    sys.stdout.write('\033c')
    sys.stdout.flush()
    print_choice4("""

              ▄████████ ███▄▄▄▄       ███      ▄█  ▀█████████▄   ▄█        ▄██████▄   ▄████████    ▄█   ▄█▄ 
             ███    ███ ███▀▀▀██▄ ▀█████████▄ ███    ███    ███ ███       ███    ███ ███    ███   ███ ▄███▀ 
             ███    ███ ███   ███    ▀███▀▀██ ███▌   ███    ███ ███       ███    ███ ███    █▀    ███▐██▀   
             ███    ███ ███   ███     ███   ▀ ███▌  ▄███▄▄▄██▀  ███       ███    ███ ███         ▄█████▀    
           ▀███████████ ███   ███     ███     ███▌ ▀▀███▀▀▀██▄  ███       ███    ███ ███        ▀▀█████▄    
             ███    ███ ███   ███     ███     ███    ███    ██▄ ███       ███    ███ ███    █▄    ███▐██▄   
             ███    ███ ███   ███     ███     ███    ███    ███ ███▌    ▄ ███    ███ ███    ███   ███ ▀███▄ 
             ███    █▀   ▀█   █▀     ▄████▀   █▀   ▄█████████▀  █████▄▄██  ▀██████▀  ████████▀    ███   ▀█▀ 
                                                                       ▀                                 ▀      
                      
                      
                                                   ✦ Создатель - MrFa ✦                                                                                                                                                                                                                                                                                                    
""")
    
    choice = input("""
                                            Выберите действие:
                                        1. Использовать этот обход только на БЕСПРОВОДНОМ ИНТЕРНЕТЕ
                                        2. Использовать этот обход только на ПРОВОДНОМ ИНТЕРНЕТЕ
                                        3. Использовать этот обход НА ВСЕХ ВИДАХ ИНТЕРНЕТА
                                        4. Меню
                                        5. Выход
                                          """)
    

    if choice == 1:
        os.startfile("component\\youtube_dns\wifi.bat" 'runas')
        youtube_dns()
    if choice == 2:
        os.startfile("component\\youtube_dns\etherner.bat" 'runas')
        youtube_dns()
    elif choice == 3:
        os.startfile("component\\youtube_dns\we.bat" 'runas')
        youtube_dns()
    elif choice == 4:
        main()
    else:
        print("Неверный выбор.")






    
    main()

def youtube_script():

    sys.stdout.write('\033c')
    sys.stdout.flush()
    print_choice1("""

              ▄████████ ███▄▄▄▄       ███      ▄█  ▀█████████▄   ▄█        ▄██████▄   ▄████████    ▄█   ▄█▄ 
             ███    ███ ███▀▀▀██▄ ▀█████████▄ ███    ███    ███ ███       ███    ███ ███    ███   ███ ▄███▀ 
             ███    ███ ███   ███    ▀███▀▀██ ███▌   ███    ███ ███       ███    ███ ███    █▀    ███▐██▀   
             ███    ███ ███   ███     ███   ▀ ███▌  ▄███▄▄▄██▀  ███       ███    ███ ███         ▄█████▀    
           ▀███████████ ███   ███     ███     ███▌ ▀▀███▀▀▀██▄  ███       ███    ███ ███        ▀▀█████▄    
             ███    ███ ███   ███     ███     ███    ███    ██▄ ███       ███    ███ ███    █▄    ███▐██▄   
             ███    ███ ███   ███     ███     ███    ███    ███ ███▌    ▄ ███    ███ ███    ███   ███ ▀███▄ 
             ███    █▀   ▀█   █▀     ▄████▀   █▀   ▄█████████▀  █████▄▄██  ▀██████▀  ████████▀    ███   ▀█▀ 
                                                                       ▀                                 ▀      
                      
                      
                                                   ✦ Создатель - MrFa ✦                                                                                                                                                                                                                                                                                                    
""")

    choice = input("""
                                                    Выберите действие:
                                                    1. Применить скрипт
                                                    2. Откатить скрипт
                                                    3. Меню
                                                    4. Выход
                                          """)
    

    if choice == "1":
        os.startfile("component\\service_install_russia_blacklist.cmd", 'runas')
        time.sleep(3)
        os.startfile("component\\service_install_russia_blacklist_dnsredir.cmd", 'runas')
    sys.stdout.write('\033c')
    sys.stdout.flush() 
    if choice == "2":
        os.startfile("component\\service_remove.cmd", 'runas')
    elif choice == "3":
        main()
    elif choice == "4":
        exit()
    else:
        print("Неверный выбор.")




if __name__ == "__main__":
    main()