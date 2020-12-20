#renew更新偏好值，每次运行结束程序后，或者用户试图刷新时，运行这个接口
import update_weights
import inceptionv3
import os
import glob
model_dir=os.getcwd()
image_dir=os.path.join(
          model_dir, 'preference')
paths = glob.glob(os.path.join(image_dir,'*.jpg'))
inceptionv3.predict(paths)
update_weights.modify()
            