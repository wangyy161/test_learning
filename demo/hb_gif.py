
import imageio
import os


def create_gif(image_list, gif_name):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # Save them as frames into a gif
    imageio.mimsave(gif_name, frames, 'GIF', duration=0.1)

    return

def main():
    image_list = ['黑色背景金币-0.png', '黑色背景金币-1.png', '黑色背景金币-2.png',
                  '黑色背景金币-3.png', '黑色背景金币-4.png', '黑色背景金币-5.png',
                  '黑色背景金币-6.png', '黑色背景金币-7.png', '黑色背景金币-8.png',
                  '黑色背景金币-9.png', '黑色背景金币-10.png', '黑色背景金币-11.png',
                  '黑色背景金币-12.png', '黑色背景金币-13.png', '黑色背景金币-14.png',
                  '黑色背景金币-15.png', '黑色背景金币-16.png', '黑色背景金币-17.png',
                  '黑色背景金币-19.png', '黑色背景金币-20.png', '黑色背景金币-21.png',
                  '黑色背景金币-22.png', '黑色背景金币-23.png', '黑色背景金币-24.png',
                  '黑色背景金币-25.png', '黑色背景金币-26.png', '黑色背景金币-27.png',
                  '黑色背景金币-28.png', '黑色背景金币-29.png']
    gif_name = '黑色背景金币.gif'
    create_gif(image_list, gif_name)


if __name__ == "__main__":
    main()
