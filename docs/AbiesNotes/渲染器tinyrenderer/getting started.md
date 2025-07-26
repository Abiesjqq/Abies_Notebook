# 编译

~~在Github主页上给出的代码为:~~

```bash
git clone https://github.com/ssloy/tinyrenderer.git &&
cd tinyrenderer &&
cmake -Bbuild &&
cmake --build build -j &&
build/tinyrenderer obj/diablo3_pose/diablo3_pose.obj obj/floor.obj
```

~~但是可能会碰到连接不稳定无法下载的情况，可以直接在GitHub里download zip~~

~~解压后要cd到类似于`<name>\tinyrenderer-master\tinyrenderer-master`文件夹执行build指令~~

~~`tinyrenderer.exe`文件在`build\Debug`里,最后一条指令可改用`.\build\Debug\tinyrenderer.exe obj\diablo3_pose\diablo3_pose.obj obj\floor.obj`~~

只要tgaimage.h, tgaimage.cpp，编译时链接tgaimage.cpp即可

编译运行：

```bash
g++ temp.cpp tgaimage.cpp -o temp
temp
```

# 一个视频

YouTube上的视频: [https://www.youtube.com/watch?v=Dy_jbA_fwFk&list=PLsYRP8pwiVX_CrqYJOhCS6LxewZZ6lDLr](https://www.youtube.com/watch?v=Dy_jbA_fwFk&list=PLsYRP8pwiVX_CrqYJOhCS6LxewZZ6lDLr)