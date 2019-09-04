# freeotp_migrate

Python script to migrate from FreeOTP to FreeOTP+

## Requirements

You need retrieve FreeOTP ADB backup by yourself.

### Steps to get tokens.xml

Become developer on your phone
1. Android -> Settings -> System -> About -> Build number (tap,tap,tap) to get android developer mode
2. In "Developer options" allow "USB debugging"
3. Connect phone to PC

ADB backup (case for FreeOTP)
1. install `adb` package
2. run `adb backup -f freeotp-backup.ab -apk org.fedorahosted.freeotp`
3. will be asked for password so entry some <password>

In case encrypted phone
1. download https://github.com/nelenkov/android-backup-extractor/releases
2. run `java -jar abe-all.jar unpack freeotp-backup.ab freeotp.tar <password>` to extract backup
3. run `tar xvf freeotp.tar`
4. tokens are in apps/org.fedorahosted.freeotp/sp/tokens.xml
5. run this script in same folder as 'tokens.xml' or specify file by '-i' argument

## Notice

Do import and export in same time frame as OTP counter can get raised and your newly generated tokens won't work.
In my case two day old export from FreeOTP didn't work. When I did export then import within hour everything went ok.
