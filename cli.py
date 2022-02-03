from config import *
from inference_video import *
from upcunet_v3 import *
import cv2
import argparse
from time import time as ttime

def cli():
    parser = argparse.ArgumentParser(description='Real-CUGAN')
    modeSubparser = parser.add_subparsers(metavar='mode')

    #Video Mode
    videoMode = modeSubparser.add_parser('video', help='video mode')
    videoMode.set_defaults(func=procVideo)
    videoMode.add_argument('videofile', type=str, help='path to video file')
    videoMode.add_argument('outputFile', type=str, help='path to output file')

    #Image Mode
    imageMode = modeSubparser.add_parser('image', help='image mode')
    imageMode.set_defaults(func=procImageDir)
    imageMode.add_argument('imagedir', type=str, help='path to image dir')
    imageMode.add_argument('outputDir', type=str, help='path to output dir')
    args=parser.parse_args()
    args.func(args)

def procImageDir(args:argparse.Namespace):
    upscaler2x = RealWaifuUpScaler(scale, eval("model_path%s" % scale), half=half, device=device)
    output_dir = args.outputDir
    os.makedirs(output_dir,exist_ok=True)
    for name in os.listdir(args.imagedir):
        print("Processing "+name)
        splitName = name.split(".")
        inp_path = os.path.join(args.imagedir, name)
        suffix = splitName[-1]
        prefix = ".".join(splitName[:-1])
        frame = cv2.imread(inp_path)[:, :, [2, 1, 0]]
        t0 = ttime()
        result = upscaler2x(frame, tile_mode=tile)[:, :, ::-1]
        t1 = ttime()
        print(prefix, "done", t1 - t0)
        final_opt_path=os.path.join(output_dir, prefix + '.' + suffix)
        cv2.imwrite(final_opt_path, result)

def procVideo(args:argparse.Namespace):
    opt_path = args.outputFile
    video_upscaler=VideoRealWaifuUpScaler(nt,n_gpu,scale,half,tile,p_sleep,decode_sleep,encode_params)
    video_upscaler(args.videofile,opt_path)
    
if __name__ == '__main__':
    cli()