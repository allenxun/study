/**********************
 *file List.h
 *author allen
 *version 1.0
 *date 2015/01/28
 ***********************/
  
#ifndef LIST
#define LIST
 
class IListNode;
class List;
class ListPrivate;
 
typedef bool (*callback)(IListNode *, int index, void * param);
 
class IListNode
{
    friend class List;
  
 public:
     IListNode(): owner(0), prev(0), next(0) {}
     IListNode(const IListNode &node): owner(0), prev(0), next(0) {}
     IListNode &operator=(const IListNode &node);
     virtual ~IListNode(); //! Îö¹¹º¯Êý
  
 protected:
     virtual bool process(void *param) = 0;
  
 private:
     List *owner;
     IListNode *prev;
     IListNode *next;
 };
  
 class List
 {
 public:
     enum Position
     {
         Head,  
         Tail  
     };
  
     List();
     ~List();
  
     bool insert(Position pos, IListNode *node);
  
     bool insertAt(int index, IListNode *node);
  
     bool remove(IListNode *node);
  
     bool removeAt(int index);
  
     bool iterate(callback func, void *param);
     
	 bool processAll(void *param) const;
  
     bool clear();
  
     bool contains(const IListNode *node) const;
  
     bool isEmpty() const;
  
     int count() const;
  
     IListNode * at(int index) const;
  
 public:
     static bool process(IListNode *node, void *param);
  
 private:
     ListPrivate *list;
     IListNode *head;
     IListNode *tail;
  
 private:
     List(const List &list);
     List &operator=(const List &list);
  
 private:
     bool isolate(IListNode *node) const;
     bool prepare(IListNode *node) const;
     bool hasNode(const IListNode *node) const;
     bool noOwner(const IListNode *node) const;
  
 private:
     static bool isolateCallback(IListNode *node, int index, void *param);
 };
  
 #endif
