@echo off


start cmd /k "cls && echo... && timeout /t 2 >nul && color 0A && for /l %%i in (1,1,10000) do (set /a rand=!random! %% 94 + 33 && <nul set /p =!rand! && timeout /t 0 >nul) && echo. && echo Acceso concedido. && pause >nul"
