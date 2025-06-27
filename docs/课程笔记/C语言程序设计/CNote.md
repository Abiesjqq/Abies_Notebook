CNote==把大写变为小写:==

```c
#include<stdio.h>;
#include<ctype.h>; //含有tolower等函数
int main()
{
    char c;
    while (c=getchar()!=EOF)
        putchar(tolower(c));
    return 0;
}
```

**==优先级==**

1. 后缀 ++ --
2. 一元 + - ! ~ ++ -- \* & sizeof
3. 乘除 % / \*
4. 加减 + -
5. 位移 << >>
6. 关系 < <= > >=
7. 相等 == !=
8. 位与 &
9. 位异或 ^
10. 位或 |
11. 逻辑与 &&
12. 逻辑或 ||
13. 条件 ?:
14. 赋值 = += -= \*= /= %= <<= >>= &= ^= |
15. 逗号 ,

- 从右往左:单目运算,赋值运算,条件表达式

**==原码,反码,补码,移码==**

- 真值:将带符号位的机器数对应的真正数值称为机器数的真值
- 原码:原码就是符号位加上真值的绝对值,即用第一位表示符号 其余位表示值。比如如果是 8 位二进制: +1 = 0000_0001
- 反码:正数的反码是其本身，负数的反码是在其原码的基础上符号位不变，其余各个位取反。
- 补码:正数的补码就是其本身，负数的补码是在其反码的基础上+1
- 移码:不管正负数，只要将其补码的符号位取反即可
  移码格式：1 位符号位 其余为 真值+2^(N)−1, 其中 N 表示位数
  单精度浮点数据为 8 位， 双精度为 11 位

**==可变参数函数==**
函数参数存储:从右到左依次入栈,连续存储(从高地址到低地址)
如果通过指针访问函数参数,除了第一个参数之外,后面的参数可省略,用...代替
例如,下面的函数可行:

```c
void print(int a,...)
{
    int *ptr=&a;
    printf("%d ",*ptr);
    printf("%d ",*(ptr+1));
}
```

==sprintf 和 sscanf==

```c
int n,m;
char s[80]="hello 11 22";
sscanf(s,"%d%d",&n,&m);
    //sscanf:从字符串中读入,读到空格或换行自动跳过,剩余部分匹配
```

<span style="font-size:larger;background-color:yellow;">C 语言“段错误”类型</span>
在 C 语言编程中，段错误（Segmentation Fault）通常是指程序尝试访问或修改它没有权限访问的内存区域。以下是一些常见的导致段错误的类型：

1. **空指针解引用**：
   程序试图通过一个未初始化或已经设置为`NULL`的指针访问内存。
   ```c
   int *p = NULL;
   *p = 10; // 这将导致段错误
   ```
2. **越界访问**：
   当数组访问超出其边界时，程序可能会访问到不属于该数组的内存区域。
   ```c
   int arr[10];
   arr[100] = 10; // 这可能引起段错误
   ```
3. **野指针**：
   指针指向已释放的内存后未被重新赋值，之后若尝试通过该指针访问内存，则会引发段错误。
   ```c
   int *p = malloc(sizeof(int));
   free(p);
   *p = 10; // 这可能会导致段错误
   ```
4. **写入只读内存**：
   尝试修改 const 变量或字符串字面量所在的内存区域。
   ```c
   const int x = 10;
   int *p = (int *)&x;
   *p = 20; // 这将导致段错误
   ```
5. **栈溢出**：
   函数调用太深导致栈空间耗尽，或者局部变量使用了过多栈空间。
   ```c
   void recursiveFunction() {
       int a[1000000];
       recursiveFunction(); // 递归太深可能导致栈溢出，进而引发段错误
   }
   ```
6. **错误的内存分配**：
   使用了不正确或不匹配的内存分配和释放函数，例如混用`malloc`和`free`与`new`和`delete`。
   ```c
   void *p = malloc(sizeof(int));
   delete p; // 错误的使用delete来释放malloc分配的内存，可能导致段错误
   ```
7. **未对齐的内存访问**：
   在某些硬件架构上，对齐的内存访问是必须的，未对齐的访问可能会导致段错误。
   要避免段错误，需要养成良好的编程习惯，比如始终初始化指针、检查指针是否为`NULL`、确保数组访问不越界、避免使用野指针、不要修改只读内存区域，以及正确管理动态内存分配。在调试程序时，可以使用工具如`valgrind`（在 Linux 上）来检测内存相关问题。

==时间复杂度，空间复杂度，问题规模==

- **时间频度**:一个算法中的语句执行次数称为语句频度或时间频度。记为 T(n)。
- **问题规模**:在刚才提到的时间频度中，n 称为问题的规模，当 n 不断变化时，时间频度 T(n)也会不断变化。
- **时间复杂度**: 一般情况下，算法中基本操作重复执行的次数是问题规模 n 的某个函数，用 T(n)表示，若有某个辅助函数 f(n),使得当 n 趋近于无穷大时，T(n)/f(n)的极限值为不等于零的常数，则称 f(n)是 T(n)的同数量级函数。记作 T(n)=Ｏ(f(n)),称Ｏ(f(n)) 为算法的渐进时间复杂度，简称时间复杂度。

==细节==
由高级语言编写的程序：源程序.c  
源程序.c->（编译后）目标程序.obj->（链接后）可执行程序.exe  
结构化程序的三种基本结构：顺序、选择、循环  
主要原则：模块化、自顶向下、逐步求积  
一个 c 语言是由函数组成的，函数是 C 语言基本单位（C 语言没有子程序）  
程序的最小单位是语句  
C 语言程序总是从 main 函数开始执行  
不常见关键字：signed extern register sizeof auto  
sizeof 是运算符，不是函数  
最简单的数据类型是整型、实型、字符型  
整型数据分为八进制、十进制、十六进制（没有二进制）  
-017 表示八进制（o）  
科学计数法：e 前 e 后必有数，e 后必须为整数（可带正负号）  
int,char,short 所占字节数由所用机器的字长决定  
'\ddd'每位 d 为八进制数，表示一个字符 例如'\17'  
'\xhh'每个 h 为十六进制数，表示字符 例如'\xaa'  
字符加减为 ascii 加减，字符型变量可按整型赋值  
字符常量：单引号 字符串常量：双引号 例如"A"占两个字节  
%d 输出为十进制，%o 八进制，%x 十六进制（自动转化）  
printf("x=%%d,y=%%d",x,y); 输出 x=%d,y=%d  
%前后必须为整数  
逗号运算符在所有运算符中优先级最低  
++(i+1)是非法的（i+1 是表达式，不是变量）  
x=i>0 x 的值为 0 或 1  
一个表达式中含多种类型，最终结果类型为存储范围最大的  
存储范围：char int long float double  
a=2 表达式 a=2; 语句（有分号）  
x=y=1 是正确的赋值语句  
int a=3; a+=a-=a\*a; a 的值为-12  
int a=0; a+=(a=8); a 的值为 16  
单目运算符对象可以是字符、整型、实型等任何类型，不能常量  
int a=10;printf("%d %d",a--,--a); 输出 10 9，a--后该语句值为 10，a 的值为 9  
x=(i=4,j=5,k=6)； x 的值为 6  
(m=6,m+1,n=6,m+n) 的值为 12  
char 型数据在内存中存储形式为 ascii 码  
整型数据存储形式为二进制补码  
A 的 acsii 码为 65，a 为 97，回车 13，空格 32  
每个 c 程序有且仅有一个 main 函数  
-19%4 的值为-3（结果正负由前面的数的正负决定）  
实型+整型 结果为实型  
< CR >表示回车  
printf 中参数多于格式说明符：从前往后输出，多余的忽略  
int a=1234; printf("%2d",a); 输出为 1234（数字长度大于限定，则忽略限定原样输出，不能破坏数据完整性）  
scanf 中%2d 表示截取两个长度的数字，若输入有多余，多余部分忽略  
将整型值赋给实型，自动转化为小数，带.000000  
%c 可能读入空格、回车（有 ascii 码的都是字符）  
int x,y; scanf("%d%d",&x,&y); 输入为 1，2，则 y 为不确定的值  
putchar 输出字符或字符型变量  
scanf 格式控制后为变量地址，格式控制包含格式声明和普通字符  
printf 是输出列表：常量、变量、表达式  
{}中的语句称为复合语句，单独的；称为空语句  
交换 x 和 y 的值：x+=y; y=x-y; x-=y;  
&&左边为假，不执行右边；||左边为真，不执行右边（短路）  
if（-1）后面语句执行（不等于 0 都执行）  
int x=1,y=2,z=3; if (x>y) x=y; y=z; z=x; 执行后 x=1,y=2,z=1（if 后无大括号）  
switch 括号中可以为表达式 int char enum，不能为 float  
三种逻辑运算符： ！ && ||  
算术运算>逻辑运算>赋值运算，7&&3+12 等价于 7&&（3+12）  
num[]={...} {}中元素可多不可少  
二维数组定义，行可以省略，列不可省略  
若二维数组初始化只有一个{}，从前往后填  
int a[4] 不能 a=…，因为数组名为地址  
函数不能嵌套定义  
实参和其对应的形参占用独立的存储单元  
形参必须是变量，不能是常量、表达式  
若实参、形参类型不一致，以形参类型为准  
实参到形参：值传递（对形参的修改不改变实参的值）  
函数类型由返回值决定  
一个程序由一个或多个源程序文件组成  
C 语言不提供输入输出语句，标准库提供  
若函数由返回值，必须通过 return 返回  
形参的值不能传回给实参  
实参到形参有两种方式：值传递、地址传递  
ascii 码中大小写相差 32，小写大于大写  
!x!=0 先执行!x，再判断是否!=0  
if (); while(); 因为后面有分号，为空语句（但若括号中语句改变变量的值，仍会作用）  
在函数内部定义变量名和全局变量相同的变量，则他们是两个不同的变量，不会相互影响  
形参可以说明为 const，不能为 static  
变量隐含的存储类型为 auto（自动型）  
变量的存储类型包括自动型、静态型、外部型、寄存器型  
声明外部变量：extern  
C 语言变量按其生存期分为局部变量和全局变量  
静态局部变量的作用域是它所在的局部，生存期为整个函数  
静态变量的初始化在编译阶段完成  
define 是预定义标识符，可以作为用户标识符（但使用后原含义丧失）  
C 语言有 32 个关键字  
预处理功能有三种：宏定义，文件包含，条件编译  
预处理命令以#开头

一些奇怪的题目：

```c
#include<stdio.h>
#define max(a,b) (a)>(b)?(a):(b)
int main(){
	int x,y,z;
	x=10;y=15;
	z=10*max(x,y);            //10*10>15?10:15,结果为10
	printf("%d\n",z);
	return 0;
}
```

```c
int m=0;
if (m || (m=2) || (m=3));    //m=2为赋值语句，执行后m为2，该语句为2，条件成立，后续语句短路，m保留2
printf("%d\n",m);
```

```c
int a=0,b=0,c=2,d=4;
if ((c=a==b || d=b==a));       //(a==b)为1，前一语句为赋值c=1，条件成立，d维持4
printf("%d\n",d);
```

```c
int x=1,y=2,z=3;
x+=y+=z;                       //y为5，x为6，输出6
printf("%d\n",x<y?y:x);
```

```c
#include<stdio.h>
int main(){
	int y=10;
	while (y--);  //y=1时仍执行，此时y=0；下一轮条件不成立，但y--已执行，故y为-1
	printf("y=%d\n",y);
}
```

```c
#include<stdio.h>
int main(){
	int y=10;
	do y--;
	while (--y);  //y=2时y--后y为1，--y条件不成立，但y值变为0，输出时输出y，即输出0
	printf("%d\n",y--);
}
```

```c
for (i=0;i<4;i++)
for (k=1;k<3;k++); printf("*"); //for后有分号，输出*
```

```c
#include<stdio.h>
int main(){
	int x,y;
	for (x=30,y=0;x>=10,y<10;x--,y++) {  //中间为逗号表达式，x>=10无效，
输出为x=0  y=12
		x/=2;
		y+=2;
	}
	printf("x=%d y=%d\n",x,y);
}
```

==main==

==FILE==

```c
#include <stdio.h>

int main(int argc,char *argv[])
{
    FILE *fp1,*fp2;
    if (argc!=3) { //这是判断什么?
        printf("Usage:copy f1 f2\n");
        exit(1); //这是什么意思?
    }
    if ((fp1=fopen(argv[1],"r"))==NULL
        || (fp2=fopen(argv[2],"w"))==NULL) {
        printf("Can't open file!\n");
        exit(2); //这是什么意思?
    }

    while (putc(getc(fp1),fp2)!=EOF); //putc和getc干什么?

    fclose(fp1);
    fclose(fp2);
    return 0;
}
```

这段代码是一个简单的 C 语言程序，用于将一个文件的内容复制到另一个文件。下面是对注释掉的问题的解释：

1. `if (argc!=3)` 这是判断什么？

   - 这个条件判断程序接收到的命令行参数个数是否不等于 3。在这个程序中，它期望接收到三个参数：程序名、源文件名和目标文件名。如果参数个数不是 3，说明用户没有正确地提供所需的参数。

2. `exit(1);` 这是什么意思？

   - `exit(1);` 是一个函数调用，用于立即终止程序的执行。`exit`函数的参数是程序的退出状态码，`1` 通常表示程序因为某种错误或异常情况而终止。在这种情况下，如果用户没有提供正确的参数个数，程序会打印使用说明并退出，状态码为 1。

3. `exit(2);` 这是什么意思？

   - 类似于`exit(1);`，`exit(2);`也是用于终止程序的执行，并且提供一个不同的退出状态码`2`。在这里，如果程序无法打开指定的文件（无论是源文件还是目标文件），程序会打印错误信息并退出，状态码为 2。

4. `while (putc(getc(fp1),fp2)!=EOF);` putc 和 getc 干什么？
   - `getc(fp1)` 函数用于从文件指针`fp1`指向的文件（源文件）中读取一个字符。`putc(c, fp2)` 函数用于将字符`c`写入文件指针`fp2`指向的文件（目标文件）。这两个函数在循环中使用，用于逐个字符地从源文件读取并写入到目标文件，直到到达文件末尾（EOF）。`EOF`是一个宏，表示文件结束符。

整个程序的工作流程是：

- 检查命令行参数个数。
- 尝试打开源文件和目标文件。
- 逐个字符地从源文件读取并写入到目标文件，直到文件结束。
- 关闭两个文件。
- 程序结束。

```c
//将大小写互换,并存储到另一个文件
#include <stdio.h>
int main(int argc,char *argv[])
{
    FILE *fp1,*fp2;
    char c;
    if (argc!=3) exit(1);
    if ((fp1=fopen(*++argv,"r"))==NULL
        || (fp2=fopen(*++argv,"w")==NULL)) exit(2);

    while ((c=fgetc(fp1))!=EOF) {
        fputc(c+'A'-'a',fp2);
    }

    fclose(fp1);
    fclose(fp2);
    return 0;
}
```

```c
//concatenate files
#include <stdio.h>

void filecopy(FILE *ifp,FILE *ofp)  //FILE是什么?可以是stdin或stdout吗?
{
    int c;
    while ((c=getc(ifp))!=EOF) putc(c,ofp);
}

int main(int argc,char *argv[])  //argv是什么?
{
    FILE *fp;
    if (argc==1) filecopy(stdin,stdout);
    else {
        while (--argc){
            if ((fp=fopen(*++argv,"r"))==NULL) {
                printf("cat:can't open %s\n",*argv);
                return 1; //return 1和exit(1)相同吗?
            } else {
                filecopy(fp,stdout);
                fclose(fp);
            }
        }
    }
    return 0;
}
```

这段代码是一个简单的 C 语言程序，用于连接（concatenate）多个文件的内容并输出到标准输出（stdout）。下面是对注释掉的问题的解释：

1. `FILE是什么？可以是stdin或stdout吗？`

   - `FILE` 是 C 语言标准库中定义的一个结构体类型，用于表示文件流。它可以用来读写文件。`FILE` 结构体包含了文件的缓冲区、文件描述符等信息，使得程序能够通过标准库函数对文件进行操作。
   - 是的，`FILE` 可以是 `stdin` 或 `stdout`。`stdin` 是标准输入流，通常与键盘输入关联；`stdout` 是标准输出流，通常与屏幕输出关联。在这段代码中，`filecopy(stdin, stdout);` 表示将标准输入的内容复制到标准输出。

2. `argv是什么？`

   - `argv` 是 `main` 函数的一个参数，它是一个指向字符指针数组的指针。这个数组包含了命令行参数，其中 `argv[0]` 是程序的名称，`argv[1]`、`argv[2]` 等是传递给程序的参数。`argc` 是 `argv` 数组中元素的个数，包括程序名。

