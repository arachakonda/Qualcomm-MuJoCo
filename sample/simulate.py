import mujoco
from mujoco import viewer
import sys

if __name__ == '__main__':
  # print version, check compatibility
  print('MuJoCo version {}'.format(mujoco.mj_versionString()))
  if mujoco.mjVERSION_HEADER != mujoco.mj_version():
    raise mujoco.FatalError('Headers and library have different versions')

  if len(sys.argv) > 1:
    viewer.launch(sys.argv[1])
  else:
    viewer.launch()