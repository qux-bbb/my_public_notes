#include<stdio.h>
#include "md5.h"

int main(int argc, char* argv[])
{
	char a[] = "hello";

	printf("%s\n", md5(a));

	return 0;
}