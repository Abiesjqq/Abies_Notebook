## 创建

新建.txt文件，在记事本中编辑，再将后缀转为.bat，双击运行。（或在Notepad++中编辑？没试过……）

## ECHO

```bat
rem do not show instructions
@echo off

rem echo the following sentence (do not need quotation marks)
echo This is the first line of the program.

rem set variables and call variables
set layout=Hello, world!
echo %layout%

rem /A means Arithmetic
set /A first=10
set /A second=20
set /A add=%first%+%second%
echo sum is %add%

rem set global and local variables
set /A globalVariable=1
SETLOCAL
set /A localVariable=%glabalVariable%+2
echo Global variable is %globalVariable%
echo Local variable is %localVariable%
ENDLOCAL

```

## 字符串操作

```bat
@echo off

rem judge whether a variable is empty
set a=Hi, world
set z=
if [%a%]==[] echo a is empty!
if [%z%]==[] echo z is empty!

rem Substring: <string>:~<begin>[,length]
set str=HiAbies
echo.%str%
set str=%str:~0,2%
echo.%str%

rem Replace: <string>:<old>=<new>
set str=Hi, my name is abies
set str=%str:abies=Abies%
echo.%str%

```

## 循环

```bat
@echo off

rem /l means loop
rem %%i means i is a loop variable
for /l %%i in (1,1,10) do (
    echo step %%i
)

rem traverse a specific list, can not use /l
set myArray=1 2 4 5 6
for %%i in (%myArray%) do (
    echo step %%i
)

rem while loop
rem call is used to handle nested expansion
setlocal enabledelayedexpansion
set myArr[0]=1
set myArr[1]=7
set myArr[2]=13
set i=0
:myloop
if defined myArr[!i!] (
    set tmp=myArr[!i!]
    echo Element !i! = !tmp!
    set /a "i+=1"
    GOTO :myloop
)
```

## 文件操作

```bat
@echo off

rem input text into file
echo hold me in the darkness > temp.txt

rem echo contents of fole
rem /f means file, "tokens=*" means read the whole line
for /f "tokens=*" %%x in (temp.txt) do (echo %%x)
```

## 示例

### 批量重命名照片

```bat
@echo off
setlocal enabledelayedexpansion
set count=1000
:: start from 1001, thus the last 3 bits starting from 001

for %%f in (*.jpg) do (
    set /a count+=1
    ren "%%f" "Fig_!count:~-3!.jpg"
)
echo Finish!
pause

```

### 格式化记录日志

```bat
@echo off
set /p task=What do you do today?
echo [%date% %time%] %task% >> work_log.txt
echo Finish recording in work_log.txt
pause
```

### Git提交

```bat
@echo off

set "repos=D:\Blog D:\AAAmkdocs\MkDocs-Guide"
for %%r in (%repos%) do (
    call :auto_commit "%%r"
)

pause
goto :eof

:auto_commit
cd /d %1

git add .

git diff --cached --quiet
if %errorlevel% equ 1 (
    for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
    set "date_str=%dt:~0,4%-%dt:~4,2%-%dt:~6,2%"
    git commit -m "Auto-commit on %date_str%"

    echo.
    echo Repository: %1
    echo Files changed:
    git show --name-only --format=""

    git push origin auto-commit

    echo.
    echo Finish commiting!
) else (
    echo.
    echo No changes detected in repository %1.
)
exit /b
```