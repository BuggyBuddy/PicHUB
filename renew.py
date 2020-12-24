#renew更新偏好值，每次运行结束程序后，或者用户试图刷新时，运行这个接口
import update_weights
import inceptionv3
inceptionv3.predict()
update_weights.modify()
