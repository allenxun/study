/*******************************
 *Author:allen xun
 *Time:2015.1.16
 *File:DoubleList.c
 *Version:0.1.0
 * *****************************/
#include"DoubleList.h"
#include<stdio.h>
void myPrint(Item i)
{
	printf("%d \n",i);
}
int main()
{
	DoubleList *plist = NULL;
	PNode p = NULL;
	
	plist = InitList();
	p = InsFirst(plist,MakeNode(1));
	InsBefore(plist,p,MakeNode(2));
	InsAfter(plist,p,MakeNode(3));

	printf("p前驱位置的值为%d\n",GetItem(GetPrevious(p)));
	printf("p位置的值为%d\n",GetItem(p));
	printf("p后继位置的值为%d\n",GetItem(GetNext(p)));
	
	printf("遍历输出各节点数据项:\n");
	ListTraverse(plist,myPrint);
	printf("除了头节点该链表共有%d个节点\n",GetSize(plist));
	FreeNode(DelFirst(plist));
	printf("删除第一个节点后重新遍历输出为:\n");
	ListTraverse(plist,myPrint);
	printf("除了头节点该链表共有%d个节点\n",GetSize(plist));
	DestroyList(plist);
	printf("链表已被销毁\n");
	return 0;
}
