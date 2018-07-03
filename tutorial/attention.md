### 注意事项
#### 不要忘记写逗号，不要忘记写逗号，不要忘记写逗号
在调试echarts的时候前端经常会报Uncaught SyntaxError: Unexpected token 的error是因为option中某一个list项和项之间没有逗号<br>
echarts对格式要求比较严格
#### 注意格式转换
在html文件中script部分也可以引用jinja模版里面的变量， 但是如果传过来的是结构化数据，那么js会自动加上转义，使结构化的数据不能按结构解析
所以解决办法是： {{ data|safe }} 或者是{{ data|tojson }}
