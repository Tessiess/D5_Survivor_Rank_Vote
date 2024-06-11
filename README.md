# D5_Survivor_Rank_Vote

第五人格 求生者强度投票箱

**更新1.0.0版** 大众强度榜来啦！

由于之前某up的强度评级引发了大众的争论，于是本人借鉴了隔壁游戏的比较思路，看看大众眼中的强度如何

前端JS，后端Python Flask，数据全部来自网友投票，仅供娱乐，准确度可能很低，求轻喷。有好点子欢迎直接提issue或者Pull requests！

## 直接访问：求生者强度投票箱 [http://150.158.55.168:5555](http://150.158.55.168:5555)

运行正常时，界面如下图所示：

<img src="images\frontend.png" alt="frontend" width="1000px">

## 在本地电脑上部署

1. Clone 本项目

   `git clone --depth=1 https://github.com/Tessiess/D5_Survivor_Rank_Vote.git`

1. 搭建环境：

   ```powershell
   cd .\D5_Survivor_Rank_Vote\
   # 创建虚拟环境
   python -m venv venv
   # 激活该环境
   .\venv\Scripts\activate
   # (可选) 更新 pip
   python -m pip install -U pip
   # 安装依赖
   pip install -r requirements.txt
   ```

1. 运行应用：

   `flask --app backend.py run --debug --host=0.0.0.0 --port 5555`

1. 用浏览器打开 [`127.0.0.1:5555`](http://127.0.0.1:5555)

## 计分规则

如图所示，从所有求生者中，随机抽取两位，供用户投票强弱。你可以点击你认为较强的求生者，为其投票。

每次投票，得票的求生者+1分，未得票的求生者-1分。当投票次数足够多时，可以认为所有求生者之间都得到了较充分的比较。

如果你认为两位求生者实力不相上下，可以点击 **跳过，换一组** 按钮，感谢你认真、负责地进行求生者评价！

最后，程序将统计所有求生者的胜率和得分，以胜率排名。(为避免恶意刷票，每个ip只能投30票，自第31票起，每票按0.01票计算权重。)

## 结果展示

每次的投票结果数据，投票后将立刻写入服务端电脑，存储为pickle文件。

点击 **查看总投票结果** 按钮，将根据现有全部数据和上述规则，实时生成排行榜。

点击 **查看您的投票结果** 按钮，将根据用户单人的投票数据，实时生成排行榜。其不受50票限制，但数据将在网页刷新/关闭时**清零**。

特别要注意的是，当数据量很少时，由于随机抽取轮到每位求生者的次数不等，且较小群体的主观认知偏见较大，此时生成的排名结果质量很差，谬误甚多，完全不能反映求生者的真实水平。

即使数据量较大，此种排名也并不精确，最终结果受随机分组的影响较大。因此，建议无需过分关注具体排名，而是来了解求生者的大致水平。此外，也提供对胜率接近的求生者进行的聚类分块，帮助衡量求生者的相对强弱。

## 作者

[@Tessiess](https://github.com/Tessiess):只会调用以下大佬们的代码qwq，如果对项目有不满可以攻击我，不要攻击下面的大佬

[@SYadda(董杭杭)](https://github.com/SYadda)：前端和后端整体框架设计

[@blackwang08](https://github.com/blackwang08)：前端网页美化

[@lengyanyu258](https://github.com/lengyanyu258)：前端网页美化，排行聚类分块算法

[@lpdink](https://github.com/lpdink)：前端 展示自己的投票结果

## 版权及鸣谢

鸣谢：本投票两两比较的灵感来源于隔壁游戏，图片来自于第五人格官网(为啥图片不一样大qwq)，大部分代码来自于引用项目，特别鸣谢他们详细的代码注释！

本程序内使用的游戏图片、文本等信息，其版权属于 网易第五人格joker工作室。
