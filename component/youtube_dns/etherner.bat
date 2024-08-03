@echo off
cls
set dns_server=8.8.8.8
cls
netsh interface ip set dns "Ethernet" static %dns_server%
cls
netsh interface ip set dns "Проводной" static %dns_server%
cls
netsh interface ip set dns "Проводная сеть" static %dns_server%cls
