# HashMap和HashTable和ConcurrentHashMap

**HashMap**：普通的Map，不能有重复的键  
**HashTable**：具有线程安全特点，在操作时会对整张表加锁  
**ConcurrentHashMap**：具有线程安全特点，在操作时会对被操作元素加锁，比HashTable效率更高，因为可以同时更改一个Hash表不同的segment(段)


2017/9/15  
