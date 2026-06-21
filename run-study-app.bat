@echo off
chcp 65001 >nul 2>&1
title Study App - Language Learning Wiki

echo =============================================================
echo     KHOI CHAY UNG DUNG ON TAP NGON NGU (Language Wiki)
echo =============================================================
echo.

:: Menu chon ngon ngu
echo Chon ngon ngu hoc:
echo   [1] Tieng Han (Korean - TOPIK)
echo   [2] Tieng Anh (English - IELTS)
echo.
set /p LANG_CHOICE="Nhap so (1 hoac 2, mac dinh 1): "
if "%LANG_CHOICE%"=="2" (
    set STUDY_LANG=english
    title Study App - English IELTS Learning
    echo.
    echo  Ban da chon: Tieng Anh (English - IELTS)
) else (
    set STUDY_LANG=korean
    title Study App - Korean TOPIK Learning
    echo.
    echo  Ban da chon: Tieng Han (Korean - TOPIK)
)

:: Kiem tra xem co file .current-lang da luu khong
if exist "%~dp0.superpowers\.current-lang" (
    set /p SAVED_LANG=<"%~dp0.superpowers\.current-lang"
    if defined SAVED_LANG (
        set STUDY_LANG=%SAVED_LANG%
        echo  (Da doc ngon ngu da luu truoc do: %SAVED_LANG%)
    )
)

echo.
echo [Step 1/4] Giai phong cac cong 3001 va 5173 neu co tien trinh chay ngam...

:: Giai phong cong 3001
netstat -aon | findstr :3001 > "%TEMP%\port_3001.txt" 2>nul
for /f "usebackq tokens=5" %%a in ("%TEMP%\port_3001.txt") do (
    echo Dang tat tien trinh cu chay ngam tai cong 3001, PID: %%a
    taskkill /f /pid %%a >nul 2>&1
)
del "%TEMP%\port_3001.txt" >nul 2>&1

:: Giai phong cong 5173
netstat -aon | findstr :5173 > "%TEMP%\port_5173.txt" 2>nul
for /f "usebackq tokens=5" %%a in ("%TEMP%\port_5173.txt") do (
    echo Dang tat tien trinh cu chay ngam tai cong 5173, PID: %%a
    taskkill /f /pid %%a >nul 2>&1
)
del "%TEMP%\port_5173.txt" >nul 2>&1

echo.
echo [Step 2/4] Dang khoi dong API Server (%STUDY_LANG%) va Vite Client...
cd /d "%~dp0language-wiki\study-app"
start /b cmd /c "set STUDY_LANG=%STUDY_LANG%&& npm run server"
start /b cmd /c "npm run dev"

echo Dang cho ung dung san sang (kiem tra cong 5173)...
:wait_loop
ping 127.0.0.1 -n 2 >nul
netstat -ano | findstr :5173 >nul
if errorlevel 1 goto wait_loop

echo.
echo [Step 3/4] Khoi dong Trinh duyet...
echo =============================================================
echo  LUU Y QUAN TRONG: 
echo  - KHONG duoc dong cua so den (CMD) nay.
echo  - Sau khi hoc xong, ban chi can DONG CUA SO TRINH DUYET,
echo    cua so CMD nay se tu dong tat server va giai phong cac cong!
echo =============================================================
echo.

:: Thu nghiem mo bang Chrome, neu khong duoc thi dung Edge
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe" >nul 2>&1
if %errorlevel% equ 0 (
    echo Dang mo ung dung bang Google Chrome...
    start /wait chrome.exe --new-window http://localhost:5173/ --user-data-dir="%TEMP%\study-app-chrome-profile"
) else (
    echo Dang mo ung dung bang Microsoft Edge...
    start /wait msedge.exe --new-window http://localhost:5173/ --user-data-dir="%TEMP%\study-app-edge-profile"
)

echo.
echo [Step 4/4] Don dep he thong...
echo Cua so trinh duyet da dong. Dang tu dong tat API Server va Vite...

:: Don dep cong 3001
netstat -aon | findstr :3001 > "%TEMP%\port_3001.txt" 2>nul
for /f "usebackq tokens=5" %%a in ("%TEMP%\port_3001.txt") do (
    taskkill /f /pid %%a >nul 2>&1
)
del "%TEMP%\port_3001.txt" >nul 2>&1

:: Don dep cong 5173
netstat -aon | findstr :5173 > "%TEMP%\port_5173.txt" 2>nul
for /f "usebackq tokens=5" %%a in ("%TEMP%\port_5173.txt") do (
    taskkill /f /pid %%a >nul 2>&1
)
del "%TEMP%\port_5173.txt" >nul 2>&1

echo.
echo Da giai phong cac cong mang 3001 va 5173 thanh cong!
echo Cua so nay se tu dong dong sau 3 giay.
ping 127.0.0.1 -n 4 >nul
