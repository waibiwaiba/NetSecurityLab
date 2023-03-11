#include <stdio.h>

// 将一个 64 位数转化为对应的二进制字符串
void to_binary_string_64(unsigned long long n, char *str) {
  int i;
  for (i = 63; i >= 0; i--) {
    str[i] = (n & 1) + '0'; // 取出最后一位并转化为字符
    n >>= 1; // 右移一位，继续处理下一位
  }
  str[64] = '\0'; // 在末尾添加结束符
}

// 将一个 32 位整数转换为对应的二进制字符串
void to_binary_string_32(int n, char *str) {
    int i;
    for (i = 31; i >= 0; i--) {
        str[i] = (n & 1) + '0';  // 取出最后一位并转化为字符
        n >>= 1;  // 右移一位，继续处理下一位
    }
    str[32] = '\0';  // 在末尾添加结束符
}

int binary_to_int(const char *binary_str) {
    int result = 0;
    const char *p = binary_str;
    while (*p) {
        result <<= 1;  // 将 result 左移一位，为下一位预留位置
        if (*p == '1') {
            result |= 1;  // 将最后一位设置为 1
        }
        p++;
    }
    return result;
}

void print_pointer_address(void *p) {
    unsigned long long address = (unsigned long long)p;  // 将指针地址转换为 unsigned long long 类型
    printf("指针地址：%016llx\n", address);  // 打印指针地址的16进制表示，总共16个字符宽度，左侧填充0

}

void print_hex_str(char hex_str[]) {
    int i = 0;
    while (hex_str[i] != '\0') {
        printf("%c   ", hex_str[i]);
        i++;
    }
}

int main() {
  int a = 10;
  int *p = &a;  // 定义一个指向 a 的指针变量
  int **pp = &p;  // 定义一个指向指针 p 的指针变量
  printf("%%d, p  的结果是：%d\n", p);
  printf("%%d, **p的结果是：%d\n", *pp);
  unsigned long long address = (unsigned long long)p;
  char binary_str_64[65]; // 64 位二进制字符串需要 65 个字符，最后一位是结束符 '\0'
  to_binary_string_64(address, binary_str_64);
  printf("p 指向的地址的64二进制字符串：\n%s\n", binary_str_64);
  int result = binary_to_int(binary_str_64);
  printf("将上面的二进制字符串转化为int类型的整数：\n%28d\n", result);
  int x = *p;  // 将指针 p 的地址的值存储在 x 中
  printf("%%d, *p 的结果是：%d\n", x);  // 打印 x 的值
  char binary_str_32[33];
  to_binary_string_32(x, binary_str_32);
  
  printf("%%d, *p 对应的32位二进制字符串：\n%s\n", binary_str_32);
//   printf("p  的地址：%p\n", (void*)&p);   // 输出 p 的地址
  
  print_pointer_address((void *)&p);
  char hex_str[20];  // 定义一个字符数组用于存储16进制串
  sprintf(hex_str, "%p", (void*)&p);  // 将地址的16进制形式保存到字符数组中
  printf("hex_str: \n");
  print_hex_str(hex_str);
  printf("\n");
  printf("pp 的地址：%p\n", (void*)&pp);  // 输出 pp 的地址
  printf("%d\n", *p);
  printf("%d\n", **pp);  // 输出 p 所指向的值
  return 0;
}