3. `return 1 //return 1和exit(1)相同吗？`
   - `return 1` 和 `exit(1)` 在大多数情况下效果是相同的，它们都会导致程序返回状态码 `1` 给操作系统。不过，它们之间有一个细微的差别：
     - `return` 语句是从一个函数返回到调用它的函数，而 `exit` 函数是直接从程序中退出，并且清理所有使用的资源，包括关闭所有打开的文件和释放分配的内存。
     - 在 `main` 函数中使用 `return` 和 `exit` 效果是相同的，因为 `main` 函数是程序的入口点，从 `main` 返回意味着程序结束执行。但在其他函数中，`return` 只能返回到 `main` 或其他调用它的函数，而 `exit` 则是直接结束整个程序。
     - 在这段代码中，`return 1;` 是从 `main` 函数返回状态码 `1`，因此它的效果与 `exit(1)` 是相同的。

```c
//sort
#include <stdio.h>

void sort(int *list,int n)
{
    int i,j,next;
    for (i=1;i<n;i++) { //插入排序
        next=list[i];
        for (j=i-1;j>=0 && next<list[j];j--) {
            list[j+1]=list[j];
        }
        list[j+1]=next;
    }
}

int main()
{
    int input[10],i;
    FILE *fpin,*fpout;
    if ((fpin=fopen("file1.dat","r"))==NULL) {
        printf("Can't open file1\n");
        exit(-1);
    }
    for (i=0;i<10;i++) {
        fscanf(fpin,"%d",&input[i]); //&input[i]是什么意思?
            //fread(input,sizeof(int),`10,fpout); //fscanf和fread有什么区别?
    }

    sort(input,10);

    if ((fpout=fopen("file2.dat","w"))==NULL) {
        printf("Can't open file2\n");
        exit(-1);
    }
    for (i=0;i<10;i++) {
        fprintf(fpout,"%d",input[i]);
            //fwrite(input,sizeod(int),10,fpout); //fprintf和fwrite有什么区别?
    }
    printf("\n");
    return 0;
}
```

这段代码是一个简单的 C 语言程序，用于读取一个文件中的整数数据，对这些数据进行排序，然后将排序后的结果写入另一个文件。下面是对注释掉的问题的解释：

1. `&input[i]是什么意思？`

   - `&input[i]` 是取数组 `input` 中第 `i` 个元素的地址。`fscanf` 函数需要一个指向整数的指针作为参数，以便能够将读取的数据存储到相应的内存位置。

2. `//fscanf和fread有什么区别？`

   - `fscanf` 和 `fread` 都是用于文件读取的函数，但它们在读取数据时的行为和用途有所不同：
     - `fscanf` 是一个格式化输入函数，它可以从文件中读取格式化的数据，并且能够根据指定的格式字符串解析数据。例如，`fscanf(fpin,"%d",&input[i]);` 会从文件中读取一个整数，并将其存储在 `input[i]` 指向的位置。
     - `fread` 是一个二进制读取函数，它用于从文件中读取固定大小的数据块。`fread` 不会对数据进行任何格式化处理，它只是简单地按字节读取数据。例如，`fread(input,sizeof(int),10,fpin);` 会从文件中读取 10 个整数大小的数据块到 `input` 数组中。

3. `//fprintf和fwrite有什么区别？`
   - `fprintf` 和 `fwrite` 都是用于文件写入的函数，它们的主要区别在于数据的写入方式：
     - `fprintf` 是一个格式化输出函数，它可以将数据按照指定的格式写入文件。例如，`fprintf(fpout,"%d",input[i]);` 会将 `input[i]` 的值按照整数格式写入文件。
     - `fwrite` 是一个二进制写入函数，它用于将数据作为字节流写入文件，不进行任何格式化处理。例如，`fwrite(input,sizeof(int),10,fpout);` 会将 `input` 数组中的 10 个整数作为二进制数据写入文件。

在这段代码中，`fscanf` 和 `fprintf` 被用来读取和写入格式化的整数数据，而注释中的 `fread` 和 `fwrite` 则是用来演示如何以二进制方式读取和写入数据。

==宏==

- 没有值的宏:`#define _DEBUG`
  - 这类宏是用于条件编译的， 后面有其他的编译预处理指令来
    检查这个宏是否已经被定义过了
- 像函数的宏:`#define cube(x) ((x) * (x) * (x))`
- \# operator:`#define PRINT_INT(n) printf(#n "=%d", n)`
  在 C 语言中，`#define` 用于创建宏定义，而 `#` 是一个预处理操作符，称为字符串化操作符（stringizing operator）。当预处理器遇到 `#` 操作符时，它会将其操作数转换为一个字符串字面量。

在你给出的例子中：

```c
#define PRINT_INT(n) printf(#n "=%d", n)
```

这个宏定义 `PRINT_INT(n)` 会将 `n` 这个参数转换为一个字符串，并将其包含在 `printf` 函数的格式字符串中。具体来说：

1. `#n` 将参数 `n` 转换为一个字符串字面量。如果 `n` 是一个宏参数，比如 `x`，那么 `#n` 将变成 `"x"`。

2. `printf(#n "=%d", n)` 将这个字符串与 `"=%d"` 结合，形成一个完整的格式字符串，然后使用 `n` 的值作为 `printf` 函数的第二个参数。

举个例子，如果你这样使用宏：

```c
int x = 10;
PRINT_INT(x);
```

预处理器会将 `PRINT_INT(x)` 替换为：

```c
printf("x = %d", x);
```

这里，`x` 被字符串化了，变成了 `"x"`，然后与 `"=%d"` 结合，形成了 `"x = %d"` 这个格式字符串。`printf` 函数随后会打印出 `x` 的值，并且前面带有变量名 `x`。

使用 `#` 操作符的好处是，它允许宏在展开时包含变量名作为字符串，这在调试和日志记录时非常有用，因为它可以显示哪个变量被打印出来。

- \## operator:
  在 C 语言中，`##` 是一个预处理操作符，称为标记粘贴操作符（token-pasting operator）。它用于在宏展开时将两个标记（tokens）连接在一起。标记可以是任何有效的 C 语言标识符，包括宏参数、关键字、操作符等。

在你给出的例子中：

```c
#define MYCASE(item,id) \
case id: \
item##_##id = id;\
break
```

这个宏定义 `MYCASE(item, id)` 用于在 `switch` 语句中生成一个 `case` 标签，并执行一些操作。具体来说：

1. `item##_##id`：这里使用了两次 `##` 操作符。首先，`##` 将 `item` 和下划线 `_` 连接在一起，形成一个新的标记 `item_`。然后，`##` 将 `_` 和 `id` 连接在一起，形成 `item_id`。如果 `item` 是 `widget` 而 `id` 是 `23`，那么 `item##_##id` 将变成 `widget_23`。

2. `case id:`：这是一个 `case` 标签，它将匹配 `switch` 语句中的值 `id`。

3. `item##_##id = id;`：这行代码将 `id` 的值赋给新生成的变量名 `item_id`。

4. `break`：这行代码用于退出 `switch` 语句。

现在，如果你这样使用宏：

```c
switch(x) {
    MYCASE(widget,23);
}
```

预处理器会将 `MYCASE(widget,23)` 替换为：

```c
case 23:
    widget_23 = 23;
    break;
```

这里，`widget` 和 `23` 被分别粘贴到 `_` 的前后，生成了变量名 `widget_23`，并且这个变量被赋值为 `23`。

使用 `##` 操作符的好处是，它允许宏在展开时动态生成变量名或其他标记，这在创建具有唯一名称的变量或函数时非常有用，尤其是在处理类似 `switch` 语句或创建多个相似函数时。

在 C 语言中，反斜杠 \ 用于续行，它允许程序员将一条语句或定义跨越多行书写，使得代码更加易读。当编译器预处理器遇到行尾的反斜杠时，它会忽略换行符，并将下一行与当前行的内容连接起来，就好像它们是一行一样。

==编译过程==

- 编译预处理 --> .i
- 编译成汇编代码 --> .s
- 汇编成目标代码 --> .o
- 链接成可执行程序 --> .exe （ 或 a.out）
- 这些文件都可以再用 gcc 单独操作， 产生下一步结果 （但是选项复杂）
- gcc -c 的选项可以只编译， 产生目标文件， 但是不链接
  **编译单元**
- 一个.c 文件是一个编译单元
- 编译器每次编译只处理一个编译单元
  **项目**
- 在 Dev C++中新建—个项目， 然后把几个源代码文件加入进去
- 对于项目， Dev C++的编译会把—个项目中所有的源代码文件都编译后， 链接起来
- 有的 IDE 有分开的编译和构建两个按钮， 前者是对单个源代码文件编译， 后者是对整个项目做链接
  **include**
  _"" 还是 <>?_
- `#include`有两种形式来指出要插入的文件
  - "" 要求编译器首先在当前目录(.c 文件所在的目录)寻找这个文件， 如果没有，到编译器指定的目录去找(自己定义的)
  - <> 让编译器只在指定的目录去找(系统里的)
- 编译器自己知道自己的标准库的头文件在哪里
- 环境变量和编译器命令行参数也可以指定寻找头文件的目录
  **static**
- 在函数前面加上 static 就使得它成为只能在所在的编译单元中被使用的函数
- 在全局变量前面加上 static 就使得它成为只能在所在的编译单元中被使用的全局变量
  **声明**
- `int i;` 是变量的定义
- `extern int i;` 是变量的声明
- 同—个编译单元里， 同名的结构不能被重复声明
- 如果你的头文件里有结构的声明， 很难这个头文件不会在—个编译单元里被`#include`多次 所以需要“标准头文件结构”

==程序文件,数据文件==
程序文件和数据文件是计算机系统中两种不同类型的文件，它们在用途和功能上有所区别：

1. **程序文件**：

   - **定义**：程序文件是指包含可执行指令的文件，这些指令是由编程语言编写并编译成机器语言的代码。程序文件通常包含了应用程序的逻辑和功能，它们可以被操作系统直接执行。
   - **类型**：程序文件可以是编译后的二进制文件（如`.exe`文件在 Windows 系统中，或 ELF 格式的文件在类 Unix 系统中），也可以是解释型语言的源代码文件（如`.py`文件对于 Python）。
   - **作用**：程序文件的主要作用是执行特定的任务，比如处理数据、显示图形界面、控制硬件等。
   - **例子**：Word 处理软件、浏览器、游戏、操作系统等。

2. **数据文件**：
   - **定义**：数据文件是指包含数据的文件，这些数据可以是文本、数字、图像、音频、视频等任何形式的信息。数据文件通常由程序读取或写入，用于存储和检索信息。
   - **类型**：数据文件可以是纯文本文件（如`.txt`）、配置文件（如`.ini`、`.xml`、`.json`）、数据库文件（如`.db`、`.sqlite`）、图像文件（如`.jpg`、`.png`）、文档文件（如`.docx`、`.pdf`）等。
   - **作用**：数据文件的主要作用是存储信息，供程序在需要时读取或写入。它们可以是持久存储的数据，也可以是临时数据。
   - **例子**：文档、图片、音乐、视频、数据库中的数据记录等。

在实际应用中，程序文件和数据文件经常相互配合工作。程序文件处理数据文件中的数据，而数据文件提供程序文件需要处理的信息。例如，一个文本编辑器（程序文件）可以打开和编辑一个文本文件（数据文件），或者一个数据库管理系统（程序文件）可以查询和更新数据库文件（数据文件）中的数据。
==文件指针==
每个被使用的文件，都会在内存中开辟出一个相应的文件信息区。该信息区用来存放文件相关信息（如文件名、文件状态以及文件当前位置等）。这些信息是保存在一个结构体变量中的，该结构体类型是由系统申明的，名为 `FILE` （注意是类型）。
==perror==
`perror` 是 C 语言标准库中的一个函数，用于在发生错误时向标准错误输出（通常是终端或控制台）打印一条错误信息。这个函数会根据当前的 `errno` 值（一个全局变量，记录了上一次库函数调用失败的错误代码），查找对应的错误消息，并将其输出。

函数原型如下：

```c
void perror(const char *s);
```

- `s` 参数是一个字符串，`perror` 会在输出的错误信息前加上这个字符串。如果 `s` 是 `NULL`，则不输出任何前缀。

`perror` 的作用是提供一个简单的方式来报告错误，而不需要程序员手动编写错误消息。这个函数通常在检测到错误后被调用，例如在文件操作或其他系统调用失败后。

下面是一个使用 `perror` 的简单示例：

```c
#include <stdio.h>
#include <errno.h>

int main() {
    FILE *fp = fopen("nonexistentfile.txt", "r");
    if (fp == NULL) {
        perror("Error opening file");
        return 1;
    }
    // 文件操作...
    fclose(fp);
    return 0;
}
```

在这个例子中，如果 `fopen` 调用失败（比如因为文件不存在），`perror` 会被调用，并输出类似于 "Error opening file: No such file or directory" 的消息。这里的 "Error opening file" 是用户提供的前缀，后面跟着的是 `perror` 根据 `errno` 值查找到的错误描述。

`perror` 函数会输出一个错误消息，该消息由两部分组成：

1. **用户定义的前缀**：这是你传递给 `perror` 函数的字符串参数。如果传递的是 `NULL`，则没有前缀。
2. **错误描述**：这是 `perror` 根据全局变量 `errno` 的值来确定的错误消息。`errno` 是一个整数，它在库函数发生错误时被设置为一个特定的值，每个值对应一个预定义的错误条件。`perror` 会查找这个值对应的错误描述字符串。

错误描述字符串通常是固定的，由 C 库提供，并且是本地化的，意味着它会根据系统的区域设置进行本地化。例如，如果 `errno` 的值是 `ENOENT`（通常表示“没有那个文件或目录”），那么 `perror` 可能会输出 "No such file or directory"。

==顺序读写==
顺序读写是指数据按照一定的顺序（通常是线性顺序）被读取或写入到存储介质（如硬盘、文件等）的过程。这种读写方式遵循数据在存储介质上的物理或逻辑排列顺序，一次处理一个数据项。顺序读写在计算机科学和数据处理中非常常见，以下是一些关键点：

1. **顺序读取**：
   - 在顺序读取中，数据被按顺序从一个位置读取到另一个位置。例如，从文件的开始到结束逐行读取文本数据。
   - 顺序读取通常用于需要处理整个数据集的情况，如备份文件或处理日志文件。
2. **顺序写入**：
   - 在顺序写入中，数据被按顺序写入到存储介质的连续位置。例如，将输出结果逐行写入到一个新文件中。
   - 顺序写入通常用于生成报告或将处理结果保存到文件中。

==**复杂定义**==

1. int \*f();
   f: function returning pointer to int
2. int (\*f)()
   f: pointer to function returning int
3. char \*\*argv
   argv: pointer to pointer to char
4. int (\*daytab)[13]
   daytab: pointer to array[13] of int
5. void \*comp()
   comp: function returning pointer to void
6. void (\*comp)()
   comp: pointer to function returning void
7. char (\*(\*x())[])()
   x: function returning pointer to array[] of pointer to function returning char
8. char (\*(\*x[3])())[5]
   x: array[3] of pointer to function returning pointer to array[5] of char

**==stdint.h==**
`stdint.h`是 C 标准库中的一个头文件，它定义了一组标准的整数类型，这些类型具有明确的大小和符号。`stdint.h`头文件是在 C99 标准中引入的，目的是提供跨平台的整数类型定义，以确保在不同的系统和编译器之间具有相同的大小和行为。

### 定义的类型

`stdint.h`定义了以下类型的整数：

- **有符号整数类型**：

  - `int8_t`：8 位有符号整数
  - `int16_t`：16 位有符号整数
  - `int32_t`：32 位有符号整数
  - `int64_t`：64 位有符号整数

- **无符号整数类型**：

  - `uint8_t`：8 位无符号整数
  - `uint16_t`：16 位无符号整数
  - `uint32_t`：32 位无符号整数
  - `uint64_t`：64 位无符号整数

- **最小宽度整数类型**：

  - `int_least8_t`、`int_least16_t`、`int_least32_t`、`int_least64_t`：至少具有指定宽度的最小宽度有符号整数类型
  - `uint_least8_t`、`uint_least16_t`、`uint_least32_t`、`uint_least64_t`：至少具有指定宽度的最小宽度无符号整数类型

- **最快宽度整数类型**：

  - `int_fast8_t`、`int_fast16_t`、`int_fast32_t`、`int_fast64_t`：最快且至少具有指定宽度的有符号整数类型
  - `uint_fast8_t`、`uint_fast16_t`、`uint_fast32_t`、`uint_fast64_t`：最快且至少具有指定宽度的无符号整数类型

- **最大宽度整数类型**：
  - `intmax_t`：最大的有符号整数类型
  - `uintmax_t`：最大的无符号整数类型

### 示例

```c
#include <stdio.h>
#include <stdint.h>

int main() {
    int32_t a = 12345;
    uint32_t b = 12345;
    printf("int32_t: %d\n", a);
    printf("uint32_t: %u\n", b);
    return 0;
}
```

在这个示例中，我们使用了`int32_t`和`uint32_t`类型来定义变量`a`和`b`，并使用`printf`函数输出它们的值。通过使用`stdint.h`中的类型，我们可以确保`a`和`b`在不同平台上都具有相同的大小和行为。

### 一种神奇的应用

