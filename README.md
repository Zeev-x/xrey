# xrey
ESP32/ESP8266 Web Server Library dengan Auto Upload Filesystem

Library ini menyediakan web server asinkron untuk ESP32 dan ESP8266, lengkap dengan **auto-upload filesystem** (SPIFFS/LittleFS) sehingga pengguna tidak perlu mengunggah file secara manual. Cocok untuk membuat project IoT, server web lokal, atau REST API ringan.

---

## Fitur

- Mendukung ESP32 dan ESP8266
- Web server asinkron berbasis `ESPAsyncWebServer`
- Auto upload filesystem dari folder library
- Mendukung JSON melalui `ArduinoJson`
- Mudah digunakan, cukup include `espServer.h`

---

## Contoh Project

### platformio.ini
```ini
[env:esp32dev]  ; Ganti dengan board yang digunakan
platform = espressif32
board = esp32dev
framework = arduino
monitor_speed = 115200
lib_deps = 
    https://github.com/Zeev-x/xrey.git
    me-no-dev/ESPAsyncWebServer
    me-no-dev/AsyncTCP
    bblanchon/ArduinoJson @ ^6.21.0

extra_scripts = .pio/libdeps/esp32dev/espServer/scripts/upload_fs.py
```
Untuk ESP8266, gunakan platform = espressif8266, board misal esp12e, dan ganti AsyncTCP dengan ESPAsyncTCP.

main.cpp
```cpp
#include <espServer.h>

void setup() {
  Serial.begin(115200);
  espServerSetup();  // Inisialisasi server dan filesystem
}

void loop() {
  //More Function
}
```
