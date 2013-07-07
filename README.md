> WeiboUnfoTool helps you analyze and filter people who you may wanna unfollow out

##Structure

- MVC: templates+views+controllers+models

##Based-on

- [Flask](https://github.com/mitsuhiko/flask)
- Sina Weibo Python SDK: [sinaweibopy](https://github.com/michaelliao/sinaweibopy)

##Design

###Brief

每次给出20个可能的需要Unfo的关注者。

###Strategy

一般用户Following的人不会超过2000，基数不大。从中提出两类用户，一种是Unfo的（推荐需要取关的），一种是Fo的（不大可能想取关的）。然后过滤出来的就是"Unfo的或非Fo的"。

#### Unfo ####

- 垃圾号
    
    - 最后一次发博时间>1 year
    - 关注数>1500 且 粉丝数<500
    - 微博数<5
    - 个人资料不完整（无头像、无标签等。。）

- 不敢兴趣
    
    - 无共同好友（这里对好友的判定要斟酌，**好友=互粉** or **好友=有除了加V用户之外的共同关注**）
    - 无备注
    - 无分组
    - 无共同标签

#### Fo ####

- 互粉
- 共同好友数 > N （同需注意好友判定）

###其他

1. 用户自定义策略（e.g. 标签关键词过滤）
1. 应用提供类别选择（e.g. 程序猿、娱乐明星等）
1. **话说那个"微博推荐"接口只针对还没Fo的人吧？不然就方便了**

##Sina Weibo API (May) Used

###Read

- friendships/friends （关注列表）
- friendships/friends/ids   
- friendships/friends/bilateral （互粉）
- friendships/friends/bilateral/ids 
- friendships/friends/in_common （共同关注）
- users/show （用户信息）
- users/counts （批量获取用户的粉丝数、关注数、微博数）
- tags/tags_batch   （返回指定用户的标签列表）
- friendships/groups （好友分组，高权限接口，暂缓。。）
- friendships/friends/remark_batch  （关注人的备注信息，高权限接口，暂缓。。）

###Write

- friendships/destroy   （取关）
- friendships/create  （关注）

##TODO

- Filter Design Pattern?
- 实现初步的策略，推出20的人。
- 20个人之后，涉及到下一组人，用数据库`维护`会话还是用什么Storage？