```c
#include <stdio.h>
#include <stdint.h>

int main() {
    double x;
    scanf("%lf", &x);

    // 使用union来访问double的内存表示
    union {
        double d;
        uint64_t i;
    } u = {x};

    // 输出64位机内码的十六进制形式
    printf("%016llX\n", u.i);

    return 0;
}
```

在`printf`函数的格式说明符中，`%016llX`用于指定输出的格式，具体含义如下：

- `%`：表示这是一个格式说明符的开始。
- `0`：表示如果输出的数字不足指定的宽度，则在左侧填充 0 以达到指定的宽度。
- `16`：表示输出的宽度为 16 个字符。如果数字的十六进制表示不足 16 位，左侧会填充 0 以达到 16 位。
- `ll`：表示`long long`类型。对于十六进制整数输出，它告诉`printf`函数`u.i`是一个 64 位的整数（`uint64_t`类型）。
- `X`：表示以十六进制大写形式输出整数。如果使用小写的`x`，则输出的是十六进制小写形式。

综上所述，`%016llX`的意思是：以十六进制大写形式输出一个 64 位整数，输出的宽度为 16 个字符，如果不足 16 位则在左侧填充 0。

**==#ifndef==**
`#ifndef` 是 C 语言预处理器的一个指令，用于条件编译。它的全称是 "if not defined"，意思是“如果没有定义”。`#ifndef` 通常与 `#define` 和 `#endif` 一起使用，用于避免头文件内容的重复包含（也称为多重包含），这在大型项目中非常常见。

### 使用 `#ifndef` 避免头文件重复包含

当你在一个项目中有多个源文件和头文件时，可能会出现一个头文件被多次包含的情况。这会导致编译错误，因为同一个符号（如函数原型或类型定义）会被多次定义。为了避免这种情况，可以使用 `#ifndef`、`#define` 和 `#endif` 来创建一个宏保护（macro guard）或头文件保护（header guard）。

下面是一个典型的使用 `#ifndef` 的头文件示例：

```c
// my_header.h
#ifndef MY_HEADER_H  // 如果 MY_HEADER_H 没有被定义
#define MY_HEADER_H  // 定义 MY_HEADER_H

// 头文件的内容
int my_function(int arg);

#endif // MY_HEADER_H
```

在这个例子中，当编译器第一次遇到 `my_header.h` 时，`MY_HEADER_H` 还没有被定义，所以它会定义 `MY_HEADER_H` 并包含头文件的内容。如果在后续的编译过程中再次遇到 `my_header.h`，`MY_HEADER_H` 已经被定义了，因此 `#ifndef MY_HEADER_H` 的条件不成立，编译器会跳过头文件的内容，从而避免了重复包含。

### 使用 `#ifndef` 进行条件编译

除了避免头文件重复包含，`#ifndef` 还可以用于条件编译，根据是否定义了某个宏来决定是否包含某些代码。例如：

```c
#ifndef USE_MY_FEATURE
// 如果 USE_MY_FEATURE 没有被定义，则包含以下代码
void my_feature_function() {
    // 实现代码
}
#endif
```

在这个例子中，如果 `USE_MY_FEATURE` 没有被定义，编译器会包含 `my_feature_function` 的定义；如果 `USE_MY_FEATURE` 被定义了，则不会包含这个函数的定义。

### 总结

- 使用 `#ifndef` 可以避免头文件的重复包含，这是通过创建宏保护来实现的。
- `#ifndef` 也可以用于条件编译，根据宏的定义情况来决定是否包含某些代码。
- 在使用 `#ifndef` 时，通常需要配合 `#define` 和 `#endif` 一起使用，以确保代码的正确性和可读性。

<br>

### **_细节_**

```c
int x = 5, y = 7;
void swap ( )
{
      int z ;

      z = x ;  x = y ;  y = z ;
}
int main(void)
{
      int x = 3, y = 8;
      swap ( ) ;  //改变的是全局变量的x,y,main函数中不变
      printf ("%d,%d \n", x , y ) ;   //输出为3,8

      return 0 ;
}
```

- 自动变量，系统不自动赋初始值
- 变量的隐含存储变量为 auto(自动型)
- 外部变量:extern
- C 语言变量按作用域分为局部变量和全局变量
- 按生存期分为静态存储方式和动态存储方式
- 静态变量的初始化在编译阶段完成

```c
#include <stdio.h>
int fun(int a,int b) {
    return a-b;
}
int a=10,b=4;
int main() {
    int a=4,b=10;
    int t=fun(a,b);  //a,b在main内部定义,传入函数中
    printf("%d\n",t); //运行结果为-6
    return 0;
}
```

```c
#include <stdio.h>
int f(int m) {
    static int n=0;
    n+=m;
    return n;
}
int main() {
    int n=0;  //n在main和f中重复定义,两个函数中的n不是同一个n
    printf("%d ",f(++n));
    printf("%d\n",f(n++)); //运行结果为1 2
    return 0;
}
```

<br>

- 用逗号运算符可以在一行中写多行语句
- 宏定义中可使用标识符,实际函数运行时定义同名变量,函数中将其替换
  举例:`#define F a+a \\ int a=3,x=9;`
  执行`x=F*F`后,x 的值为 15
- define 可以定义为用户标识符(预定义标识符可以定义为用户标识符)
  if 不能定义为用户标识符(关键字不能定义为用户标识符)
- 3< x <5 的值恒为 1
- 3\==x==0 的值恒为 0
- 控制表达分为语句级（顺序，分支，循环）和模块级（函数）
- 混合运算注意左结合和右结合
- 分支控制分为双路分支（if else）和多路分支（switch case）
- static 修饰全局变量：只能在该文件里使用，其他文件不能访问（即使加 extern 也不行）
- `If (grade<60) {…}`grade 的取值至少有三组
- 多重 if else：注意 else 配对的是最近的且不带 else 的 if
- 复合语句：用大括号包围的一系列语句，在语法上被认为是一条语句
- 标识符：用于定义变量，函数，宏
- for 后的复合语句可以为空，即 for ( ; ; ) ;语法正确
- (a&3)==(a%4)的值为 1，（因为 3 的二进制是 11，a&3 相当于取出最后两位）
- !!(x>y)和（x>y)等价
- 非零值都认为是 true
- 定义为`int a[3][2]={1,2,3,4,5,6}`，若行列超过定义，自动往后取值，如`a[1][3]`为 6
- _p++等价于_(p++)，因为++为右结合
- `char c[]=“l\t\r\\\0will\n”; \\ printf(“%d\n”strlen(c));`运行结果为 4
- `char str[10];  str[U+200E] = “string”`错误，因为字符串变量名不能被改变
- `puts`输出包含’\0’
- 函数定义中数组可规定大小
- 函数的形参和实参分别占用不同的存储单元
- c 语言源文件不一定要包含 main 函数
- 函数原型声明可以声明多次
- syntax error：语法错误
  compilation error：编译错误
- 续行符为`\`,可将一行代码写在多行
- 从小到大冒泡排序,第 i 轮将原本第 i 个位置的元素放到对应位置
- 简单选择排序即选择排序
- `int a[10]; a++;`错误.a 为数组名,不可改变值
- `int a[10];`则\*a 为 a[0]
- 指针不能相加,但是可以相减.同一数组的两指针相减,返回着两个指针之间的元素个数
- 两指针相等即指向的地址相等
- 常用类型字节数:
  - char:1 字节
  - int:4 字节
  - long long:8 字节
  - float:4 字节
  - double:8 字节

<br>

- sizeof 不是函数，是编译运算符
  `sizeof` 运算符可以用于任何数据类型，包括原始类型（如 `int`、`float`）和复合类型（如 `struct`、`union`、数组）。`sizeof` 的结果类型是 `size_t`，这是一个无符号整数类型，定义在 `stddef.h` 或 `stdint.h` 头文件中。

<br>

- c 语言报错类型

1. **语法错误（Syntax Errors）**：

   - 这些错误发生在代码不符合 C 语言的语法规则时。例如，缺少分号、括号不匹配、错误的关键字使用等。

2. **语义错误（Semantic Errors）**：

   - 语义错误是指代码在语法上正确，但在逻辑上或上下文中不正确。例如，赋值一个整数值给一个浮点变量而没有类型转换、使用未初始化的变量、函数调用时参数数量不匹配等。

3. **链接错误（Linker Errors）**：

   - 链接错误发生在编译阶段之后，当编译器试图将多个编译单元（源文件）链接成一个可执行文件时。常见的链接错误包括未定义的引用（例如，声明了函数但没有定义）和多重定义（同一个函数或变量被定义了多次）。

4. **运行时错误（Runtime Errors）**：

   - 这些错误不是在编译时检测到的，而是在程序运行时发生的。例如，数组越界、除以零、内存泄漏、野指针等。

5. **警告（Warnings）**：

   - 编译器也会报告警告，这些通常不是错误，但它们指出了可能的问题，比如未被使用的变量、可能的除以零、格式字符串警告等。虽然警告不会阻止编译过程，但它们通常指示潜在的问题，应该被认真对待。

6. **编译器特定的错误（Compiler-Specific Errors）**：

   - 这些错误是由特定编译器实现的特定限制或特性引起的。例如，某些编译器可能对代码优化级别有不同的要求，或者对某些特性的支持不同。

7. **预处理器错误（Preprocessor Errors）**：

   - 这些错误与预处理指令有关，比如宏定义错误、条件编译指令错误等。

8. **类型错误（Type Errors）**：

   - 这些错误发生在类型不匹配的情况下，比如将一个整型变量赋值给一个字符型变量而没有适当的类型转换。

9. **内存分配错误（Memory Allocation Errors）**：
   - 在动态内存分配时，如果内存不足，可能会发生错误，如 `malloc` 或 `calloc` 返回 `NULL`。

<br>

```c
for(num = 1; num <= 100; num++){
    s = 0;   //此处应int t=num;否则num值改变
    do{
       s = s + num % 10;
       num = num / 10;
    }while(num != 0);
    printf("%d\n", s);
}
```

<br>

- `ftell`:获取文件流当前位置
  在 C 语言中，`ftell`函数是用于获取文件流当前位置的函数。它定义在`<stdio.h>`头文件中，其作用是返回给定流（由`FILE*`类型的指针指向）的当前文件位置指示器的值，即从文件开头到当前位置的字节数量。

### 函数原型

`ftell`函数的原型如下：

```c
long int ftell(FILE *stream);
```

其中，`stream`参数是一个指向`FILE`对象的指针，该对象标识了流。

### 返回值

- 如果调用成功，`ftell`函数返回从文件开头算起的字节数量，即当前文件位置指示器的值。
- 如果发生错误，函数返回`-1L`，并且全局变量`errno`被设置为一个正值。

### 使用场景

`ftell`函数常用于以下场景：

1. **随机文件访问**：在随机方式存取文件时，使用`fseek`函数来回移动文件指针，不容易确定当前指针位置，通过调用`ftell`函数可以确定指针位置。
2. **获取文件大小**：通过将文件指针移动到文件末尾（使用`fseek`函数），然后使用`ftell`获取文件指针相对于文件头的偏移值，从而得到文件的大小。

### 示例代码

下面是一个使用`ftell`函数获取文件大小的示例代码：

```c
#include <stdio.h>

int main() {
    FILE *fp;
    long len;
    fp = fopen("file.txt", "r");
    if(fp == NULL) {
        perror("打开文件错误");
        return(-1);
    }
    fseek(fp, 0, SEEK_END);
    len = ftell(fp);
    fclose(fp);
    printf("file.txt 的总大小 = %ld 字节\n", len);
    return(0);
}
```

在这个示例中，首先打开名为`file.txt`的文件，然后将文件指针移动到文件末尾，最后使用`ftell`函数获取文件的大小，并打印出来。

- `feof`:检查文件流是否达到末尾
  在 C 语言中，`feof`函数用于检查文件流是否已经到达文件末尾。当从文件中读取数据时，`feof`函数可以用来确定是否已经读到了文件的末尾。

### 函数原型

`feof`函数的原型如下：

```c
int feof(FILE *stream);
```

其中，`stream`参数是一个指向`FILE`对象的指针，该对象标识了流。

### 返回值

- 如果文件末尾尚未到达，`feof`函数返回`0`。
- 如果文件末尾已经到达或发生了错误，`feof`函数返回非零值。

### 使用场景

`feof`函数常用于在读取文件时检查是否已经到达文件末尾。它通常与`fgetc`或`fgets`等读取函数一起使用，以确保在读取操作到达文件末尾时能够正确处理。

### 示例代码

下面是一个使用`feof`函数检查文件末尾的示例代码：

```c
#include <stdio.h>

int main() {
    FILE *fp;
    int c;
    fp = fopen("example.txt", "r");
    if (fp == NULL) {
        perror("文件打开失败");
        return -1;
    }

    // 读取文件直到到达文件末尾
    while ((c = fgetc(fp)) != EOF) {
        putchar(c);
    }

    // 检查是否到达文件末尾
    if (feof(fp)) {
        printf("已到达文件末尾。\n");
    }

    fclose(fp);
    return 0;
}
```

在这个示例中，程序打开一个名为`example.txt`的文件，并使用`fgetc`函数逐个字符地读取文件内容。每次读取后，都会检查是否到达文件末尾。如果`feof`返回非零值，表示已经到达文件末尾，程序将输出相应的消息。

需要注意的是，`feof`函数只有在尝试读取操作之后才会被设置为非零值，因此在调用`feof`之前至少需要进行一次读取操作。此外，如果读取操作由于其他原因（如文件错误）导致`EOF`被设置，`feof`也会返回非零值，因此在使用`feof`时需要考虑这种情况。

#### 一些关于指针占内存几位的东西

- CPU 通过数据总线,地址总线和控制总线与内存进行数据交换与操作
- 数据总线:数据总线的宽度决定 CPU 单次数据传输的传送量,即电脑的位数
- 控制总线:决定 CPU 对其他控件的控制能力以及控制方式
- 地址总线:决定 CPU 的寻址能力,或寻址的最大内存容量.
  - 若地址总线为 32 位,则一次能处理的信息位 2^32 条,描述的地址空间是 0x0000 0000~2^32-1,此时需要 32 个 0 或 1 的组合找到内存中的地址,即 4 个字节的大小
  - 所以,32 位计算机中,指针占 4 个字节
  - 64 位计算机中,指针占 8 个字节

<a id="TOP"></a>

[题目](#题目)
[知识点](#知识点)

## 细节

- source file:源文件  
  type modifier:类型修饰符  
  recursive functions:递归函数  
  concise:简明的  
  singly linked list:单链表  
  doubly linked list:双向链表  
  demical:十进制  
  character constant:字符常量  
  call functions in nest:嵌套调用函数  
  recursive-call:递归调用  
  prototype:原型  
  parameter:参数  
  compound statement:复合语句  
  call sentence:调用语句  
  be proportional to:和...成正比  
  memory:内存  
  randomly access:随机访问  
  headerfile:头文件  
  assignment statement:赋值语句  
  rules of precedence:优先级法则  
  type cast:强制类型转换  
  storage-class specifiers:存储类型说明符(如 static,extern,auto,register)  
  declaration specifier:类型说明符(如 int,char...)
- `#include "stdio.h"`也正确
- C 语言预处理功能包括宏定义,文件包含,条件编译
- 文件读写时,位置指针不断改变,文件指针不变
- 随机操作适用于文本文件,二进制文件等
- fseek 可用于文本文件,也可用于二进制文件
- 按数据的组织形式划分,可以分为文本文件和二进制文件
- 函数 fopen 中第一个参数的正确格式样例:"c:\\user\\text.txt"
- 0~1 的浮点数可将 0 省略，例如：0.18 和.18 等价,-0.18 和-.18 等价
- `a=2;`则'a'是字符 a 而不是字符 2
- `!a>b`先计算`!a`,再判断`(!a)>b`
- s 是指针,s+1 即将指针后移一位
- 非 NULL 的指针逻辑值为 1
- `!0`为 1,`!非零数`为 0
- `if (a-b) ...;`只要 a!=b 即执行(非零值都执行)
- static 可以应用于数,也可应用于数组
- switch 中 default 可以放在任何位置,且其作用相同
- `(int)浮点数`:直接去掉小数部分,保留整数部分
- `typedef struct stc {...} *p;`defines p as a pointer to struct stc
- It's illegal in C to initialize a member of struct when it's defined.
  e.g. `struct a {int n=100};` is illegal.
- C 语言中 true 不是关键字
- `a<b?a:c<d?c:d`等价于`( a < b ) ? a : ( ( c < d ) ? c : d )`,注意?和:从里到外前后配对
- 0123 表示八进制,不是 123
- 64 位架构中,所有指针都是 8 字节
- `unsigned short sht=0;sht--;`执行后 sht 下溢为 65535
- p,q 是数组中两个指针,`p-q`输出在数组中相差几个单位,`(int)p-(int)q`输出实际相差几个字符
- `char s[2][3] = {"ab", "cd"}, *p=(char*)s`p 为指向 s[0] [0]的指针,可以依次访问 s 中元素
- `*++p+2`:p -> ++p -> _++p -> _++p+2
- `m=a>b`:m=(a>b)
- 条件判断`str[i]!='\0'`和`str[i]`等价
- 如果字符数组中有\ooo 表示的字符,\ooo 视为字符而不将\0 作为结束标志
- 野指针(没赋过值,不知道指向哪里的指针)不能解引用,不能写入,只能将它指向某个地方
  - `char *s;scanf("%s",s);`是错误的,应该使用`char s[100]`
  - 如果定义时为`char *s`,应后续使用`malloc`,或另开一个字符数组`temp`然后`s=temp`
