@echo off
cls
set dns_server=8.8.8.8
cls
netsh interface ip set dns "Беспроводная сеть" static %dns_server%
cls
netsh interface ip set dns "Wi-Fi" static %dns_server%
cls
netsh interface ip set dns "WiFi" static %dns_server%
cls