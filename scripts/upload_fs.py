Import("env")
import os
import shutil

lib_data_dir = os.path.join(env['PROJECT_LIBDEPS_DIR'], env['PIOENV'], "espServer", "data")
project_data_dir = os.path.join(env['PROJECT_DIR'], "data")

def before_upload(source, target, env):
    if os.path.isdir(project_data_dir):
        shutil.rmtree(project_data_dir)

    shutil.copytree(lib_data_dir, project_data_dir)
    env.Replace(DATA_DIR=project_data_dir)
    print(">>> Using library data folder:", project_data_dir)

    env.Execute("pio run -t uploadfs -e {}".format(env['PIOENV']))

    shutil.rmtree(project_data_dir)
    print(">>> Temporary data folder removed.")

env.AddPreAction("upload", before_upload)

