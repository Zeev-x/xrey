Import("env")
import os

# path data di dalam library (otomatis dicari di .pio/libdeps)
lib_data_dir = os.path.join(env['PROJECT_LIBDEPS_DIR'], env['PIOENV'], "espServer", "data")

def before_upload(source, target, env):
    if os.path.isdir(lib_data_dir):
        print(">>> Using library data folder:", lib_data_dir)
        env.Replace(DATA_DIR=lib_data_dir)
    else:
        print(">>> No data folder found in library")

# Pastikan filesystem image dibangun dulu sebelum upload firmware
env.AddPreAction("upload", before_upload)
env.Depends("upload", "uploadfs")
