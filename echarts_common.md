## 内容
### 饼图
data
### 直方图
#### data
x轴： 类目轴  
y轴： 数值轴  
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
一个最简单的直方图
如果我们有二维数据呢，上面讲述的是销量，那么我们可能会将连续两年的销量做对比, 那么我们需要在series(系列)中再加入一组数据
```js
            {
                name: '销量',
                type: 'bar',
                data: [8, 24, 43, 15, 15, 25]
            }
```
##### 加上一个系列的数据之后图例变没了
在echarts中图例是用legend表示的，但是value是不能随便指定的，必须和series中的对应系列的name相同

##### 想要看到精确的提示数据，但是又不想把数据展示在图表上？
如果我们想要精确的看到数据，可以使用tooltip选项，tooltip选项可以直接写{} echarts会自动给定默认值，我们也可以自己配置：
    tooltip:{
        trigger: "item",
        formatter: "{a}<br/>{b}: {c}"
    }
##### 如果再想加入2016， 2017， 2018 数据呢，当然我们可以将数据罗列在series中，并且legend也要增加， Echarts4.0提供了一个更加先进的方式

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
##### 现在我们又不想竖着看，我们想横着看
dataset中的行列可以随意配置，具体配置参数seriesLayoutBy，只需要将每一个系列的serieslayoutBy值设置为row(默认为column):
```js
series: [
        {type: 'bar', seriesLayoutBy: 'row'},
        {type: 'bar', seriesLayoutBy: 'row'},
        {type: 'bar', seriesLayoutBy: 'row'},
        {type: 'bar', seriesLayoutBy: 'row'}
    ]
```


