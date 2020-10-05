'''
author: zhouhonghong
date: 2020/09/30

get_ab_jpg:遍历文件夹判断非空，得到未生成的视频名称，进一步得到
视频帧的存储路径，生成一个txt
'''
import os

def get_ab_jpg(path_f, txt_j, txt_v):
    file = open(txt_v)
    all_videos = []
    # ab_videos = []
    exist_videos = []
    for line in file.readlines():
        all_videos.append(line.strip().split("/")[-1])
    for video_name in os.listdir(path_f):
        if os.listdir(os.path.join(path_f, video_name)):
            exist_videos.append(video_name)
        # else:
        #     ab_videos.append(video_name)
    file.close()
    file2 = open(txt_j)
    all_jpgs = file.readlines()
    ab_jpgs = []
    for jpg_path in all_jpgs:
        for video in exist_videos:
            if video not in jpg_path:
                ab_jpgs.append(jpg_path)
    file2.close()
    file_out = open('jpg_paths_for_absent_videos.txt','w')
    file_out.write(str(ab_jpgs))
    file_out.close()


if __name__ == '__main__':

    """
    input
    """
    # 特征路径
    path_f = ''
    # 保存所有需处理的jpg名称的txt的路径
    txt_j = '.txt'
    # 保存所有需处理的video名称的txt的路径
    txt_v = '.txt'
    """
    output
    """
    # 未生成特征的视频名称
    get_ab_jpg(path_f, txt_j, txt_v)
