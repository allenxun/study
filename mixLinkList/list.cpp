/****************
 *file List.cpp
 *author allen xun
 *version 1.0
 *date 2015.01.28
 ****************/
  
#include <assert.h>
#include <stddef.h>
#include "List.h"
  
class ListPrivate
{
public:
    ListPrivate() : _count(0) {}
 
    inline void incCount() {++_count;}
    inline void decCount() {--_count;}
    inline void rstCount() {_count = 0;}
    inline int count() const {return _count;}
 
    inline bool isValidIndex(int index)
    {
        return (index >= 0 && index < _count) ?
            true : false;
    }
 
private:
    int _count;
};
 
 
IListNode &IListNode::operator=(const IListNode &node)
{
    return *this;
}
 
IListNode::~IListNode()
{
    assert(!owner && !prev && !next);
}
  
List::List() : list(new ListPrivate), head(0), tail(0)
{
 
}
 
List::~List()
{
    (void)clear();
}
 
bool List::insert(Position pos, IListNode *node)
{
    bool retVal = false;
 
    if((pos == Head || pos == Tail) && prepare(node))
    {
        if(!head && !tail)
            head = tail = node;
        else
        {
            assert(head && tail);
 
            switch(pos)
            {
            case Head:
                head->prev = node;
                node->next = head;
                head = node;
                break;
            case Tail:
                tail->next = node;
                node->prev = tail;
                tail = node;
                break;
            default:
                assert(0);
            }
        }
  
        list->incCount();
        retVal = true;
    }
 
    return retVal;
}
 
bool List::insertAt(int index, IListNode *node)
{
    bool retVal = false;
 
    if(index == 0)
        retVal = insert(Head, node);
    else if(index == list->count())
        retVal = insert(Tail, node);
    else
    {
        assert(head && tail);
 
        IListNode *prevNode = at(index - 1);
 
        if(prevNode && prepare(node))
        {
            node->next = prevNode->next;
            node->prev = prevNode;
 
            assert(prevNode->next);
 
            prevNode->next->prev = node;
            prevNode->next = node;
 
            list->incCount();
            retVal = true;
        }
    }
 
    return retVal;
}
 
bool List::remove(IListNode *node)
{
    bool retVal = false;
 
    if(hasNode(node))
    {
        if(head == node)
            head = node->next;
        if(tail == node)
            tail = node->prev;
 
        if(node->next)
            node->next->prev = node->prev;
        if(node->prev)
            node->prev->next = node->next;
 
        (void)isolate(node);
 
        list->decCount();
        retVal = true;
    }
 
    return retVal;
}
 
bool List::removeAt(int index)
{
   return remove(at(index));
}
  
bool List::iterate(callback func, void *param)
{
    bool retVal = false;
 
    if(func && head && tail)
    {
        IListNode *iterator = head;
 
        {
            IListNode *tempPtr = NULL;
            int index = 0;
 
            do
                tempPtr = iterator->next;  
            while(func(iterator, index++, param) && (iterator = tempPtr));
        }
 
        if(!iterator) retVal = true;
    }
 
    return retVal;
}
  
bool List::clear()
{
    bool retVal = false;
 
    if(list->count() && (retVal = iterate(isolateCallback, this)))
    {
        list->rstCount(); 
        head = 0;
        tail = 0;
    }
 
    return retVal;
}
 
bool List::processAll(void *param) const
{
    bool retVal = false;
 
    if(head && tail)
    {
        IListNode *iterator = head;
 
        while(iterator->process(param) && (iterator = iterator->next));
        if(!iterator) retVal = true;
    }
 
    return retVal;
}
 
bool List::contains(const IListNode *node) const
{
    return hasNode(node);
}
  
bool List::isEmpty() const
{
    return !list->count();
}

int List::count() const
{
    return list->count();
}
 
IListNode *List::at(int index) const
{
    IListNode *retVal = NULL;
 
    if(list->isValidIndex(index))
    {
        IListNode *iterator = head;
        for(;index && (iterator = iterator->next); --index);
  
        if(!index) retVal = iterator;
    }
 
    return retVal;
}
 
bool List::process(IListNode *node, void *param)
{
    return node ? node->process(param) : false;
}
 
bool List::isolate(IListNode *node) const
{
    if(hasNode(node))
    {
        node->owner = NULL;
        node->prev = NULL;
        node->next = NULL;
  
        return true;
    }
    else
        return false;
}
  
bool List::prepare(IListNode *node) const
{
    if(noOwner(node))
    {
        node->owner = const_cast<List *>(this);
        node->prev = NULL;
        node->next = NULL;
  
        return true;
    }
    else
        return false;
}
  
bool List::hasNode(const IListNode *node) const
{
    return node ? node->owner == this : false;
}
  
bool List::noOwner(const IListNode *node) const
{
    return node ? !node->owner : false;
}
  
bool List::isolateCallback(IListNode *node, int index, void *param)
{
    List *self = (List *)param;
 
    return self ? self->isolate(node) : false;
}
