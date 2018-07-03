### 直方图
#### data
一般情况下
x轴： 类目轴<br>  
y轴： 数值轴<br>
legend：图例<br>
title: 表名称<br>
series:数据系列<br>
废话不多说，先上代码和图示
Echarts4.0之前的数据格式
```js
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>ECharts</title>
    <!-- 引入 echarts.js -->
    <script src="echarts.min.js"></script>
</head>
<body>
    <!-- 为ECharts准备一个具备大小（宽高）的Dom -->
    <div id="main" style="width: 600px;height:400px;"></div>
    <script type="text/javascript">
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('main'));
        // 指定图表的配置项和数据
        var option = {
            title: {
                text: 'ECharts 入门示例'
            },
            //tooltip: {},
            legend: {
                data:['销量']
            },
            xAxis: {
                data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
            },
            yAxis: {},
            series: [{
                name: '销量',
                type: 'bar',
                data: [5, 20, 36, 10, 10, 20]
            }]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
    </script>
</body>
</html>
```
上面展示的是一个最简单的直方图<br>
在html中首先必须得有一个dom元素来存放我们的图表，这个dom元素必须得指定表格的宽高，否则不显示图表<br>
大家可以看到一些基本的元素都在上面，比如title, legend(也可以不指定)， Xaxis, Yaxis, series<br> 
##### 如果我们有二维数据呢，上面讲述的是销量，那么我们可能会将连续两年的销量做对比, 那么我们需要在series(系列)中再加入一组数据
```js
            {
                name: '销量',
                type: 'bar',
                data: [8, 24, 43, 15, 15, 25]
            }
```
##### 加上一个系列的数据之后图例变没了
在echarts中图例是用legend表示的，但是对应的值是不能随便指定的，必须和series中的对应系列的name相同

##### 想要看到精确的提示数据，但是又不想把数据展示在图表上？
如果我们想要精确的看到数据，可以使用tooltip选项，tooltip选项可以直接写{} echarts会自动给定默认值，我们也可以自己配置：
    tooltip:{
        trigger: "item",
        formatter: "{a}<br/>{b}: {c}"
    }
##### 如果再想加入2016， 2017， 2018 数据呢，当然我们可以将数据罗列在series中，并且legend也要增加， Echarts4.0提供了一个更加先进的方式

#### dataset

优点：
   很多配置项不用专门配置就可以自动生成(legend tooltips)<br>
   数据可以被复用<br>
   不用为了规定的数据格式进行转化<br>  
默认情况下，x轴会对应到dataset的第一列，每个维度的数据会对应dataset中的除第一列的每一列<br>  
数据格式： 二维数组、key-value（key-value并不支持seriesLayoutBy）<br>

        
```js
option = {
    legend: {},
    tooltip: {},
    dataset: {
        // 提供一份数据。
        source: [
            ['product', '2015销量', '2016销量', '2017销量', '2018销量'],
            ['衬衫', 43, 85, 93, 99],
            ['羊毛衫', 83, 73, 55, 67],
            ['雪纺衫', 86, 65, 82, 98],
            ['裤子', 72, 53, 39, 33],
            ['高跟鞋', 27, 45, 46, 56],
            ['袜子', 78, 63, 79, 45]
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
        {type: 'bar'},
        {type: 'bar'}
    ]
}
```
可以看出来我们的series中少了name的配置和在legend中的配置，echarts会根据dataset中第一行识别legend,第一列识别x轴type
##### 现在我们又不想让数据按列展示，我们想将数据按行展示
dataset中的行列可以随意配置，具体配置参数seriesLayoutBy，只需要将每一个系列的serieslayoutBy值设置为row(默认为column):
```js
series: [
        {type: 'bar', seriesLayoutBy: 'row'},
        {type: 'bar', seriesLayoutBy: 'row'},
        {type: 'bar', seriesLayoutBy: 'row'},
        {type: 'bar', seriesLayoutBy: 'row'}，
        {type: 'bar', seriesLayoutBy: 'row'}，
        {type: 'bar', seriesLayoutBy: 'row'}
    ]
```
##### 如果想在一个页面上展示一个既按行展示又按列展示的
```js
xAxis: [{type: 'category', gridIndex: 0},
            {type: 'category', gridIndex: 1}],
            
    // 声明一个 Y 轴，数值轴。
    yAxis: [{gridIndex: 0},
            {gridIndex: 1}],
    grid: [
        {bottom: '55%'},
        {top: '55%'}
    ],
    // 声明多个 bar 系列，默认情况下，每个系列会自动对应到 dataset 的每一列。
    series: [
        {type: 'bar', seriesLayoutBy: 'row'},
        {type: 'bar', seriesLayoutBy: 'row'},
        {type: 'bar', seriesLayoutBy: 'row'},
        {type: 'bar', seriesLayoutBy: 'row'},
        {type: 'bar', seriesLayoutBy: 'row'},
        {type: 'bar', seriesLayoutBy: 'row'},
        {type: 'bar', xAxisIndex: 1, yAxisIndex: 1},
        {type: 'bar', xAxisIndex: 1, yAxisIndex: 1},
        {type: 'bar', xAxisIndex: 1, yAxisIndex: 1},
        {type: 'bar', xAxisIndex: 1, yAxisIndex: 1},
   
    ]
```
##### dataset不仅支持x轴展示category，而且支持y轴展示category

```js
xAxis: [{gridIndex: 0},
            {gridIndex: 1}],
            
    // 声明一个 Y 轴，数值轴。
    yAxis: [{gridIndex: 0, type: 'category'},
            {gridIndex: 1, type: 'category'}],
```

### dimension和encode
#### dimension(维度)
上面的例子中如果series是按行展示的，则维度名是第一行（销量），如果是按列展示，则维度名是第二行（衣服类别）
维度名和维度类型也可以自己指定，在dataset中加入一个dimension的选项，设置type值和name,不过一般情况下是不会用dimension设置维度名和type
#### encode(数据到图形的映射)
```js
option = {
    dataset: {
        source: [
            ['score', 'amount', 'product'],
            [89.3, 58212, 'Matcha Latte'],
            [57.1, 78254, 'Milk Tea'],
            [74.4, 41032, 'Cheese Cocoa'],
            [50.1, 12755, 'Cheese Brownie'],
            [89.7, 20145, 'Matcha Cocoa'],
            [68.1, 79146, 'Tea'],
            [19.6, 91852, 'Orange Juice'],
            [10.6, 101852, 'Lemon Juice'],
            [32.7, 20112, 'Walnut Brownie']
        ]
    },
    xAxis: {type: 'category'},
    yAxis: {},
    series: [
        {
            type: 'bar',
            encode: {
                // 将 "amount" 列映射到 X 轴。
                x: 'product',
                // 将 "product" 列映射到 Y 轴。
                y: 'amount'
            }
        }
    ]
};
```
如果想让x轴和y轴互换，只需要将x轴和y轴的数据映射(encode)互换，然后将类目轴设置为y<br>
#### 问题 seriesByLayout和encode各适用于什么场景？


      