- `#ifndef`后面不区分大小写
- 默认情况下,`DeQueue`表示队首出队,`DeleteQueue`表示清空队列.
  "队列可以双端操作"正确
- 嵌套调用函数实现相似操作(比如递增排序,递减排序),可以使用函数指针,e.g. `int (*cmd)(int a,int b)`
- 定义函数时不声明类型，默认为返回 int 的函数
- `#include <math.h>`后，可使用 pow 函数，`pow(x,y)`(只要 x^y 有定义即可,不一定均为正整数)
- `printf`中-表示左对齐,+表示显示正负号,空格表示如果第一位不是正负号则加空格
- sizeof 输出字节数，而不是元素个数

## 题目

<a id="题目"></a>

[RETURN TO THE TOP](#TOP)

- 以下代码的输出为 **\_**.

```c
int x = -1;
printf("%d", (unsigned int)x);
```

unsigned int 的转换并不会改变 x 的二进制值（而是以无符号的方式来理解这段数据），而对于 printf 来说，它要输出的是一个 %d，即有符号数（无符号用 %u），所以输出时还是会当作有符号整型来理解，即输出 -1。

- (C16A) For the code below:

```c
int a, b; char c;
scanf("%d%c%d",&a,&c,&b);
```

If let a=1,b=2,c='+', the input **C \_** is NOT correct.
A. 1+2< ENTER >
B. < BLANK >< ENTER >1+< ENTER >2< ENTER>
C. < ENTER >1< ENTER >+< BLANK >2< ENTER >
D. < BLANK >< BLANK >1+< BLANK >< BLANK >2< ENTER >
%d 会忽略数字左边的空白字符（包括空格、换行等），而 %c 会立即读取一个字符。

- 以下代码的输出为 **\_**.

```c
void func(int a[5]) {
    printf("%d", sizeof(a));
}
int main() {
    int a[5] = {0};
    printf("%d\n", sizeof(a));
    func(a);
}
```

这里首先输出数组 a 占的字节数，也就是 4\*5=20。然后将 a 传入 func 函数后，a 退化为了指针（即使函数前面里类型还是 int[5]），在 func 函数中计算 sizeof(a) 的话输出的就是指针占的大小，这个值是不一定的，在 32 位架构中是 4，在 64 位架构中是 8。

- For storage-class specifiers, which one below is NOT correct? ** C \_**.
  B. A static global variable is not accessible by other compile units.
  C. A static function is accessible by other static functions in different compile units.

  - B:这个选项是正确的.静态全局变量（static 修饰的全局变量）只在声明它的编译单元（源文件）内部可见。它不会被其他编译单元访问。这种变量的作用域是文件作用域（file scope），它不能被其他文件中的函数或变量直接引用。
  - C:这个选项是错误的。静态函数（static 修饰的函数）只在定义它的编译单元内可见。静态函数的作用域是文件作用域，也就是说，它只能在定义它的源文件中被调用，不能被其他编译单元中的静态函数或其他函数访问。

- The fllowing program will output **\_ 100 \_\_\_**.

```c
#include <stdio.h>
typedef void* (*H)(int a);
void* h(int a)
{
   if(a) printf("%d", a);
   return h;
}
int main(void)
{
   ( (H) h(0) )(100);  //强制类型转换
   return 0;
}
```

- Write down the declaration of a function pointer to a void procedure(过程) f with
  two formal parameters: the first is an integer variable, the other is a pointer to an
  array of 10 integers.
  **\_\_** void (\*f)(int,int(\*)[10]); **\_\_\_**

- When input Hello,World< ENTER>, what’s the result after executing the following
  code fragment?

```c
char *str;
scanf(“%s”, str);
printf(“%s”, str);
```

**\_\_** the program may exit abnormally **\_\_**

- str 为野指针,不能赋值

- 判断:
  A. The return type of a function shall be void or an object type other than array type.

  - 解释：数组类型不能作为函数的返回类型，这意味着你不能直接返回数组。不过，你可以通过返回指向数组的指针来间接返回数组。因此，这个说法是 正确的。
    B. Each parameter of a function has automatic storage duration.
  - 解释：在 C 语言中，函数的参数默认具有自动存储期（Automatic Storage Duration，简称 ASL）。当函数被调用时，参数会在栈上分配内存，并在函数调用结束时自动销毁。因此，函数参数的存储期是 自动的，除非特别指定为 static。这个说法是 正确的。
    C. After all parameters have been assigned, the compound statement that constitutes the body of the function definition is executed.
  - 解释：这句话描述了函数执行的基本流程。函数的参数会在函数体开始执行之前被赋值，并且在所有参数赋值之后，函数体的复合语句（函数体）会被执行。这个说法是 正确的，符合 C 语言函数调用的常规流程。

- 以下代码语法正确的是 **\_**.
  A. for ( ); B. do { } while ( ); C. while ( ) ; D. for ( ; ; ) ;

  - while 的括号中必须有条件判断,BC 错

- (C13A) In the following code fragments, item _C _ is correct.
  A. int *p; scanf("%d", &p);
  B. int *p; scanf("%d", p);
  C. int k, *p=&k; scanf("%d", p);
  D. int k, *p; \*p=&k; scanf("%d", p);

  - A. 这里实际上是读入了数据写到了 p 指针的空间上（即通过输入来给指针赋值），是错误的操作；
  - B. 这里读入数据写到了 p 指向的空间中，而 p 是一个野指针，不能向它指向的空间写入数据，是错误的；
  - C. 这里将 k 的地址赋值给了 p，所以读入会写到 k 中，是正确的，选 C；
  - D. 这里 \*p=&k 一句实际上是将 k 的地址写入 p 指向的空间中，同理，p 是野指针，这个操作是错误的。

- 以下代码是否存在错误，如果有请指出哪里有问题 **\_**.

```c
char *a = "hello";
char b[] = "hello";
a[0] = 'H';
b[0] = 'H';
```

这里我们要区分的是 a 和 b。a 就是一个字符指针，它指向了 "hello" 的开头，而这个 "hello" 存在于静态存储区中，是只读的，不能进行修改，所以 a[0] = 'H' 会在运行时产生错误（可以通过编译，但是运行会报错）
而 b 是一个字符数组，它自带了栈上空间，在初始化赋值的时候 "hello" 会被复制到 b 的空间中，所以 b[0] = 'H' 是合法的。

- (C13A) Given: char format[] = "No.%d%c"; the statement printf(format, 3, \*("xyz"+2)); will print out ** No.3z \_**.

  -      printf中第一个参数可由字符数组直接代替

- (C14A) The value of expression !\*("2015-01-28"+5) is ** 0 \_**

  - 一定要区分清楚 '0' 和 '\0'，'0'==48 而 '\0'==0，所以 !'0' 是 !48 即 0

- 对于函数声明 void f(char **p)，以下哪个 var 的定义会使 f(var) 语法错误 **\_**.
  A. char var[10] [10];
  B. char *var[10];
  C. void *var = NULL;
  D. char \*v=NULL, **var=&v;

  - A. 二维数组不能退化为二级指针，所以肯定是错的
  - C. 在 C 语言中，void* 表示「指向任意类型的指针」，而这个「任意类型」也可以是 char*（即指向 char 的指针），所以它可以代表「指向指向 char 的指针的指针」（char\*\*），所以是对的

- (C13A) Given the declaration: int a[ 3 ] [ 3 ]={1,2,3,4,5,6,7,8,9};, the value of a[-1] [5] is **\_**.

首先来看 a[-1]，即 (a-1)，a-1 会以三个 int 为单位向左移动，即 (a-1) 是一个指向如下位置的指针：

```
   0 0 0 1 2 3 4 5 6 7 8 9
   ^
   |
*(a-1) = p
```

现在我们将 a[-1] 也就是 \*(a-1) 视为 p，那我们要找的结果就是 p[5]，此时 p 是一个指向 int 类型的指针，\*(p+5) 就相当于找到它指向的位置右侧第 5 个 int 的值，也就是 3。

- (C14A) Given the declaration: int a[3] [2]={1,2,3,4,5,6}; what is the value of expression (a[1]+1)[0]? **4 \_**.
  `a[1]+1`为 4 的位置,此时相当于从 4 开始的数组,`(a[1]+1)[0]`即为当前位置

- (C17A) The following code fragment will output ** ue \_**.

```c
char *week[]={"Mon", "Tue","Wed","Thu","Fri","Sat","Sun"}, **pw=week;
char c1, c2;
c1 = (*++pw)[1];
c2 = *++pw[1];
printf("%c#%c#", c1, c2);
```

- 首先 c1 = (\*++pw)[1]，++pw 使 pw 指向了 week[1]，然后 (\*++pw) 就是 week[1]，再 [1] 就是 week[1] [1] 也就是 'u'
- 然后 c2 = \*++pw[1]，这里的理解方式一定是对 pw[1] 进行 ++，pw[1] 此时是 week[2]，然后将其自增得到指向 week[2] [1] 的指针，再解引用得到 'e'

- (C15A/C16A) For the declarations: char _s, str[10];, statement ** D \_** is completely correct.
  A. strcpy(s, "hello");
  B. str="hello"+1
  C. s=_&(str+1)
  D. s=str+1
  这里涉及到了一个野指针的问题，下面会专门有一个部分
  A. 将 `"hello"` 拷贝到 s 指向的空间。但是 s 指向什么呢？你并不清楚，也就是说 s 是一个野指针，你不清楚它指向哪里，也就自然不能向它指向的空间中写入数据
  B. `str` 是一个数组，数组名不能被赋值，所以是错的
  C. `str+1` 不能被取地址，因为这是计算过程中的一个数，而不是实际存在内存中的数，所以是错的
  D. `str+1` 表示的就是 `str` 数组中第二个元素的地址，将其赋值给 s，是正确的

- In which of the following is p a pointer variable? \_ C\_\_\_\_.
  A. int* \*p(); B. int \*p(); C. int (*p)[5]; D. int \*p[6];

  - 翻译:哪个 p 是指针变量?
  - A:p 是函数指针,指向返回 int\*的函数
  - B:p 是函数,返回 int\*
  - C:p 是指向 5 个 int 的数组的指针(相比于 int p[5],这里的 p 不是常值指针)
  - D:p 是包含 6 个整型指针的数组

- **已知`unsigned short  m=65539;` 则执行语句`printf("%d", m);`后的输出结果是\_**\_3\_\_\_\_**.**

  - `unsigned short` 类型通常是 16 位无符号整数，取值范围是 `0` 到 `65535`。
  - 由于 `65539` 超出了 `unsigned short` 类型的最大值（`65535`），所以赋值 `65539` 会导致数值溢出。具体溢出的方式是：将 `65539` 对 `65536` 取模，得到 `65539 % 65536 = 3`。

- 14.下列程序段的输出结果是**\_z#yz#xyz#\_\_\_**．

```c
char s[]="xyz", *ps=s;
while (*ps++);   ps--;
for(ps--; ps-s>=0; ps--) printf("%s#",ps);
```

- \*p++后 p 指向\0 后一位

- **假设已有结构类型定义：struct point { int a, int b }；请用 typedef 把具有 5 个上述结构类型元素的数组类型重新命名为 RECT，具体形式为：\_typedef struct point RECT[5] \_\_\_;**

  - 通过 `typedef` 关键字，我们为 `struct point[5]` 创建了一个别名 `RECT`。这意味着，`RECT` 是一个新的类型，表示一个包含 5 个 `struct point` 元素的数组。

- **对于以下代码段，若输入“12e-0x34.56”（不含引号），则输出结果是**\_**12.00x34**\_\_**.**

```c
float f; char c; int d;
scanf("%f%c%d", &f, &c, &d);
printf("%.2f%c%d", f, c, d);
```

- - 12e-0 等价于 12e0 等价于 12
  - c 为 x
  - d 为 34

- **若有以下的定义和语句，则程序段运行的结果是**\_**32**\_\*\*\*\*.

```c
struct wc{ int a;int *b;}\*p;
int x0[]={11,12}, x1[]={31,32};
struct wc x[2]={100,x0,300,x1};
p=x;
printf("%d ",*++(++p)->b);
```

- - 运算顺序总结：

  1. `++p`：将指针 `p` 从 `x[0]` 递增到 `x[1]`。
  2. `(++p)->b`：访问 `x[1].b`，它指向数组 `x1`。
  3. `++(++p)->b)`：递增 `p->b` 指针，指向 `x1[1]`（值为 `32`）。
  4. `*++(++p)->b`：解引用 `p->b`，即解引用 `x1[1]`，得到值 `32`。

- **以下程序的输出是\_**\_first string\_\_\_\_**.**

```c
#include<stdio.h>
#define F "first %s"
#define D "string"
void main( )
{   char string[ ] = "character";
 printf( F, D );
}
```

- **程序中的 `printf` 语句**：

```c
printf( F, D );
```

- `F` 被展开为 `"first %s"`，所以实际调用的是 `printf("first %s", D)`。
- `D` 被展开为 `"string"`，因此 `printf` 语句变为 `printf("first %s", "string")`。
- `D`本身是字符串,不会替换成`string`

- 下列程序段的输出是**\_**7**\_**.

```c
int c=0,k;
for (k=1;k<3;k++)
   switch (k)
   {
      default: c+=k;
      case 2: c++;
      case 4: c+=2;
   }
printf("%d\n",c);
```

- 没有`break`,会从匹配的一项开始执行之后的所有项

- 各种类型表示的数的范围
- **有符号整数**的范围是 `-2^(n-1)` 到 `2^(n-1) - 1`，其中 `n` 是位数。
- **无符号整数**的范围是 `0` 到 `2^n - 1`，其中 `n` 是位数。

#### 常见类型及其取值范围（以 32 位和 64 位系统为例）：

- **`char`**: `signed char` 范围 `-128` 到 `127`，`unsigned char` 范围 `0` 到 `255`
- **`short`**: `signed short` 范围 `-32,768` 到 `32,767`，`unsigned short` 范围 `0` 到 `65,535`
- **`int`**: `signed int` 范围 `-2,147,483,648` 到 `2,147,483,647`，`unsigned int` 范围 `0` 到 `4,294,967,295`
- **`long`**: `signed long` 范围 `-2,147,483,648` 到 `2,147,483,647`，`unsigned long` 范围 `0` 到 `4,294,967,295`（32 位）
- **`long long`**: `signed long long` 范围 `-9,223,372,036,854,775,808` 到 `9,223,372,036,854,775,807`，`unsigned long long` 范围 `0` 到 `18,446,744,073,709,551,615`
- **`float`**: 范围 `1.5 × 10^−45` 到 `3.4 × 10^38`
- **`double`**: 范围 `5.0 × 10^−324` 到 `1.7 × 10^308`

<br>

## 知识点

<a id="知识点"></a>

[RETURN TO THE TOP](#TOP)

- 几个函数的使用形式

1. printf:`printf("%s",s);`
2. fprintf:`fprintf(fp,"%s",s);`
3. sprintf:`sprintf(str,"%s",s);`

4. scanf:`scanf("%d",&a);`
5. fscanf:`fscanf(fp,"%d",&a);`
6. sscanf:`sscanf(str,"%d",&a);`

7. getc:`c=getc(fp);`或`c=getc(stdin);`
8. fgetc:`c=fgetc(fp);`
9. getchar:`c=getchar();`

10. putc:`putc('A',fp);`或`putc('A',stdout);`
11. fputc:`fputc('A',fp);`
12. putchar:`putchar('A');`

13. gets:不使用
14. fgets:`fgets(str,100,fp);`或`fgets(str,100,stdin);` 保留'\n'

15. puts:`puts(str);` 自动添加'\n'
16. fputs:`fputs(str,fp);`或`fputs(str,stdout);` 不添加'\n'

返回值:

| **函数名** | **正常时返回值** | **错误时返回值** |
| ---------- | ---------------- | ---------------- |
| `printf`   | 输出的字符数     | 负值             |
| `fprintf`  | 输出的字符数     | 负值             |
| `sprintf`  | 输出的字符数     | 负值             |
| `scanf`    | 扫描的项数       | `EOF`            |
| `fscanf`   | 扫描的项数       | `EOF`            |
| `sscanf`   | 扫描的项数       | `EOF`            |
| `getc`     | 读取的字符       | `EOF`            |
| `fgetc`    | 读取的字符       | `EOF`            |
| `getchar`  | 读取的字符       | `EOF`            |
| `putc`     | 输出的字符       | `EOF`            |
| `fputc`    | 输出的字符       | `EOF`            |
| `putchar`  | 输出的字符       | `EOF`            |
| `gets`     | 字符串指针       | `NULL`           |
| `fgets`    | 字符串指针       | `NULL`           |
| `puts`     | 非负值           | `EOF`            |
| `fputs`    | 非负值           | `EOF`            |

- 关于`typedef`
  在 C 语言中，`typedef` 用来为类型定义一个新的名称，这个名称可以是任何合法的标识符。所以，**`typedef` 后不一定要使用自己定义的名称**，你可以使用 `typedef` 为现有类型（包括基础数据类型、指针类型、结构体类型等）重新命名。

#### 1. 为基础类型定义别名：

#### 2. 为结构体类型定义别名：

#### 3. 为函数指针类型定义别名：

```c
typedef int (*FunctionPointer)(int);  // 定义了一个新的类型别名 'FunctionPointer'，它是一个指向返回 int 类型并接受 int 参数的函数的指针
FunctionPointer fp;                   // 'fp' 现在是一个函数指针，指向符合这个类型的函数
```

#### 4. 直接为数组类型指定别名：

```c
typedef int Array[10];  // 为 'int[10]' 数组类型定义别名 'Array'
Array arr;              // 'arr' 就是一个包含 10 个 int 的数组
```

#### 5. 直接为指针类型指定别名：

```c
typedef int* IntPointer;  // 为 'int*' 指针类型定义别名 'IntPointer'
IntPointer ptr;           // 'ptr' 现在是一个指向 int 类型的指针
```

- 八进制转义序列
- `\ooo`

### 八进制转义序列的规则：

- 八进制转义序列以反斜杠（`\`）开始，后面跟着一个或两个八进制数字。
- 每个八进制数字只能是 `0` 到 `7` 之间的数字。
- 八进制数字最多可以有三个数字，表示一个字节（即 8 位）。因此，最多可以表示的值是 `\377`，即 255（十进制）。

- 十六进制转义序列
- `\xhh`
  其中 `hh` 是一个或多个十六进制数字（可以是 0-9 或 A-F），表示一个字符的 ASCII 码。

### 十六进制转义序列的规则：

- 十六进制转义序列以 `\x` 开头，后面可以跟一个或多个十六进制数字。
- 每个十六进制数字是 `0` 到 `9` 或 `A` 到 `F` 之间的字符。
- 十六进制转义序列最多可以表示一个字节（即 8 位），所以它的取值范围是从 `\x00` 到 `\xFF`（即 0 到 255）。

```c
typedef struct s {
    ...
} new ; //有typedef时new为结构体类型,没有typedef时new为结构体变量
```

<br>

### union

```c
#include <stdio.h>

union Data {
    int i;
    float f;
    char str[4];
};

int main() {
    union Data data;

    // 使用联合体进行数据类型转换
    data.i = 1234;
    printf("int: %d\n", data.i);  //1234
    printf("float: %f\n", data.f);  //整型的二进制对浮点数而言没有意义,输出随机浮点数
    printf("str: %s\n", data.str);  //1234的二进制表示不对应ASCII码,输出随机字符串

    // 联合体的内存共享特性
    data.f = 3.14f;
    printf("float: %f\n", data.f);
    printf("int: %d\n", data.i);
    printf("str: %s\n", data.str);

    // 位字段操作
    data.i = 0;
    data.str[0] = 0xAB; // 设置第一个字节
    printf("int: %d\n", data.i); // 输出整型值，观察第一个字节的变化

    return 0;
}
```

- 汇编代码
- 汇编代码是一种低级编程语言，它允许程序员用接近机器指令的方式来编写程序，直接控制硬件资源。每条汇编指令通常对应于 CPU 的一条机器指令，具有高效率和平台依赖性，但可读性和可维护性较差。

- IDE
- IDE 是集成开发环境（Integrated Development Environment）的缩写，它是一种软件应用程序，为开发者提供编写、调试和测试代码的综合性工具。IDE 通常包括以下功能：

1. **代码编辑器**：提供语法高亮、代码补全、代码格式化等编辑功能。
2. **编译器或解释器**：将编写的代码转换成可执行程序。
3. **调试器**：帮助开发者查找和修复代码中的错误。
4. **项目管理工具**：管理项目文件和依赖关系。
5. **版本控制**：集成 Git 等版本控制系统，方便代码的版本管理和团队协作。
6. **数据库管理**：一些 IDE 提供数据库连接和管理功能。
7. **用户界面设计**：对于图形界面应用程序，IDE 可能包含界面设计工具。
8. **代码分析工具**：检查代码质量和潜在的错误。
9. **插件和扩展**：许多 IDE 支持插件，以增加额外的功能。

- argc 怎么计数
  `argc` 是一个整数，表示命令行参数的数量。它由操作系统在程序启动时自动设置，并传递给程序。`argc` 计数的是：

1. **程序名**（`argv[0]`）作为第一个参数。
2. **通过命令行输入的参数**，每个参数用空格分隔。每个空格分隔的单词都会被当作一个独立的命令行参数。

### 具体计数规则：

- **`argc` 的值是参数个数，包含程序名**。也就是说，`argc` 的值总是至少为 1，因为 `argv[0]` 存储了程序的名称。
- 如果命令行没有额外的参数，`argc` 为 1，仅包含程序名。
- 如果命令行有多个参数，`argc` 会随着额外的参数增加。

### 例子：

1. **简单命令行输入：**
   输入命令：

   ```bash
   $ ./myprogram
   ```

   `argc = 1`，只有程序名 `./myprogram`。

2. **命令行有一个参数：**
   输入命令：

   ```bash
   $ ./myprogram hello
   ```

   `argc = 2`，`argv[0] = "./myprogram"`，`argv[1] = "hello"`。

3. **命令行有多个参数：**
   输入命令：

   ```bash
   $ ./myprogram hello world 123
   ```

   `argc = 4`，`argv[0] = "./myprogram"`, `argv[1] = "hello"`, `argv[2] = "world"`, `argv[3] = "123"`。

4. **带空格的命令行参数：**
   如果参数本身包含空格，可以使用引号将其包围，命令行只会将整个引号内的内容当作一个参数。比如：
   ```bash
   $ ./myprogram "hello world"
   ```
   `argc = 2`，`argv[0] = "./myprogram"`, `argv[1] = "hello world"`。

### `argc` 和 `argv` 例子：

```c
#include <stdio.h>

int main(int argc, char *argv[]) {
    printf("argc = %d\n", argc); // 输出参数个数

    // 打印所有命令行参数
    for (int i = 0; i < argc; i++) {
        printf("argv[%d] = %s\n", i, argv[i]);
    }

    return 0;
}
```

### 运行结果：

假设运行命令：

```bash
$ ./myprogram how are you
```

输出：

```
argc = 4
argv[0] = ./myprogram
argv[1] = how
argv[2] = are
argv[3] = you
```

### 总结：

- `argc` 计数的是传递给程序的参数个数，包含程序名。
- 每个由空格分隔的部分都会成为一个独立的命令行参数。

## 文件、字符串操作

- [Q&A](#Q&A)
- [打开文件的标准代码](#打开文件的标准代码)
- [fopen](#fopen)
- [fclose](#fclose)
- [fscanf](#fscanf)
- [fprintf](#fprintf)
- [fgetc](#fgetc)
- [fputc](#fputc)
- [fread](#fread)
- [fwrite](#fwrite)
- [fseek](#fseek)
- [feof](#feof)
- [linux 文件输入输出](#linux文件输入输出)
- [cat](#cat)

<a id="Q&A"></a>
**1.文件指针和位置指针是什么？**
文件指针和位置指针是文件操作中常用的概念，它们在 C 语言等编程语言中尤其重要。
**文件指针**：
文件指针是一个数据类型（在 C 语言中通常为`FILE*`类型），它用于在程序中唯一标识一个文件。当你打开一个文件时，操作系统会返回一个文件指针，之后你可以使用这个指针来进行读、写、关闭等操作。文件指针相当于文件的“把手”，通过它，程序可以访问文件的内容。

例如，在 C 语言中，使用`fopen`函数可以打开一个文件，并获取其文件指针：

```c
FILE *fp = fopen("example.txt", "r"); // 打开文件用于读取
if (fp != NULL) {
    // 使用fp进行文件操作
    fclose(fp); // 操作完成后关闭文件
}
```

**位置指针**：
位置指针（或称为文件位置指示器）是一个内部指针，它指示当前在文件中的位置。当你读取或写入文件时，位置指针会根据读取或写入的数据量自动移动。位置指针对于随机访问文件是非常重要的，因为它允许程序跳转到文件的任意位置。
在 C 语言中，可以使用以下函数来操作位置指针：

- `fseek()`：用于定位文件指针到文件中的指定位置。
- `ftell()`：返回文件指针的当前位置。
- `rewind()`：将位置指针重置到文件的开始位置。
  例如：

```c
FILE *fp = fopen("example.txt", "r");
if (fp != NULL) {
    fseek(fp, 10, SEEK_SET); // 将位置指针移动到文件的第10个字节
    long pos = ftell(fp); // 获取当前位置指针的值
    printf("Current position in file: %ld\n", pos);
    fclose(fp);
}
```

总结来说，文件指针是程序操作文件的接口，而位置指针用于在文件内部进行定位。两者在文件操作中起着至关重要的作用。

**2.随机操作只适用于文本文件吗？**

不是的，随机操作不仅适用于文本文件，它也适用于许多其他类型的数据文件，包括但不限于以下几种：

1. **二进制文件**：二进制文件包含以二进制形式存储的数据，这些数据可以是程序的可执行代码、图像、音频、视频或其他复杂的对象。随机操作在处理二进制文件时非常常见，因为它允许直接访问文件中的特定字节或数据结构。
2. **数据库文件**：数据库文件通常设计为支持随机访问，以便快速检索和更新记录。数据库管理系统（DBMS）利用索引和其他数据结构来优化随机访问操作。
3. **日志文件**：虽然日志文件通常是顺序写入的，但它们也可以支持随机读取，以便分析特定时间点的事件。
4. **配置文件**：配置文件通常以文本形式存储，但它们也可以是二进制格式。随机操作可以用来快速读取特定的配置项。
5. **索引文件**：索引文件包含用于快速定位其他数据的位置信息，它们依赖于随机访问来高效地工作。
   随机操作的关键在于数据的存储方式是否支持快速定位到特定位置。以下是一些支持随机操作的存储介质和数据结构：

- **硬盘驱动器（HDD）和固态驱动器（SSD）**：这些存储设备允许随机读写操作。
- **数组**：在内存中，数组是一种支持随机访问的数据结构，可以快速访问任何索引位置的元素。
- **哈希表**：哈希表通过哈希函数提供快速的随机访问能力。
  总的来说，只要文件格式和数据存储方式允许，随机操作就可以应用于多种类型的文件，而不仅仅是文本文件。

**3."a"方式打开文件后，文件指针指向哪里？**
当使用 “a” 模式（追加模式）打开文件时，文件指针会指向文件的末尾。这意味着如果文件已经存在，任何写入操作都会在文件的现有内容之后添加数据，而不会覆盖现有内容。

**4.文件的读函数将读入的信息存放在哪里？**
在 C 语言中，文件的读函数（如 `fread`、`fgets`、`fgetc` 等）会将读取的信息存放在你指定的缓冲区（buffer）中。这个缓冲区可以是一个变量、一个数组或者任何适当的数据结构，只要它有足够的空间来存储读取的数据。
**缓冲区是内存吗？**
是的，缓冲区是内存中预留的一块区域，用于临时存储数据。在文件操作中，缓冲区通常用于存储从文件读取的数据或者即将写入文件的数据。
缓冲区的使用有几个目的：

1. **减少磁盘 I/O 操作次数**：直接对磁盘进行读写操作是非常耗时的。通过使用缓冲区，可以一次性读取或写入更多的数据，减少对磁盘的操作次数，从而提高效率。
2. **数据暂存**：当程序需要处理的数据量很大时，缓冲区可以作为数据的临时存储地，使得程序可以分批处理数据，而不是一次性处理全部数据。
3. **数据转换**：在某些情况下，缓冲区还可以用于数据格式的转换。例如，从文件读取的原始二进制数据可以在缓冲区中被转换成程序内部使用的格式。
   缓冲区可以是各种类型的内存区域，例如：

- **栈内存**：在函数内部声明的局部数组通常分配在栈上，可以用作缓冲区。
- **堆内存**：使用动态内存分配（如 C 语言中的`malloc`或`calloc`）在堆上分配的内存块也可以用作缓冲区。
  在 C 语言中，当你使用标准 I/O 函数（如`fread`、`fwrite`、`fgets`、`fputs`等）时，这些函数内部通常已经使用了标准库提供的缓冲区。例如，每个`FILE`对象都有一个与之关联的缓冲区，用于减少实际的磁盘读写次数。然而，当你需要更细粒度的控制时，你可以自己定义缓冲区，并将其传递给这些函数。

**5.怎么用文件路径打开文件？**
在 C 语言中，使用 `fopen` 函数打开文件时，如果文件路径中包含反斜杠 `\`，则必须使用双反斜杠 `\\` 来转义，因为在 C 字符串中反斜杠 `\` 是一个转义字符。
选项分析如下：
A. `c:user\text.txt` - 这不是正确的路径格式，反斜杠没有转义，且没有驱动器盘符前的冒号。
B. `c:\user\text.txt` - 这也不是正确的路径格式，因为反斜杠没有转义。
C. `"c:\user\text.txt"` - 虽然使用了引号，但是反斜杠仍然没有转义，所以这个选项也是不正确的。
D. `"c:\\user\\text.txt"` - 这是正确的格式，反斜杠被正确地转义了，且整个路径被双引号包围，这是 C 语言字符串的标准写法。
因此，正确答案是 D. `"c:\\user\\text.txt"`。

**6.fgetc 打开文件用什么方式?**
函数`fgetc`用于从指定的文件流中读取一个字符。为了能够从文件中读取内容，文件必须以读模式或读写模式打开。

<span style="font-size:larger;background-color:yellow;">打开文件的标准代码</span>
<a id="打开文件的标准代码"></a>

```c
FILE *fp=fopen("filename","r");
if (fp) { //如果没有打开文件，返回NULL
    int a;
    fscanf(fp,"%d",&a);
    printf("%d\n",a);
    fclose(fp);
} else {
    printf("ERROR");
}
```

- `"r"` (read):只读.文件必须存在.
- `"w"` (write):只写.如果文件存在,则会被截断至 0 字节大小;如果文件不存在,则创建新文件.
- `"a"` (append):追加.如果文件存在，写入的数据会被添加到文件末尾;如果文件不存在,则创建新文件.
- `"r+"` (read/update):读写.文件必须存在.
- `"w+"` (write/update):读写.如果文件存在,则会被截断至 0 字节大小;如果文件不存在,则创建新文件.
- `"a+"` (append/update):读写追加.如果文件存在,写入的数据会被添加到文件末尾;如果文件不存在,则创建新文件.
- `"x"`:只新建,如果文件已存在则不能打开(防止对原有文件破坏)
  每个模式都可以与 `b` 结合使用,表示二进制模式,例如 `"rb"` 表示以二进制只读方式打开文件.在某些系统中,如果不使用 `b` 模式,可能会影响文件的读写,特别是涉及到跨平台的文件交换时。

<div STYLE="page-break-after: always;"></div>

<span style="font-size:larger;background-color:yellow;">fopen</span>
<a id="fopen"></a>
在 C 语言中,`fopen` 函数用于打开文件，它的原型定义在 `stdio.h` 头文件中。以下是如何使用 `fopen` 的步骤和示例：

1. 包含 `stdio.h` 头文件，以便可以使用 `fopen` 函数。

```c
#include <stdio.h>
```

1. 调用 `fopen` 函数，并传递两个参数：文件名和打开模式。

```c
FILE *fp = fopen("filename.txt", "r");
```

这里的 `"filename.txt"` 是你想要打开的文件的路径和名称，`"r"` 是打开模式，表示以只读方式打开文件。
`fopen` 函数返回一个 `FILE*` 类型的指针，如果文件打开成功，这个指针将被用于后续的文件操作。如果打开失败，`fopen` 将返回 `NULL`。

以下是一个完整的示例，演示如何使用 `fopen` 打开一个文件并读取其内容：

```c
#include <stdio.h>
int main() {
    FILE *fp;
    char buffer[100];
    // 打开文件
    fp = fopen("example.txt", "r");
    if (fp == NULL) {
        perror("Error opening file");
        return -1;
    }
    // 读取文件内容
    while (fgets(buffer, 100, fp) != NULL) {
        printf("%s", buffer);
    }
    // 关闭文件
    fclose(fp);
    return 0;
}
```

在这个例子中，如果文件 `example.txt` 存在并且成功打开，程序将读取文件的内容并打印到标准输出。最后，使用 `fclose` 函数关闭文件。
`perror` 是 C 语言标准库中的一个函数，用于打印出一个描述最后一次调用库函数时发生错误的信息。它的原型定义在 `stdio.h` 头文件中：

```c
void perror(const char *s);
```

当你调用 `perror` 时，它会输出参数 `s` 指定的字符串，后面跟着一个冒号、一个空格和一条错误消息。这条错误消息通常解释了为什么上一个库函数调用失败。
参数 `s` 是一个字符串，通常是你的程序中与错误相关的标识符或者提示信息。如果 `s` 是一个空指针（`NULL`），则 `perror` 只打印出错误消息，不打印前导字符串。
错误消息本身是由 `perror` 函数基于全局变量 `errno` 的当前值来生成的。`errno` 是一个在 `errno.h` 头文件中定义的外部整数变量，许多库函数在执行失败时会设置 `errno` 的值来指示具体的错误类型。
以下是一个使用 `perror` 的例子：

```c
#include <stdio.h>
#include <errno.h>
#include <unistd.h>
int main() {
    if (close(10) == -1) { // 假设10不是一个有效的文件描述符
        perror("close");
    }
    return 0;
}
```

在这个例子中，`close` 函数尝试关闭一个无效的文件描述符，这将导致 `close` 返回 `-1` 并设置 `errno`。随后调用 `perror` 将打印出类似于以下的消息：

```
close: Bad file descriptor
```

这里的 "Bad file descriptor" 是根据 `errno` 的值生成的错误描述。

<span style="font-size:larger;background-color:yellow;">fclose</span>
<a id="fclose"></a>

在 C 语言中，`fclose` 函数用于关闭一个由 `fopen` 函数打开的文件流。以下是 `fclose` 的使用步骤和示例：

1. 包含 `stdio.h` 头文件，以便可以使用 `fclose` 函数。

```c
#include <stdio.h>
```

2. 在打开文件后，当完成文件的所有操作时，调用 `fclose` 函数来关闭文件。

```c
int fclose(FILE *stream);
```

这里的 `stream` 是一个指向 `FILE` 结构的指针，它代表了你要关闭的文件流。
`fclose` 函数执行成功时返回 `0`，如果发生错误则返回 `EOF`（在 `stdio.h` 中通常定义为 `-1`）。
以下是一个示例，展示如何使用 `fclose`：

```c
#include <stdio.h>
int main() {
    FILE *fp;
    // 打开文件
    fp = fopen("example.txt", "w");
    if (fp == NULL) {
        perror("Error opening file");
        return -1;
    }
    // 写入文件内容
    fprintf(fp, "Hello, World!\n");
    // 关闭文件
    if (fclose(fp) != 0) {
        perror("Error closing file");
        return -1;
    }
    return 0;
}
```

在这个例子中，程序首先尝试以写入模式打开 `example.txt` 文件。如果文件成功打开，它将写入一行文本。完成写入操作后，程序调用 `fclose` 来关闭文件。如果 `fclose` 返回 `EOF`，表示关闭文件时发生了错误，程序将打印出错误信息并返回 `-1`。

<span style="font-size:larger;background-color:yellow;">fscanf</span>
<a id="fscanf"></a>
`fscanf` 是 C 语言标准库函数之一，它用于从文件中读取格式化的输入。这个函数与 `scanf` 类似，但是 `fscanf` 是从指定的文件流中读取数据，而不是从标准输入（键盘）。
下面是 `fscanf` 函数的基本用法：

```c
int fscanf(FILE *stream, const char *format, ...);
```

- `FILE *stream`：这是一个指向 `FILE` 对象的指针，该对象标识了要从中读取数据的文件流。
- `const char *format`：这是一个字符串，指定了数据的格式，与 `scanf` 的格式字符串相同。
- `...`：这是一个变量列表，用于存储从文件中读取的数据。
  `fscanf` 函数的返回值是成功匹配并赋值的输入项个数,如果遇到错误或文件结束(EOF),则返回 EOF。
  下面是一些 `fscanf` 的使用示例：

### 读取整数

```c
#include <stdio.h>
int main() {
    FILE *file = fopen("data.txt", "r");
    int number;
    if (file != NULL) {
        while (fscanf(file, "%d", &number) != EOF) {
            printf("Read number: %d\n", number);
        }
        fclose(file);
    }
    return 0;
}
```

在这个例子中，`fscanf` 从 `data.txt` 文件中读取整数，直到文件结束。

### 读取字符串

```c
#include <stdio.h>
int main() {
    FILE *file = fopen("data.txt", "r");
    char buffer[100];
    if (file != NULL) {
        while (fscanf(file, "%99s", buffer) != EOF) { // 注意：使用 %99s 以避免缓冲区溢出
            printf("Read string: %s\n", buffer);
        }
        fclose(file);
    }
    return 0;
}
```

在这个例子中，`fscanf` 从 `data.txt` 文件中读取字符串，直到文件结束。注意，我们使用 `%99s` 来限制读取的字符数，避免超出 `buffer` 的大小。

### 读取多种类型的数据

```c
#include <stdio.h>
int main() {
    FILE *file = fopen("data.txt", "r");
    int number;
    char name[50];
    if (file != NULL) {
        while (fscanf(file, "%d %49s", &number, name) != EOF) {
            printf("Number: %d, Name: %s\n", number, name);
        }
        fclose(file);
    }
    return 0;
}
```

在这个例子中，`fscanf` 一次读取一个整数和一个字符串，直到文件结束。
记住，`fscanf` 会跳过任何空白字符（空格、制表符、换行符等），直到遇到与格式字符串不匹配的字符。如果读取的数据类型与格式字符串不匹配，`fscanf` 可能会失败或产生未定义的行为。

<br>

<span style="font-size:larger;background-color:yellow;">fprintf</span>
<a id="fprintf"></a>
`fprintf` 是 C 语言标准库中的一个函数，用于将格式化的数据写入文件流。它与 `printf` 函数非常相似，但 `fprintf` 允许你指定一个文件指针，这样就可以将数据写入到文件中，而不是打印到标准输出（通常是屏幕）。
下面是 `fprintf` 函数的基本原型：

```c
int fprintf(FILE *stream, const char *format, ...);
```

- `FILE *stream`：这是一个指向 `FILE` 对象的指针，该对象标识了要写入数据的文件流。
- `const char *format`：这是一个字符串，指定了数据的输出格式，与 `printf` 的格式字符串相同。
- `...`：这是一个变量参数列表，包含了根据 `format` 字符串指定的格式要写入的数据。
  `fprintf` 函数的返回值是成功写入的字符数，或者在发生错误时返回一个负数。
  下面是一个使用 `fprintf` 的简单例子：

```c
#include <stdio.h>
int main() {
    FILE *file = fopen("example.txt", "w"); // 打开文件用于写入
    if (file == NULL) {
        perror("Error opening file");
        return -1;
    }
    int number = 42;
    const char *text = "The answer to life, the universe, and everything";
    // 将格式化的字符串写入文件
    fprintf(file, "Number: %d\nText: %s\n", number, text);
    fclose(file); // 关闭文件
    return 0;
}
```

在这个例子中：

1. 我们首先使用 `fopen` 函数打开一个名为 "example.txt" 的文件，以供写入（"w" 模式）。
2. 我们检查 `fopen` 是否成功返回了一个有效的文件指针。
3. 使用 `fprintf` 函数，我们将一个整数和一个字符串按照指定的格式写入到文件中。格式字符串包含了 `%d` 用于整数和 `%s` 用于字符串。
4. 最后，我们使用 `fclose` 函数关闭文件。
   注意，如果文件打开模式是 "w"，则每次执行程序时，"example.txt" 文件都会被覆盖。如果想要追加内容到文件末尾，应该使用 "a" 模式打开文件。

<br>

<span style="font-size:larger;background-color:yellow;">fgetc</span>
<a id="fgetc"></a>
`fgetc` 是 C 语言标准库中的一个函数，用于从指定的文件流中读取下一个字符。以下是 `fgetc` 的基本用法：

### 函数原型

```c
int fgetc(FILE *stream);
```

- `FILE *stream`：这是一个指向 `FILE` 对象的指针，该对象标识了要从中读取字符的文件流。

### 返回值

- `fgetc` 函数返回读取到的字符，如果到达文件末尾或发生读取错误，则返回 `EOF`（通常是一个负数，例如 `-1`）。

### 使用示例

下面是一个简单的例子，演示如何使用 `fgetc` 从文件中读取字符：

```c
#include <stdio.h>
int main() {
    FILE *file = fopen("example.txt", "r"); // 打开文件用于读取
    if (file == NULL) {
        perror("Error opening file"); // 如果文件打开失败，打印错误信息
        return -1;
    }
    int ch; // 用于存储读取到的字符
    while ((ch = fgetc(file)) != EOF) { // 循环直到文件末尾
        putchar(ch); // 将读取到的字符打印到标准输出
    }
    fclose(file); // 关闭文件
    return 0;
}
```

在这个例子中：

1. 使用 `fopen` 函数打开一个名为 "example.txt" 的文件用于读取。
2. 检查 `fopen` 返回的文件指针是否为 `NULL`，如果是，则打印错误信息并返回错误代码。
3. 使用 `fgetc` 在一个循环中读取文件中的每个字符，直到 `EOF` 被返回。
4. 使用 `putchar` 函数将读取到的字符打印到标准输出。
5. 使用 `fclose` 函数关闭文件。
   请注意，当 `fgetc` 返回 `EOF` 时，并不一定意味着发生了错误，它也可能是正常到达了文件末尾。要区分这两种情况，可以检查 `ferror` 函数的返回值。如果 `ferror(file)` 返回非零值，则表示在读取过程中发生了错误。

<span style="font-size:larger;background-color:yellow;">fputc</span>
<a id="fputc"></a>
`fputc` 是 C 语言标准库函数，用于将一个字符写入到指定的文件流中。其原型定义在 `stdio.h` 头文件中：

```c
int fputc(int char, FILE *stream);
```

下面是 `fputc` 函数的使用步骤和示例：

### 参数说明：

- `char`：需要写入文件的字符，以 `int` 类型传递，但是通常会传递一个 `char` 类型的值。
- `stream`：指向 `FILE` 类型的指针，代表了要写入字符的文件流。

### 返回值：

- 成功：返回写入的字符（即 `char` 参数的值）。
- 失败：返回 `EOF`（通常在 `stdio.h` 中定义为 `-1`）。

### 使用示例：

```c
#include <stdio.h>
int main() {
    FILE *fp = fopen("example.txt", "w"); // 打开文件用于写入
    if (fp == NULL) {
        perror("Error opening file");
        return -1;
    }
    char ch = 'A'; // 要写入的字符
    // 将字符 'A' 写入文件
    if (fputc(ch, fp) == EOF) {
        perror("Error writing to file");
        fclose(fp); // 关闭文件
        return -1;
    }
    // 可以继续写入其他字符
    fputc('B', fp);
    fputc('\n', fp); // 写入换行符
    fclose(fp); // 关闭文件
    return 0;
}
```

在这个例子中，程序首先尝试打开一个名为 `example.txt` 的文件用于写入。如果文件成功打开，它将使用 `fputc` 函数写入字符 'A'，然后是 'B' 和一个换行符。每调用一次 `fputc`，它都会检查返回值是否为 `EOF` 来确定写入是否成功。最后，文件被关闭。
请注意，在使用 `fputc` 之前，应该确保文件已经成功打开，并且在写入完成后，应该关闭文件以释放资源。如果写入过程中发生错误，`fputc` 将返回 `EOF`，并且可以通过调用 `perror` 来获取错误信息。

<span style="font-size:larger;background-color:yellow;">fread</span>
<a id="fread"></a>
`fread` 是 C 语言标准库函数，用于从文件流中读取数据块。它通常用于读取二进制文件或者需要一次性读取多个数据项的情况。以下是 `fread` 的基本用法：

### 函数原型

```c
size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);
```

- `void *ptr`：指向要读取数据的缓冲区的指针。
- `size_t size`：要读取的每个元素的大小（以字节为单位）。
- `size_t nmemb`：要读取的元素个数。
- `FILE *stream`：指向 `FILE` 对象的指针，该对象标识了要从中读取数据的文件流。

### 返回值

`fread` 函数返回成功读取的元素个数，这个数可能会小于 `nmemb` 指定的元素个数，特别是在到达文件末尾时。

### 使用示例

下面是一个使用 `fread` 的例子，它从一个二进制文件中读取一系列整数：

```c
#include <stdio.h>
#include <stdlib.h>
int main() {
    FILE *file = fopen("data.bin", "rb"); // 打开文件用于二进制读取
    if (file == NULL) {
        perror("Error opening file"); // 如果文件打开失败，打印错误信息
        return -1;
    }
    int numbers[10]; // 假设文件中有10个整数
    size_t elements_read;
    // 从文件中读取10个整数到numbers数组中
    elements_read = fread(numbers, sizeof(int), 10, file);
    if (elements_read == 10) {
        printf("Successfully read 10 integers from the file.\n");
        // 打印读取到的整数
        for (int i = 0; i < 10; ++i) {
            printf("%d ", numbers[i]);
        }
        printf("\n");
    } else {
        printf("Could not read 10 integers. Only %zu integers were read.\n", elements_read);
    }
    fclose(file); // 关闭文件
    return 0;
}
```

在这个例子中：

1. 使用 `fopen` 函数以二进制读取模式打开名为 "data.bin" 的文件。
2. 检查 `fopen` 返回的文件指针是否为 `NULL`，如果是，则打印错误信息并返回错误代码。
3. 使用 `fread` 从文件中读取 10 个整数到 `numbers` 数组中。
4. 检查 `fread` 返回的读取元素个数是否为 10，如果是，则打印读取到的整数；如果不是，则打印实际读取的元素个数。
5. 使用 `fclose` 函数关闭文件。
   请注意，`fread` 不会在读取到的数据后自动添加空字符（null terminator），所以它通常用于读取二进制数据或结构体。如果你正在读取文本数据，并且需要以字符串的形式处理这些数据，那么应该使用 `fgets` 或 `fgetc`。

<br>

<span style="font-size:larger;background-color:yellow;">fwrite</span>
<a id="fwrite"></a>
`fwrite` 是 C 语言标准库函数，用于将数据块写入文件流。它通常用于写入二进制文件或者需要一次性写入多个数据项的情况。以下是 `fwrite` 的基本用法：

### 函数原型

```c
size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream);
```

- `const void *ptr`：指向要写入数据的缓冲区的指针。
- `size_t size`：要写入的每个元素的大小（以字节为单位）。
- `size_t nmemb`：要写入的元素个数。
- `FILE *stream`：指向 `FILE` 对象的指针，该对象标识了要写入数据的文件流。

### 返回值

`fwrite` 函数返回成功写入的元素个数，这个数通常会等于 `nmemb` 指定的元素个数，除非出现错误。

### 使用示例

下面是一个使用 `fwrite` 的例子，它将一系列整数写入到一个二进制文件中：

```c
#include <stdio.h>
#include <stdlib.h>
int main() {
    FILE *file = fopen("data.bin", "wb"); // 打开文件用于二进制写入
    if (file == NULL) {
        perror("Error opening file"); // 如果文件打开失败，打印错误信息
        return -1;
    }
    int numbers[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}; // 要写入的整数数组
    // 将数组中的10个整数写入到文件中
    size_t elements_written = fwrite(numbers, sizeof(int), 10, file);
    if (elements_written == 10) {
        printf("Successfully wrote 10 integers to the file.\n");
    } else {
        printf("Could not write 10 integers. Only %zu integers were written.\n", elements_written);
    }
    fclose(file); // 关闭文件
    return 0;
}
```

在这个例子中：

1. 使用 `fopen` 函数以二进制写入模式打开名为 "data.bin" 的文件。
2. 检查 `fopen` 返回的文件指针是否为 `NULL`，如果是，则打印错误信息并返回错误代码。
3. 使用 `fwrite` 将 `numbers` 数组中的 10 个整数写入到文件中。
4. 检查 `fwrite` 返回的写入元素个数是否为 10，如果是，则打印成功消息；如果不是，则打印实际写入的元素个数。
5. 使用 `fclose` 函数关闭文件。
   请注意，`fwrite` 不会在写入的数据后自动添加空字符（null terminator），因此它适合于写入二进制数据或结构体。如果你需要写入文本数据并且需要在每个数据项后添加空字符，那么你应该手动添加这些空字符或者使用其他适合文本数据的函数，如 `fprintf` 或 `fputs`。

<br>

<span style="font-size:larger;background-color:yellow;">fseek</span>
<a id="fseek"></a>
`fseek` 是 C 语言标准库函数，用于在文件中移动文件指针到指定的位置。它的原型定义在 `<stdio.h>` 头文件中，以下是 `fseek` 函数的声明：

```c
int fseek(FILE *stream, long int offset, int whence);
```

以下是 `fseek` 函数的参数说明：

- `FILE *stream`：指向 FILE 对象的指针，该 FILE 对象标识了要操作的文件流。
- `long int offset`：相对于 `whence` 参数指定的位置的偏移量。这个偏移量可以是正数也可以是负数。
- `int whence`：指定 `offset` 参数是基于哪个位置进行偏移的，它可以是以下三个宏之一：
  - `SEEK_SET`：文件的开头（偏移量应该是相对于文件开头的）。
  - `SEEK_CUR`：文件指针的当前位置（偏移量应该是相对于当前位置的）。
  - `SEEK_END`：文件的末尾（偏移量应该是相对于文件末尾的）。
    `fseek` 函数成功时返回 0，出错时返回非 0 值。
    以下是一些使用 `fseek` 的示例：

1. 移动到文件开头：

```c
fseek(fp, 0, SEEK_SET);
```

2. 从当前位置向后移动 10 个字节：

```c
fseek(fp, -10, SEEK_CUR);
```

3. 移动到文件末尾前的 100 个字节：

```c
fseek(fp, -100, SEEK_END);
```

在使用 `fseek` 之后，如果想要获取当前文件指针的位置，可以使用 `ftell` 函数。
请注意，`fseek` 函数通常用于二进制文件操作，因为文本文件中的换行符在不同的操作系统上可能有不同的表示（例如，Windows 上是 `\r\n`，而 Unix/Linux 上是 `\n`），这可能会影响 `fseek` 的精确位置计算。如果要在文本文件中定位，通常建议使用二进制模式打开文件。

`SEEK_SET`、`SEEK_CUR` 和 `SEEK_END` 是在 C 语言标准库中定义的宏，它们用于 `fseek` 函数中，以指定文件指针移动的参考位置。以下是这三个宏的含义：

1. `SEEK_SET`:
   - 这是一个常量，其值为 0。
   - 当使用 `fseek` 函数时，如果 `whence` 参数设置为 `SEEK_SET`，则 `offset` 参数指定的偏移量是相对于文件开头的。
   - 例如，`fseek(fp, 100, SEEK_SET);` 会将文件指针移动到文件开头之后的第 100 个字节。
2. `SEEK_CUR`:
   - 这是一个常量，其值为 1。
   - 当使用 `fseek` 函数时，如果 `whence` 参数设置为 `SEEK_CUR`，则 `offset` 参数指定的偏移量是相对于文件指针的当前位置。
   - 例如，`fseek(fp, 50, SEEK_CUR);` 会将文件指针从当前位置向前移动 50 个字节。
3. `SEEK_END`:
   - 这是一个常量，其值为 2。
   - 当使用 `fseek` 函数时，如果 `whence` 参数设置为 `SEEK_END`，则 `offset` 参数指定的偏移量是相对于文件末尾的。
   - 例如，`fseek(fp, -10, SEEK_END);` 会将文件指针移动到文件末尾之前的第 10 个字节。
     这些宏定义在 `<stdio.h>` 头文件中，因此在使用它们之前需要包含该头文件。通过这些宏，`fseek` 函数能够灵活地在文件中定位到特定的位置，进行读取或写入操作。

<span style="font-size:larger;background-color:yellow;">feof</span>
<a id="feof"></a>
`feof` 是 C 语言标准库中的一个函数，用于检测流上的文件结束标志（end-of-file）。当在对文件进行读取操作时，如果已经到达文件末尾，`feof` 函数会返回一个非零值（通常是 `1`），表示文件结束。如果尚未到达文件末尾，则返回 `0`。
函数原型如下：

```c
int feof(FILE *stream);
```

参数 `stream` 是一个指向 `FILE` 对象的指针，该对象代表了与某个文件相关联的流。
以下是一些关于 `feof` 函数的要点：

- `feof` 仅在执行了文件读取操作并且该操作遇到了文件末尾时，才会设置文件结束标志。因此，在调用 `feof` 之前，应该先尝试读取文件。
- 如果在读取操作后立即调用 `feof`，并且它返回 `0`，这并不意味着后续的读取操作一定不会遇到文件结束。可能还需要进行下一次读取尝试，然后再次检查 `feof`。
- 当检测到文件结束标志时，应该停止读取操作，否则可能会读取到无效的数据或导致未定义的行为。
- `feof` 不会重置文件结束标志，一旦设置了，它将保持设置状态直到关闭文件或清除错误标志。
  以下是一个使用 `feof` 检测文件结束的简单示例：

```c
#include <stdio.h>
int main() {
    FILE *fp = fopen("example.txt", "r");
    if (fp == NULL) {
        perror("Error opening file");
        return -1;
    }
    int c;
    while ((c = fgetc(fp)) != EOF) {
        putchar(c);
        if (feof(fp)) {
            break; // 文件结束，退出循环
        }
    }
    fclose(fp);
    return 0;
}
```

在这个例子中，程序打开一个文件并逐字符读取，直到遇到文件结束。使用 `feof` 来检测是否到达了文件末尾，并在必要时退出循环。

<span style="font-size:larger;background-color:yellow;">linux 文件输入输出</span>
<a id="linux文件输入输出"></a>
在 Linux 终端中输入输出文件通常指的是读取文件内容（输入）和将数据写入文件（输出）。以下是一些基本的命令和使用方法：

### 输出（写入）到文件

1. **使用重定向符号 `>` 和 `>>`**:
   - `>` 用于创建新文件或覆盖现有文件。
   - `>>` 用于在现有文件末尾追加内容。
     示例：
   ```bash
   echo "Hello, World!" > hello.txt  # 创建或覆盖文件 hello.txt
   echo "再见" >> hello.txt          # 在文件 hello.txt 末尾追加内容
   ```
2. **使用命令的输出重定向**:
   命令的输出可以使用 `>` 或 `>>` 被重定向到文件。
   示例：
   ```bash
   ls -l > directory_listing.txt  # 将目录列表写入文件
   ```

### 输入（读取）文件

1. **使用命令读取文件**:
   许多命令可以直接读取文件作为输入。
   示例：
   ```bash
   cat hello.txt  # 显示文件内容
   less hello.txt # 分页显示文件内容
   ```
2. **使用管道 `|`**:
   管道可以将一个命令的输出作为另一个命令的输入。
   示例：
   ```bash
   cat hello.txt | grep "Hello"  # 从文件中查找包含 "Hello" 的行
   ```
3. **使用输入重定向 `<`**:
   使用 `<` 可以将文件内容作为命令的输入。
   示例：
   ```bash
   sort < hello.txt  # 对文件内容进行排序
   ```

### 示例：结合输入输出

假设你想将一个文件的内容排序后写入另一个文件：

```bash
sort < unsorted.txt > sorted.txt
```

在这个例子中，`sort` 命令从文件 `unsorted.txt` 读取内容，排序后将其输出到 `sorted.txt`。
这些是基本的文件输入输出操作，实际使用时可以根据需要进行组合和扩展。

<span style="font-size:larger;background-color:yellow;">cat</span>
<a id="cat"></a>
`cat` 是 Linux 和类 Unix 操作系统中的一个常用命令，它的名字来源于 "concatenate"（连接）的缩写。`cat` 命令的主要用途是查看文件内容、创建文件、文件内容合并以及基本的文本处理。
以下是 `cat` 命令的一些常见用法：

1. **查看文件内容**：
   ```bash
   cat filename.txt
   ```
   这会显示 `filename.txt` 文件的内容。
2. **创建文件或向文件追加内容**：
   ```bash
   cat > filename.txt
   ```
   按下回车后，你可以开始输入文本。当你完成输入并按下 `Ctrl + D` 时，输入的文本会被写入 `filename.txt`。如果文件已存在，这个命令会覆盖原有内容。
   要追加内容而不是覆盖，可以使用：
   ```bash
   cat >> filename.txt
   ```
3. **合并文件内容**：
   ```bash
   cat file1.txt file2.txt > combined.txt
   ```
   这会将 `file1.txt` 和 `file2.txt` 的内容合并后写入 `combined.txt`。
4. **与管道配合使用**：
   `cat` 命令常与其他命令通过管道（`|`）配合使用，例如，可以用来发送文件内容到其他命令进行处理：
   ```bash
   cat filename.txt | grep "keyword"
   ```
   这会显示 `filename.txt` 中包含 "keyword" 的所有行。
   `cat` 命令是学习 Linux 命令行时的基础工具之一，因为它简单且功能多样。然而，对于查看大文件，`cat` 可能不是最佳选择，因为它会一次性加载整个文件内容，这时可以使用 `less` 或 `more` 命令来分页查看。

<br>

**上课代码:**

```c
#include <stdio.h>
#include <ctype.h>
int main()
{
    int c;
    FILE *fpin,*fpout;
    char s[101];

    fpin=fopen("upper.txt","r");
    fpout=fopen("upper2.txt","a+");
    while ((c=fgetc(fpin))!=EOF)
    {
        fputc(tolower(c),fpout);
    }

    fscanf(fpout,"%s",s);
    printf("%s",s);

    fseek(fpout,12L,0);

    fclose(fpin);
    fclose(fpout);
    return 0;
}
```

#### memcpy

`memcpy` 函数在 C 语言中用于在内存中复制一个块的内容到另一个块。以下是 `memcpy` 函数的原型，它定义在 `<string.h>` 头文件中：

```c
void *memcpy(void *dest, const void *src, size_t n);
```

参数说明：

- `dest`：指向目标内存块的指针，即复制的数据将要被放置的地方。
- `src`：指向源内存块的指针，即要复制的数据的起始位置。
- `n`：要复制的字节数。
  `memcpy` 函数返回一个指向目标内存块 `dest` 的指针。
  以下是如何使用 `memcpy` 函数的一个例子：

```c
#include <stdio.h>
#include <string.h>
int main() {
    char src[50] = "Hello, World!";
    char dest[50];
    // 使用 memcpy 复制字符串
    memcpy(dest, src, strlen(src) + 1); // +1 是为了包含字符串的空终止符 '\0'
    printf("Source: %s\n", src);
    printf("Destination: %s\n", dest);
    return 0;
}
```

在这个例子中，我们有一个源字符串 `src` 和一个目标字符串数组 `dest`。我们使用 `memcpy` 来复制 `src` 中的内容到 `dest` 中。注意，我们传递给 `memcpy` 的字节数是 `strlen(src) + 1`，这是因为我们需要复制字符串中的所有字符以及字符串末尾的空终止符 `\0`。
注意事项：

- 确保 `dest` 指向的内存块足够大，能够容纳从 `src` 复制过来的 `n` 个字节，以避免内存溢出。
- `memcpy` 不会检查源和目标内存块之间是否有重叠，如果存在重叠，应该使用 `memmove` 函数，它会正确处理重叠区域的复制。
- `memcpy` 函数不会在目标内存块后添加空终止符 `\0`，所以如果你正在复制字符串，需要确保手动复制空终止符。

#### memmove

`memmove` 函数在 C 语言中用于在内存中复制一个块的内容到另一个块，即使这两个块有重叠也是安全的。以下是 `memmove` 函数的原型，它定义在 `<string.h>` 头文件中：

```c
void *memmove(void *dest, const void *src, size_t n);
```

参数说明：

- `dest`：指向目标内存块的指针，即复制的数据将要被放置的地方。
- `src`：指向源内存块的指针，即要复制的数据的起始位置。
- `n`：要复制的字节数。
  `memmove` 函数返回一个指向目标内存块 `dest` 的指针。
  以下是如何使用 `memmove` 函数的一个例子：

```c
#include <stdio.h>
#include <string.h>
int main() {
    char buffer[50] = "This is a string, and it will be modified.";
    // 使用 memmove 在同一内存块内移动数据
    memmove(buffer + 10, buffer + 15, 10); // 将 "and it" 移动到 "This is a " 之后
    printf("Resulting string: %s\n", buffer);
    return 0;
}
```

在这个例子中，我们有一个字符数组 `buffer`，我们使用 `memmove` 来在数组内部移动数据。我们移动了从索引 15 开始的 10 个字节（即字符串 "and it"）到从索引 10 开始的位置。这样做之后，原来的字符串 "This is a string, and it will be modified." 被修改为 "This is a and it string, will be modified."。
注意事项：

- 与 `memcpy` 不同，`memmove` 能够正确处理源和目标内存块重叠的情况。
- 确保 `dest` 指向的内存块足够大，能够容纳从 `src` 复制过来的 `n` 个字节，以避免内存溢出。
- `memmove` 函数不会在目标内存块后添加空终止符 `\0`，所以如果你正在复制字符串，需要确保手动复制空终止符，或者在移动后手动设置字符串的结尾。

#### memcmp

`memcmp` 函数在 C 语言中用于比较两个内存块的前 `n` 个字节。以下是 `memcmp` 函数的原型，它定义在 `<string.h>` 头文件中：

```c
int memcmp(const void *s1, const void *s2, size_t n);
```

参数说明：

- `s1`：指向第一个内存块的指针。
- `s2`：指向第二个内存块的指针。
- `n`：要比较的字节数。
  `memcmp` 函数返回一个整数，其结果有以下三种情况：
- 如果返回值 < 0，则表示 `s1` 指向的内存块小于 `s2` 指向的内存块（按字节比较）。
- 如果返回值 > 0，则表示 `s1` 指向的内存块大于 `s2` 指向的内存块。
- 如果返回值 = 0，则表示两个内存块的前 `n` 个字节相等。
  以下是如何使用 `memcmp` 函数的一个例子：

```c
#include <stdio.h>
#include <string.h>
int main() {
    char str1[] = "Hello, World!";
    char str2[] = "Hello, world!";
    size_t n = 12; // 比较前12个字节
    int result = memcmp(str1, str2, n);
    if (result < 0) {
        printf("str1 is less than str2.\n");
    } else if (result > 0) {
        printf("str1 is greater than str2.\n");
    } else {
        printf("str1 is equal to str2.\n");
    }
    return 0;
}
```

在这个例子中，我们比较了 `str1` 和 `str2` 的前 12 个字节。由于 `str1` 中的 "World" 中的 "W" 大写，而 `str2` 中的 "world" 中的 "w" 小写，比较的结果是 `str1` 大于 `str2`，因此输出 "str1 is greater than str2."。
注意事项：

- `memcmp` 比较的是内存中的实际字节值，不区分字符的大小写。
- 如果比较的是字符串，确保比较的字节长度不超过字符串的实际长度，否则可能会比较到未定义的内存区域。
- 当比较的是以空字符 `\0` 结尾的字符串时，通常比较到第一个字符串的结尾即可，即 `n` 可以是字符串的长度，不包括空终止符。

#### memchr

`memchr` 函数在 C 语言中用于在指定的内存块中查找第一次出现的字符(只能查找单个字符)。这个函数定义在 `<string.h>` 头文件中。以下是 `memchr` 函数的原型：

```c
void *memchr(const void *s, int c, size_t n);
```

参数说明：

- `s`：指向要搜索的内存块的指针。
- `c`：要查找的字符（以 `int` 类型传递，但函数内部会将其转换为 `unsigned char`）。
- `n`：要在其中搜索的内存块的字节数。
  如果 `memchr` 在内存块中找到了指定的字符，它会返回指向该字符的指针。如果没有找到，函数返回 `NULL`。
  以下是如何使用 `memchr` 函数的一个例子：

```c
#include <stdio.h>
#include <string.h>
int main() {
    const char str[] = "Hello, World!";
    char to_find = 'W';
    // 在 str 中查找字符 'W'
    void *ptr = memchr(str, to_find, strlen(str));
    if (ptr != NULL) {
        // 找到了字符 'W'
        printf("Found '%c' at position: %ld\n", to_find, (long)(ptr - str));
    } else {
        // 没有找到字符 'W'
        printf("Character '%c' not found.\n", to_find);
    }
    return 0;
}
```

在这个例子中，我们在字符串 `str` 中查找字符 'W'。如果找到了，`memchr` 会返回指向该字符的指针，我们可以通过减去原始字符串的指针来计算字符的位置。
输出结果将是：

```
Found 'W' at position: 7
```

这里的位置是从 0 开始的索引。请注意，在计算位置时，我们假设 `str` 是一个以 null 结尾的字符串，并且 `ptr` 和 `str` 都是指向 `char` 类型的指针。如果 `str` 是其他类型的数组，计算位置的方式可能会有所不同。

#### memset

`memset` 函数在 C 语言中用于将一段内存块中的前 `n` 个字节设置为特定的值。这个函数定义在 `<string.h>` 头文件中。以下是 `memset` 函数的原型：

```c
void *memset(void *s, int c, size_t n);
```

参数说明：

- `s`：指向要设置值的内存块的指针。
- `c`：要设置的值。这个值会被转换为 `unsigned char` 类型，然后填充到内存块中。
- `n`：要设置的内存块的字节数。
  `memset` 函数返回一个指向被设置内存块的指针，通常与 `s` 相同。
  以下是如何使用 `memset` 函数的一个例子：

```c
#include <stdio.h>
#include <string.h>
int main() {
    char str[50] = "This is a sample string.";
    // 将字符串的前5个字符设置为字符 'X'
    memset(str, 'X', 5);
    // 输出结果
    printf("Modified string: %s\n", str);
    return 0;
}
```

在这个例子中，`str` 是一个字符数组，我们使用 `memset` 将它的前 5 个字节设置为字符 'X'。输出结果将是：

```
Modified string: XXXXX is a sample string.
```

注意事项：

- `memset` 用于设置字节，而不是设置特定的数据类型（如 int、float 等）。因此，当使用 `memset` 设置非字符类型的数据时，需要谨慎，因为它可能不会产生预期的结果。
- 当 `c` 不是一个字符（即 `char` 类型）时，只有 `c` 的最低字节会被用来填充内存，其他字节会被忽略。
- 如果 `s` 是一个指向结构体或对象的指针，使用 `memset` 可能会导致结构体或对象的成员被错误地初始化，特别是如果成员的大小不是 1 字节时。
- `memset` 不会自动处理字符串的结尾空字符 `\0`，所以当用于字符串时，应确保不会覆盖结尾的空字符，除非有意这样做。

以下是 17 个以 `str` 开头的函数的介绍、作用、返回值、使用语句和简单解释：

1. strcpy(dest, src);

- 作用：复制字符串 `src` 到 `dest`。
- 返回值：返回 `dest` 的指针。
- 使用语句：`strcpy(buffer, "Hello");`
- 解释：将字符串 `"Hello"` 复制到 `buffer` 中。

2. strncpy(dest, src, n);

- 作用：复制 `src` 中的最多 `n` 个字符到 `dest`。
- 返回值：返回 `dest` 的指针。
- 使用语句：`strncpy(buffer, "Hello", 4);`
- 解释：将字符串 `"Hello"` 的前 4 个字符复制到 `buffer` 中。

3. strcat(dest, src);

- 作用：将字符串 `src` 连接到 `dest` 的末尾。
- 返回值：返回 `dest` 的指针。
- 使用语句：`strcat(buffer, " World");`
- 解释：将字符串 `" World"` 连接到 `buffer` 的末尾。

4. strncat(dest, src, n);

- 作用：将 `src` 中的最多 `n` 个字符连接到 `dest` 的末尾。
- 返回值：返回 `dest` 的指针。
- 使用语句：`strncat(buffer, "World", 3);`
- 解释：将字符串 `"World"` 的前 3 个字符连接到 `buffer` 的末尾。

5. strcmp(str1, str2);

- 作用：比较字符串 `str1` 和 `str2`。
- 返回值：如果 `str1` 小于 `str2` 返回负数，如果相等返回 0，如果 `str1` 大于 `str2` 返回正数。
- 使用语句：`int result = strcmp("abc", "abd");`
- 解释：比较字符串 `"abc"` 和 `"abd"`，结果存储在 `result` 中。

6. strncmp(str1, str2, n);

- 作用：比较字符串 `str1` 和 `str2` 的前 `n` 个字符。
- 返回值：同 `strcmp`。
- 使用语句：`int result = strncmp("abc", "abd", 2);`
- 解释：比较字符串 `"abc"` 和 `"abd"` 的前 2 个字符，结果存储在 `result` 中。

7. strcasecmp(str1, str2);

- 作用：不区分大小写地比较字符串 `str1` 和 `str2`。
- 返回值：同 `strcmp`。
- 使用语句：`int result = strcasecmp("Hello", "hello");`
- 解释：不区分大小写地比较字符串 `"Hello"` 和 `"hello"`，结果存储在 `result` 中。

8. strncasecmp(str1, str2, n);

- 作用：不区分大小写地比较字符串 `str1` 和 `str2` 的前 `n` 个字符。
- 返回值：同 `strcmp`。
- 使用语句：`int result = strncasecmp("Hello", "help", 3);`
- 解释：不区分大小写地比较字符串 `"Hello"` 和 `"help"` 的前 3 个字符，结果存储在 `result` 中。

9. strchr(str, c);

- 作用：在字符串 `str` 中查找字符 `c` 的第一次出现。
- 返回值：返回指向字符 `c` 的指针，如果未找到则返回 NULL。
- 使用语句：`char *pos = strchr("example", 'e');`
- 解释：在字符串 `"example"` 中查找字符 `'e'` 的第一次出现，位置存储在 `pos` 中。

10. strrchr(str, c);

- 作用：在字符串 `str` 中查找字符 `c` 的最后一次出现。
- 返回值：同 `strchr`。
- 使用语句：`char *pos = strrchr("example", 'e');`
- 解释：在字符串 `"example"` 中查找字符 `'e'` 的最后一次出现，位置存储在 `pos` 中。

11. strstr(str1, str2);

- 作用：在字符串 `str1` 中查找子字符串 `str2` 的第一次出现。
- 返回值：返回指向子字符串 `str2` 的指针，如果未找到则返回 NULL。
- 使用语句：`char *pos = strstr("Hello World", "World");`
- 解释：在字符串 `"Hello World"` 中查找子字符串 `"World"` 的第一次出现，位置存储在 `pos` 中。
  以下是第 12 到第 17 个以 `str` 开头的函数的介绍、作用、返回值、使用语句和简单解释：

12. strtok(str, delim);

- 作用：将字符串 `str` 分解为一系列标记，`delim` 是分隔符字符串。
- 返回值：返回指向下一个标记的指针，如果没有更多标记则返回 NULL。
- 使用语句：`char *token = strtok(buffer, " ,");`
- 解释：在 `buffer` 中查找由空格或逗号分隔的下一个标记，并将其位置存储在 `token` 中。

13. strlen(str);

- 作用：计算字符串 `str` 的长度，不包括末尾的空字符 `\0`。
- 返回值：返回字符串 `str` 的长度，类型为 `size_t`。
- 使用语句：`size_t length = strlen("Hello World");`
- 解释：计算字符串 `"Hello World"` 的长度，并将结果赋值给 `length`。

14. strerror(errnum);

- 作用：根据错误编号 `errnum` 返回一个描述错误的字符串。
- 返回值：返回一个指向错误描述字符串的指针。
- 使用语句：`char *error = strerror(errno);`
- 解释：获取与 `errno` 相关的错误描述，并将其存储在 `error` 中。

15. strpbrk(str1, str2);

- 作用：在字符串 `str1` 中查找 `str2` 中任一字符的第一个位置。
- 返回值：返回指向 `str1` 中找到的第一个匹配字符的指针，如果没有找到则返回 NULL。
- 使用语句：`char *pos = strpbrk("hello", "aeiou");`
- 解释：在字符串 `"hello"` 中查找 `"aeiou"` 中任一字符的第一个位置，位置存储在 `pos` 中。

16. strcspn(str1, str2);

- 作用：在字符串 `str1` 中查找 `str2` 中任一字符的第一个位置之前的部分的长度。
- 返回值：返回 `str1` 中第一个匹配 `str2` 中任一字符的位置索引。
- 使用语句：`size_t length = strcspn("hello", "aeiou");`
- 解释：计算字符串 `"hello"` 中第一个出现 `"aeiou"` 中任一字符之前的字符数。

17. strspn(str1, str2);

- 作用：计算字符串 `str1` 开头连续包含 `str2` 中字符的长度。
- 返回值：返回 `str1` 开头连续包含 `str2` 中字符的长度。
- 使用语句：`size_t length = strspn("123abc", "1234567890");`
- 解释：计算字符串 `"123abc"` 开头连续包含 `"1234567890"` 中数字的长度。

## 基础的东西

**_为什么要用 do while 而不是直接加{}？_**
使用 `do { ... } while(0)` 而不是直接加 `{}` 来定义宏的原因有几个，主要是为了确保宏的使用更加安全和灵活：

1. **语句边界**：

   - 如果直接使用 `{}` 定义宏，那么宏展开后可能会破坏原有的代码结构，尤其是在宏需要作为条件语句（如 `if`、`while`、`for`）的一部分时。例如：
     ```c
     if (condition)
         MACRO(x, y);
     ```
     如果 `MACRO` 只是简单地用 `{ ... }` 定义，那么它可能会与 `if` 语句的语法冲突，导致编译错误。

2. **多条语句**：

   - 如果宏包含多条语句，直接使用 `{}` 可能会导致这些语句意外地成为更大的代码块的一部分，这可能会导致逻辑错误或编译错误。

3. **可预测性**：

   - `do { ... } while(0)` 结构确保宏总是作为一个单独的语句出现，无论它在哪里被使用。这意味着宏的使用不会影响周围的代码结构，提高了宏的可预测性和安全性。

4. **避免悬挂的 else 问题**：

   - 如果宏展开为多个语句，并且这些语句包括 `if` 条件，那么可能会遇到“悬挂的 else”问题。例如：
     ```c
     if (condition)
         MACRO(x, y);
     else
         do_something_else();
     ```
     如果 `MACRO` 包含多个语句，那么 `else` 可能会与宏内部的 `if` 而不是外部的 `if` 配对，导致逻辑错误。

5. **代码清晰**：
   - 使用 `do { ... } while(0)` 可以清楚地表明宏是一个单独的语句块，这有助于代码的可读性和维护。

综上所述，`do { ... } while(0)` 是一种常用的宏定义技巧，它确保宏在使用时总是作为一个单独的语句执行，避免了上述问题，并且使得宏的行为更加可预测和安全。

**_C 语言中，编译预处理后，所有的符号常量名和宏名都用相应的字符串替换。对吗？_**
这个说法不完全正确。在 C 语言中，编译预处理阶段确实会处理符号常量和宏，但它们并不是被替换为相应的字符串，而是被替换为它们所代表的值或定义的代码。

_宏定义不存在类型问题，宏名无类型，它的参数也无类型。对吗？_
是的，您的理解是正确的。在 C 语言中，宏定义和宏参数确实没有类型的概念：

1. **宏名无类型**：

   - 宏名仅仅是一个标识符，它在预处理阶段被替换为宏定义中指定的代码。宏名不涉及任何数据类型，它只是一个符号，用来指示预处理器在哪里进行文本替换。

2. **宏参数无类型**：
   - 宏参数在宏定义中出现时，它们是作为普通标识符处理的。预处理器在展开宏时，会将宏参数替换为它们在宏调用中对应的实际参数。这个替换过程不考虑参数的类型，它只是简单的文本替换。因此，宏参数没有类型，它们的类型是在宏展开后的代码中由编译器根据上下文确定的。

由于宏的这种无类型特性，使用宏时需要注意一些潜在的问题，比如类型安全和宏运算符的优先级问题。

**_C 语言程序中，在函数内定义的变量称为局部变量。对吗？_**
是的，您的理解是正确的。在 C 语言中，局部变量是指在函数内部定义的变量，它们只在定义它们的函数内部可见和可用。局部变量的作用域仅限于定义它们的函数或代码块中，这意味着它们在函数外部是不可见的，也无法被访问。

**_静态局部变量如果没有赋值，其存储单元中将是随机值。对吗？_**
不对，这个说法是错误的。在 C 语言中，静态局部变量（即在函数内部使用 `static` 关键字声明的变量）即使没有显式赋值，它们的存储单元中也不会是随机值。相反，静态局部变量会被自动初始化为零（对于基本数据类型）。这是 C 标准规定的。

这种初始化行为适用于所有静态存储期的变量，包括全局静态变量和静态局部变量。对于非基本数据类型（如结构体、联合体、数组等），如果它们不是指向自动初始化为零的类型，则需要显式初始化，否则它们的值是未定义的。

以下是一个例子：

```c
#include <stdio.h>

