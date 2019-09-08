# 准备工作
* 参考https://blog.csdn.net/ouyanggengcheng/article/details/79935657
* 参考https://blog.csdn.net/lb245557472/article/details/96476035

* 下载selenium-server-standalone-3.141.59.jar  https://npm.taobao.org/mirrors/selenium/3.141/selenium-server-standalone-3.141.59.jar

* 下载node https://nodejs.org/dist/v10.16.3/node-v10.16.3-x64.msi

* jdk环境准备、android环境准备

* 安装appium npm --registry http://registry.npm.taobao.org  install -g appium
> *  C:\Users\xxx> * npm --registry http://registry.npm.taobao.org  install -g appium
> *  C:\Users\xxx\AppData\Roaming\npm\appium -> *  C:\Users\xxx\AppData\Roaming\npm\node_modules\appium\build\lib\main.js
> *  C:\Users\xxx\AppData\Roaming\npm\authorize-ios -> *  C:\Users\xxx\AppData\Roaming\npm\node_modules\appium\node_modules\.bin\authorize-ios
> *  
> *  > *  appium-selendroid-driver@1.13.4 install C:\Users\xxx\AppData\Roaming\npm\node_modules\appium\node_modules\appium-selendroid-driver
> *  > *  node ./bin/install.js
> *  
> *  [09:01:39] Java version 1.8.0_111 found
> *  [09:01:40] Ensuring C:\Users\xxx\AppData\Roaming\npm\node_modules\appium\node_modules\appium-selendroid-driver\selendroid\download exists
> *  [09:01:40] Downloading Selendroid standalone server version 0.17.0 from https://repo1.maven.org/maven2/io/selendroid/selendroid-standalone/0.17.0/selendroid-standalone-0.17.0-with-dependencies.jar --> *  C:\Users\xxx\AppData\Roaming\npm\node_modules\appium\node_modules\appium-selendroid-driver\selendroid\download\selendroid-server-7cf7163ac47f1c46eff95b62f78b58c1dabdec534acc6632da3784739f6e9d82.jar
> *  [09:01:45] Writing binary content to C:\Users\xxx\AppData\Roaming\npm\node_modules\appium\node_modules\appium-selendroid-driver\selendroid\download\selendroid-server.jar.tmp
> *  [09:01:45] Selendroid standalone server downloaded
> *  [09:01:45] Determining AndroidManifest location
> *  [09:01:45] Determining server apk location
> *  [09:01:46] Extracting manifest and apk to C:\Users\xxx\AppData\Roaming\npm\node_modules\appium\node_modules\appium-selendroid-driver\selendroid\download
> *  [09:01:46] Copying manifest and apk to C:\Users\xxx\AppData\Roaming\npm\node_modules\appium\node_modules\appium-selendroid-driver\selendroid
> *  [09:01:46] Cleaning up temp files
> *  [09:01:46] Fixing AndroidManifest icon bug
> *  
> *  > *  appium-windows-driver@1.5.1 install C:\Users\xxx\AppData\Roaming\npm\node_modules\appium\node_modules\appium-windows-driver
> *  > *  node install-npm.js
> *  
> *  info WinAppDriver You must use WinAppDriver version 1.1
> *  info WinAppDriver Verifying WinAppDriver version 1.1 is installed via comparing the checksum.
> *  info WinAppDriver WinAppDriver.exe doesn't exist at the correct version 1.1, setting up
> *  WARNING: You are not running as an administrator so WinAppDriver cannot be installed for you; please reinstall as admin
> *  WinAppDriver was not installed; please check your system and re-run npm install if you need WinAppDriver
> *  
> *  > *  core-js@2.6.9 postinstall C:\Users\xxx\AppData\Roaming\npm\node_modules\appium\node_modules\core-js
> *  > *  node scripts/postinstall || echo "ignore"
> *  
> *  Thank you for using core-js ( https://github.com/zloirock/core-js ) for polyfilling JavaScript standard library!
> *  
> *  The project needs your help! Please consider supporting of core-js on Open Collective or Patreon:
> *  > *  https://opencollective.com/core-js
> *  > *  https://www.patreon.com/zloirock
> *  
> *  Also, the author of core-js ( https://github.com/zloirock ) is looking for a good job -)
> *  
> *  
> *  > *  appium-chromedriver@4.12.0 postinstall C:\Users\xxx\AppData\Roaming\npm\node_modules\appium\node_modules\appium-chromedriver
> *  > *  node install-npm.js
> *  
> *  [09:01:50] [Chromedriver Install] Installing Chromedriver version '75.0.3770.90' for platform 'win' and architecture '32'
> *  [09:01:50] [Chromedriver Install] Opening temp file to write 'chromedriver_win32' to...
> *  [09:01:50] [Chromedriver Install] Opened temp file 'C:\Users\xxx\AppData\Local\Temp\201988-7280-vgyorl.5fhek\chromedriver_win32.zip'
> *  [09:01:50] [Chromedriver Install] Downloading https://chromedriver.storage.googleapis.com/75.0.3770.90/chromedriver_win32.zip...
> *  [09:01:51] [Chromedriver Install] Writing binary content to C:\Users\xxx\AppData\Local\Temp\201988-7280-vgyorl.5fhek\chromedriver_win32.zip...
> *  [09:01:51] [Chromedriver Install] Extracting C:\Users\xxx\AppData\Local\Temp\201988-7280-vgyorl.5fhek\chromedriver_win32.zip to C:\Users\xxx\AppData\Local\Temp\201988-7280-vgyorl.5fhek\chromedriver_win32
> *  [09:01:51] [Chromedriver Install] Creating C:\Users\xxx\AppData\Roaming\npm\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win...
> *  [09:01:51] [Chromedriver Install] Copying unzipped binary, reading from C:\Users\xxx\AppData\Local\Temp\201988-7280-vgyorl.5fhek\chromedriver_win32\chromedriver.exe...
> *  [09:01:51] [Chromedriver Install] Writing to C:\Users\xxx\AppData\Roaming\npm\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win\chromedriver.exe...
> *  [09:01:51] [Chromedriver Install] C:\Users\xxx\AppData\Roaming\npm\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win\chromedriver.exe successfully put in place
> *  npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@2.0.7 (node_modules\appium\node_modules\fsevents):
> *  npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@2.0.7: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})
> *  
> *  + appium@1.14.2
> *  added 575 packages from 399 contributors in 67.229s
> *  
> *  C:\Users\xxx> * 

