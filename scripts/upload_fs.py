Import("env")

env_name = env["PIOENV"]

def before_upload_fs(source, target, env):
    if env_name == "esp32dev":
        print(">>> Uploading FS untuk ESP32...")
        env.Execute("pio run -t uploadfs -e esp32dev")
    elif env_name == "esp8266":
        print(">>> Uploading FS untuk ESP8266...")
        env.Execute("pio run -t uploadfs -e esp8266")
    else:
        print(">>> Skip upload FS (env tidak dikenal)")

env.AddPreAction("upload", before_upload_fs)
