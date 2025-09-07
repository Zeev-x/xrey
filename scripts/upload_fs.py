Import("env")
import os
import shutil

lib_data_dir = os.path.join(env['PROJECT_LIBDEPS_DIR'], env['PIOENV'], "espServer", "data")
project_data_dir = os.path.join(env['PROJECT_DIR'], "data")

def before_upload(source, target, env):
    # Hapus folder data project lama jika ada
    if os.path.isdir(project_data_dir):
        shutil.rmtree(project_data_dir)
    # Copy folder data library ke project
    shutil.copytree(lib_data_dir, project_data_dir)
    env.Replace(DATA_DIR=project_data_dir)
    print(">>> Using library data folder:", project_data_dir)

# Jalankan sebelum upload firmware
env.AddPreAction("upload", before_upload)
# Pastikan uploadfs dibangun dulu
env.Depends("upload", "uploadfs")
