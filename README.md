# m5camera_mpy_samples

このリポジトリは、M5Camera + OpenMV(MicroPython)のpythonサンプルです。
VSCode + pymakr の使用を前提としています。
  + pymakrはVSCodeのExtensionです。VSCodeを起動し、view -> Extensions で`pymakr`と入力し、インストールしてください

This repository is a python sample of M5Camera + OpenMV (MicroPython).
You must install VSCode and pymakr to use this samples.

# How to use  
1. M5CameraにM5Camera+OpenMVのファームウェアを書き込んでください  
   書き込み手順は、https://github.com/tenpa1105/M5Camera_OpenMV.git のHow to useを参照して下さい  
   Flash micropython binary to M5Camera. Please see https://github.com/tenpa1105/M5Camera_OpenMV.git

2. 本リポジトリをクローンしてください  
   Clone this repository.
```
git clone https://github.com/tenpa1105/m5camera_mpy_samples.git
```
3. VSCodeで、実行するサンプルのディレクトリを開いてください  
   Open sample directory in VSCode.  

4. src/config_sample.pyを環境に合わせて設定してください。設定後、config.pyにrenameしてください  
   Modify `src/config_sample.py` and rename to config.py
```
WIFI_SSID = "please enter your wifi ssid"
WIFI_PASS = "please enter your wifi password"
```
5. 画面下のUploadを押してください  
   Push `Upload` button

![sample](/img/vscode_pymakr.png)

6. src以下の.pyファイルがM5Cameraに転送され、boot.py -> main.py の順に実行されます  
   .py files under src are transferred to M5Camera and executed in the order of boot.py-> main.py.