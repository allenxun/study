#include <iostream>
#include <assert.h>
#include "List.h"
  
using namespace std;
  
class SquareNode : public IListNode
{
public:
    SquareNode(int length) : x(length) {}
 
protected:
    bool process(void *param)
    {
        return cout << x * x << endl;
    }
 
private:
    int x;
};
 
class RoundNode : public IListNode
{
public:
    RoundNode(int radius) : r(radius) {}
 
protected:
    bool process(void *param)
    {
        return cout << 3.14 * r * r << endl;
    }
 
private:
    int r;
};
 
class RectangleNode : public IListNode
{
public:
    RectangleNode(int length, int width) : x(length), y(width) {}
 
protected:
    bool process(void *param)
    {
        return cout << x * y << endl;
    }
 
private:
    int x;
    int y;
};
  
bool ListNodeProcessor(IListNode *node, int index, void *param)
{
    cout << index << "->";
    return List::process(node, param);
}
  
void TestList()
{
    SquareNode square1(5), square2(7);
    RoundNode round1(4), round2(6);
    RectangleNode rect1(3, 7), rect2(4, 8);
    List list;
 
    assert(list.insert(List::Head, &square1));
    assert(!list.insert(List::Head, &square1)); 
    assert(list.remove(&square1));
    assert(!list.processAll(NULL));         
    assert(list.insert(List::Head, &square1));
    assert(list.insert(List::Tail, &round2));
    assert(list.processAll(NULL));
    assert(list.remove(&round2));
    assert(list.processAll(NULL));
    assert(list.insert(List::Head, &round2));
    assert(list.remove(&round2));
    assert(list.processAll(NULL));
    assert(!list.insertAt(-1, &round1));
    assert(!list.insertAt(list.count() + 1, &round1));
    assert(list.insertAt(1, &round1));
    assert(list.insertAt(1, &round2));
    assert(list.count() == 3)
    assert(list.processAll(NULL));
    for(int i = 0; i < list.count(); ++i)
        assert(List::process(list.at(i), NULL));
    assert(list.iterate(ListNodeProcessor, NULL));
    assert(!list.removeAt(-1));
    assert(!list.removeAt(list.count()));
    assert(list.removeAt(0));
    assert(list.count() == 2);
    assert(list.removeAt(list.count() - 1));
    assert(list.count() == 1);
    assert(!list.isEmpty());
    assert(list.clear());
    assert(list.isEmpty());
}
 
int main()
{
    TestList();
    return 0;
}

