# m5camera_mpy_samples

このリポジトリは、M5Camera + OpenMV(MicroPython)のpythonサンプルです。
VSCode + pymakr の使用を前提としています。
  + pymakrはVSCodeのExtensionです。VSCodeを起動し、view -> Extensions で`pymakr`と入力し、インストールしてください

# How to use  
1. M5CameraにM5Camera+OpenMVのファームウェアを書き込んでください  
   書き込み手順は、https://github.com/tenpa1105/M5Camera_OpenMV.gitのHow to useを参照して下さい
2. 本リポジトリをクローンしてください
```
git clone https://github.com/tenpa1105/m5camera_mpy_samples.git
```
3. VSCodeで、実行するサンプルのディレクトリを開いてください
4. src/config.pyを環境に合わせて設定してください
```
WIFI_SSID = "please enter your wifi ssid"
WIFI_PASS = "please enter your wifi password"
```
5. 画面下のUploadを押してください

![sample](/img/vscode_pymakr.png)

6. src以下の.pyファイルがM5Cameraに転送され、boot.py -> main.py の順に実行されます