void function() {
    static int value;  // 没有显式初始化，将自动初始化为0
    printf("%d\n", value);  // 输出将为0
}

int main() {
    function();  // 输出0
    return 0;
}
```

在这个例子中，即使 `value` 没有被显式初始化，它也会被自动初始化为 0，因为 `value` 是一个静态局部变量。每次调用 `function` 时，`value` 的值都会保持不变，因为它具有静态存储期。如果 `value` 是一个非基本数据类型的静态局部变量，比如一个数组或结构体，那么它的内容将是未定义的，除非显式初始化。

**_C 语言中定义的静态变量存放在栈区，动态分配的内存空间位于堆区。对吗？_**
不对，这个说法是错误的。在 C 语言中，静态变量（包括全局静态变量和静态局部变量）并不存放在栈区，而是存放在静态存储区（也称为全局数据区）。静态存储区是程序内存中专门用于存储静态变量和全局变量的区域，这些变量在程序的整个运行期间都存在。

另一方面，动态分配的内存空间确实位于堆区。堆区是程序内存中用于动态分配和释放内存的区域。通过使用 malloc、calloc、realloc 等函数，程序可以在运行时申请和释放堆区的内存。

**_全局变量的作用域为其所在的整个文件范围。对吗？_**

**_全局变量必须在函数之外进行定义。对吗？_**
是的，您的理解是正确的。在 C 语言中，全局变量必须在函数之外进行定义，这意味着它们必须在任何函数定义之外的代码区域中声明和初始化。全局变量的作用域是整个源文件，它们可以被该文件中的任何函数访问和修改。

**_凡是函数中未指定存储类别的局部变量，其隐含的存储类型为( )。_**
自动类型(auto)

**_各种类型变量的生存期和作用域是什么?_**

### 自动变量（Automatic Variable）

- **生存期**：自动变量的生存期是局部的，仅在声明它的函数或代码块执行期间存在。当函数调用结束后，自动变量的存储空间会被释放。
- **作用域**：自动变量的作用域是局部的，仅在声明它的函数或代码块内部可见。不同函数中的自动变量是相互独立的，即使它们有相同的名称。

### 静态变量（Static Variable）

- **生存期**：静态变量的生存期是全局的，从声明时开始，直到程序结束。即使在声明它的函数或代码块执行结束后，静态变量仍然存在，其值不会丢失。
- **作用域**：静态变量的作用域是局部的，仅在声明它的函数或代码块内部可见。不同函数中的静态变量是相互独立的，即使它们有相同的名称。

### 外部变量（External Variable）

- **生存期**：外部变量的生存期是全局的，从声明时开始，直到程序结束。它们在整个程序的生命周期内都存在。
- **作用域**：外部变量的作用域是全局的，可以在多个文件或函数之间共享。如果在多个文件中声明了同一个外部变量（使用 `extern` 关键字），它们实际上指向同一个变量。

这些特性使得不同类型的变量适用于不同的编程场景。例如，自动变量适用于临时存储数据，静态变量适用于在函数调用之间保持状态，而外部变量适用于在多个模块之间共享数据。

**_编译,链接分别是干什么的?_**
编译（Compilation）和链接（Linking）是将源代码转换成可执行程序的两个关键步骤：

### 编译

- **作用**：将源代码文件转换成机器代码文件（通常是目标文件，如 `.o` 文件）。
- **过程**：
  - **预处理**：处理源代码中的宏定义、文件包含指令等。例如，展开 `#include` 指令，将包含的头文件内容插入到源文件中。
  - **语法分析**：检查源代码的语法是否正确，生成语法树。
  - **语义分析**：检查语法树中的语义是否正确，例如类型检查。
  - **优化**：对代码进行优化，以提高程序的执行效率。
  - **代码生成**：将优化后的代码转换成目标代码（机器代码）。

