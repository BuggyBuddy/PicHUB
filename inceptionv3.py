# -*- coding: utf-8 -*-
 
import tensorflow as tf
import numpy as np
import re
import os
import glob

file_dir=os.getcwd()
model_dir=os.getcwd()
image_dir=os.path.join(
          model_dir, 'preference')
paths = glob.glob(os.path.join(image_dir,'*.jpg'))
#f1=open("preference_type.txt","a+")
#f2=open("preference_possibility.txt","a+")


 
 
#将类别ID转换为人类易读的标签
class NodeLookup(object):
  def __init__(self,
               label_lookup_path=None,
               uid_lookup_path=None):
    if not label_lookup_path:
      label_lookup_path = os.path.join(
          model_dir, 'imagenet_2012_challenge_label_map_proto.pbtxt')
    if not uid_lookup_path:
      uid_lookup_path = os.path.join(
          model_dir, 'imagenet_synset_to_human_label_map.txt')
    self.node_lookup = self.load(label_lookup_path, uid_lookup_path)
 
  def load(self, label_lookup_path, uid_lookup_path):
    if not tf.gfile.Exists(uid_lookup_path):
      tf.logging.fatal('File does not exist %s', uid_lookup_path)
    if not tf.gfile.Exists(label_lookup_path):
      tf.logging.fatal('File does not exist %s', label_lookup_path)
 
    # Loads mapping from string UID to human-readable string
    proto_as_ascii_lines = tf.gfile.GFile(uid_lookup_path).readlines()
    uid_to_human = {}
    p = re.compile(r'[n\d]*[ \S,]*')
    for line in proto_as_ascii_lines:
      parsed_items = p.findall(line)
      uid = parsed_items[0]
      human_string = parsed_items[2]
      uid_to_human[uid] = human_string
 
    # Loads mapping from string UID to integer node ID.
    node_id_to_uid = {}
    proto_as_ascii = tf.gfile.GFile(label_lookup_path).readlines()
    for line in proto_as_ascii:
      if line.startswith('  target_class:'):
        target_class = int(line.split(': ')[1])
      if line.startswith('  target_class_string:'):
        target_class_string = line.split(': ')[1]
        node_id_to_uid[target_class] = target_class_string[1:-2]
 
    # Loads the final mapping of integer node ID to human-readable string
    node_id_to_name = {}
    for key, val in node_id_to_uid.items():
      if val not in uid_to_human:
        tf.logging.fatal('Failed to locate: %s', val)
      name = uid_to_human[val]
      node_id_to_name[key] = name
 
    return node_id_to_name
 
  def id_to_string(self, node_id):
    if node_id not in self.node_lookup:
      return ' '
    return self.node_lookup[node_id]


 
#读取训练好的Inception-v3模型来创建graph
def create_graph():
  with tf.gfile.FastGFile(os.path.join(
      model_dir, 'classify_image_graph_def.pb'), 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')
    

        
        
 
def predict() : 
    sess=tf.Session()
#Inception-v3模型的最后一层softmax的输出

                #创建graph
    create_graph()
    softmax_tensor= sess.graph.get_tensor_by_name('softmax:0')

    
    #读取图片
    for path in paths:
        image_data = tf.gfile.FastGFile(path, 'rb').read()


#输入图像数据，得到softmax概率值（一个shape=(1,1008)的向量）
        predictions = sess.run(softmax_tensor,{'DecodeJpeg/contents:0': image_data})
#(1,1008)->(1008,)
        predictions = np.squeeze(predictions)
 
# ID --> English string label.
        node_lookup = NodeLookup()
#取出前5个概率最大的值（top-5)
        top_5 = predictions.argsort()[-5:][::-1]
        for node_id in top_5:
          score = predictions[node_id]
          if score>=0.1:
              human_string = node_lookup.id_to_string(node_id)
#              f1.write('%s\n'%(human_string))
#              f2.write('%s\n'%(score))

     
    sess.close()
#    f1.close()
#    f2.close()