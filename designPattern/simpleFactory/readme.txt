简单工厂模式的优点在于把对象的创建和使用分开。对象的创建只和工厂有关，与消费者无关。
缺点在于新增加一种对象类型（类），就要修改工厂方法，令其能产生新类的对象。这违背“开发-封闭”原则（开放扩展，封闭修改）。

实现时：
1. 最常见的，用switch/case，传入工厂一个字符串，然后，工厂判断一下（switch/case），输出这个字符串代表的类。
2. 如何把字符串和类相关联？用switch太傻了，因为在增加类时，要去修改简单工厂类。所以可以改进。
3. 可以利用语言的特性来关联字符串和类。比如Java，用反射,Class.ForName("类名")，比如Python，_dict_["类名"]，可以取到这个类，然后用这个类来实例化。
4. 进一步地，可以利用配置文件。

fruitFactory: show the reflect in python with __import__ & re module.
printMode: return a function instead of instance with getattr.