### 链接

- **作用**：将多个目标文件和库文件组合成一个可执行文件。
- **过程**：
  - **符号解析**：解析目标文件和库文件中的符号引用，确保每个符号都有一个唯一的定义。
  - **重定位**：调整目标文件中的代码和数据地址，使其在可执行文件中正确地定位。
  - **合并**：将多个目标文件和库文件中的代码和数据合并到一个可执行文件中。

### 举例说明

假设你有两个源文件 `file1.c` 和 `file2.c`，它们分别包含一些函数定义和调用。编译器会分别将这两个文件编译成目标文件 `file1.o` 和 `file2.o`。然后，链接器会将这两个目标文件链接起来，生成一个可执行文件 `a.out` 或其他指定的文件名。如果在链接过程中发现某个函数或变量在所有目标文件和库文件中都没有定义，就会报链接错误。

**_C 语言的全局变量的初始化是在哪个阶段完成的_**
全局变量的初始化是在程序开始执行之前完成的，即在 main() 函数开始之前。这是因为在程序启动时，操作系统会加载程序的可执行文件，并根据文件中的信息对全局变量进行初始化。这个过程是在程序的控制流进入 main() 函数之前完成的。

**_可执行文件是什么？_**
可执行文件（Executable File）是一个包含了机器代码的文件，它可以直接在计算机上运行。以下是关于可执行文件的一些关键点：

