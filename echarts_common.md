## 内容
### 饼图
data
### 直方图
#### data
x轴： 类目轴  
y轴： 数值轴  
#### dataset

优点：
   很多配置项不用专门配置就可以自动生成(legend tooltips)  
   数据可以被复用  
   不用为了规定的数据格式进行转化  
一般情况下，x轴会对应到dataset的第一列，每个系列会对应dataset中的每一列  
数据格式： 二维数组、key-value,key-value并不支持seriesLayoutBy
        
```js
option = {
    legend: {},
    tooltip: {},
    dataset: {
        // 提供一份数据。
        source: [
            ['product', '2015', '2016', '2017'],
            ['Matcha Latte', 43.3, 85.8, 93.7],
            ['Milk Tea', 83.1, 73.4, 55.1],
            ['Cheese Cocoa', 86.4, 65.2, 82.5],
            ['Walnut Brownie', 72.4, 53.9, 39.1]
        ]
    },
    // 声明一个 X 轴，类目轴（category）。默认情况下，类目轴对应到 dataset 第一列。
    xAxis: {type: 'category'},
    // 声明一个 Y 轴，数值轴。
    yAxis: {},
    // 声明多个 bar 系列，默认情况下，每个系列会自动对应到 dataset 的每一列。
    series: [
        {type: 'bar'},
        {type: 'bar'},
        {type: 'bar'}
    ]
}
```

dataset中的行列可以随意配置，具体配置参数seriesLayoutBy
