# xrey
server esp

## Example Code

platformio.ini:
```ini
[env:esp32dev] #Sesuaikan dengan board yang di pakai
platform = espressif32 #Sesuaikan dengan board yang di pakai
board = esp32dev #Sesuaikan dengan board yang di pakai
framework = arduino
monitor_speed = 115200
lib_deps = 
    https://github.com/Zeev-x/xrey.git
    me-no-dev/ESPAsyncWebServer
    bblanchon/ArduinoJson @ ^6.21.0

extra_scripts = .pio/libdeps/esp32dev/espServer/scripts/upload_fs.py
```

main.cpp:
```cpp
#include <espServer.h>

void setup() {
  espServerSetup();
}

void loop() {
  // put your main code here, to run repeatedly:
}
```