* 启动hub java -jar selenium-server-standalone-3.141.59.jar -role hub
> *  (app_grid) C:\Users\xxx\PycharmProjects\app_grid> * java -jar selenium-server-standalone-3.141.59.jar -role hub
> *  10:49:58.037 INFO [GridLauncherV3.parse] - Selenium server version: 3.141.59, revision: e82be7d358
> *  10:49:58.255 INFO [GridLauncherV3.lambda$buildLaunchers$5] - Launching Selenium Grid hub on port 4444
> *  2019-09-08 10:49:59.268:INFO::main: Logging initialized @2538ms to org.seleniumhq.jetty9.util.log.StdErrLog
> *  10:50:00.496 INFO [Hub.start] - Selenium Grid hub is up and running
> *  10:50:00.496 INFO [Hub.start] - Nodes should register to http://192.168.0.109:4444/grid/register/
> *  10:50:00.497 INFO [Hub.start] - Clients should connect to http://192.168.0.109:4444/wd/hub
> *  10:52:17.298 INFO [DefaultGridRegistry.add] - Registered a node http://127.0.0.1:4723

* 启动node1 appium -p 4723 --nodeconfig ./node_honor9.json
> *  (app_grid) C:\Users\xxx\PycharmProjects\app_grid> * appium -p 4723 --nodeconfig ./node_honor9.json
> *  [Appium] Welcome to Appium v1.14.2
> *  [Appium] Non-default server args:
> *  [Appium]   nodeconfig: ./node_honor9.json
> *  [debug] [Appium] Starting auto register thread for grid. Will try to register every 5000 ms.
> *  [Appium] Appium REST http interface listener started on 0.0.0.0:4723
> *  [debug] [Appium] Appium successfully registered with the grid on http://127.0.0.1:4444
> *  [HTTP] --> *  GET /wd/hub/status
> *  [HTTP] {}
> *  [debug] [GENERIC] Calling AppiumDriver.getStatus() with args: []
> *  [debug] [GENERIC] Responding to client with driver.getStatus() result: {"build":{"version":"1.14.2"}}
> *  [HTTP] <-- GET /wd/hub/status 200 7 ms - 68
> *  [HTTP]

* 启动node2 appium -p 4724 --nodeconfig ./node_ml_note6.json
> * (app_grid) C:\Users\xxx\PycharmProjects\app_grid>appium -p 4724 --nodeconfig ./node_ml_note6.json
> * [Appium] Welcome to Appium v1.14.2
> * [Appium] Non-default server args:
> * [Appium]   port: 4724
> * [Appium]   nodeconfig: ./node_ml_note6.json
> * [debug] [Appium] Starting auto register thread for grid. Will try to register every 5000 ms.
> * [Appium] Appium REST http interface listener started on 0.0.0.0:4724
> * [debug] [Appium] Appium successfully registered with the grid on http://127.0.0.1:4444
> * [HTTP] --> GET /wd/hub/status
> * [HTTP] {}
> * [debug] [GENERIC] Calling AppiumDriver.getStatus() with args: []
> * [debug] [GENERIC] Responding to client with driver.getStatus() result: {"build":{"version":"1.14.2"}}
> * [HTTP] <-- GET /wd/hub/status 200 7 ms - 68
> * [HTTP]
> * [HTTP] --> GET /wd/hub/status
> * [HTTP] {}
> * [debug] [GENERIC] Calling AppiumDriver.getStatus() with args: []
> * [debug] [GENERIC] Responding to client with driver.getStatus() result: {"build":{"version":"1.14.2"}}
> * [HTTP] <-- GET /wd/hub/status 200 3 ms - 68
> * [HTTP]
> * [HTTP] --> GET /wd/hub/status
> * [HTTP] {}
> * [debug] [GENERIC] Calling AppiumDriver.getStatus() with args: []
> * [debug] [GENERIC] Responding to client with driver.getStatus() result: {"build":{"version":"1.14.2"}}
> * [HTTP] <-- GET /wd/hub/status 200 2 ms - 68
> * [HTTP]
> * 
* 查看node状态 http://127.0.0.1:4444/grid/console

* 启动脚本 python app_test.py
> * selenium.common.exceptions.WebDriverException: Message: An unknown server-side error occurred while processing the command. Original error: The instrumentation process cannot be initialized. Make sure the application under test does not crash and investigate the logcat output.
> * 此报错是通过重启手机解决的


