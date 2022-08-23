# issue-bot-tongli

构建一个利用 issue 进行查看东立漫画信息的 bot。

p.s.本项目的诞生不是因为东立书城的APP卡爆了 XD

東立電子書城： https://ebook.tongli.com.tw/

## 如何使用

### 查询漫画信息

从[此页面](https://github.com/1299172402/issue-bot-tongli/issues/new?assignees=&labels=search&template=search.md&title=%5BSearch%5D)发送要查询的内容，稍等片刻即可自动收到回复

示例：[[Search] #26](https://github.com/1299172402/issue-bot-tongli/issues/26) 

可以查看封面、名称、作者、评分、简介等信息

### 获取漫画

进入[此页面](https://github.com/1299172402/issue-bot-tongli/issues/new?assignees=&labels=Runner&template=runner.md&title=%5BRunner%5D+)，填写以下内容，值均区分大小写。

其中 bookid 和 isSerial 的信息可以从查询漫画中显示的**其他信息**栏目获取

| 名称         | 值                   | 说明                                             |
| ------------ | -------------------- | ------------------------------------------------ |
| type         | `NEW` 或者 `ALL`     | - NEW 获取最新集数<br />- ALL 获取全部集数       |
| bookid       |                      | 形如 42a8cecb-ea43-kw32-5cs3-08da6013d2f6 的文本 |
| isSerial     | `true` 或者 `false ` | - true 连载中的漫画<br />- false 单行本的漫画    |
| RefreshToken |                      | 保存到阿里云盘所需要的token<br />默认是 `None`   |

若要将获取到的内容存在阿里云盘内，则填写RefreshToken，在工作流完成后请注意删除RefreshToken或者退出网盘，**防止token被盗用**。

亦可以通过 artifacts 的 URL 获取。

示例：[[Runner] #32](https://github.com/1299172402/issue-bot-tongli/issues/32) 

## 后记

其实个人觉得这个项目做成 Telegram bot 可能实用性更好一些，能更直观追自己喜欢的漫画。可惜本人不太懂 TG 的 API，也没有相关的开发经验，希望以后能有人做出来。