### 组成

- **机器代码**：可执行文件包含了编译后的机器代码，这是 CPU 可以直接执行的指令。
- **数据**：包括全局变量和静态变量的初始值。
- **元数据**：如程序的入口点（通常是 `main()` 函数的地址）、程序需要的动态库信息等。

### 加载和执行

- **加载**：当用户启动一个可执行文件时，操作系统会将其加载到内存中。这个过程包括分配内存、将机器代码和数据从文件复制到内存等。
- **执行**：加载完成后，操作系统会将控制权交给程序的入口点（通常是 `main()` 函数），程序开始执行。

### 示例

- **Windows**：用户可以双击 `.exe` 文件来运行程序。
- **Linux/macOS**：用户可以在终端中直接运行可执行文件，如 `./program`。

### 函数指针
```c
#include <stdio.h>
#include <math.h>
int main()
{
    double t1 , t2;
    double (*p)(double); //定义函数指针,传入double,输出double
    p=sin;
    p=(double (*)(double))sin; //强制转换:复制变量的定义,去掉变量
    t=sin(0.5);
    t2=(*p)sin(0.5);
    printf("%lf %lf",t1,t2);
}
```
*函数指针有什么用?*
- 一个数组,每个元素调用不同函数,可以创建函数指针的数组.
```c
struct node
{
    float data;
    float (*p)(float);
} a[20] ;
//使用时:(*(a[i].p))(a[i].data);
```
- 对不同函数进行相同操作,通过改变函数指针快速修改.
```c
//定义函数
double froot(int a,int b,double (*p)(double));
//调用
double t=froot(1,2,sin);
```
<br>