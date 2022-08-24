# issue-bot-tongli

构建一个利用 issue 进行查看东立漫画信息的 bot

p.s. 本项目的诞生不是因为东立书城的APP太容易卡了XD

東立電子書城： https://ebook.tongli.com.tw/

## 如何使用

转到 Issue 新建页

<img src="https://user-images.githubusercontent.com/29673994/186096473-d9160369-cd55-4596-8570-6a65b857ed1f.png" height="80%" width="80%" >

### 查询漫画信息

使用 Search 的 Issue 模板[创建](https://github.com/1299172402/issue-bot-tongli/issues/new?assignees=&labels=search&template=search.md&title=%5BSearch%5D)，内容填写要查询的关键词，稍等片刻即可自动收到回复

示例：[[Search] #26](https://github.com/1299172402/issue-bot-tongli/issues/26) 

可以查看封面、名称、作者、评分、简介等信息

<img src="https://user-images.githubusercontent.com/29673994/186094462-c855c41a-a812-450d-a07a-4068f80b934d.png" height="80%" width="80%" >

### 获取漫画

使用 Runner 的 Issue 模板[创建](https://github.com/1299172402/issue-bot-tongli/issues/new?assignees=&labels=Runner&template=runner.md&title=%5BRunner%5D+)，填写以下内容，值均**区分大小写**。

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

<img src="https://user-images.githubusercontent.com/29673994/186094521-c6a425ff-9998-4729-af22-94eaa1b51d24.png" height="80%" width="80%" >

### 删除 issue

含有 Search 和 Runner 标记的 issue 一旦被关闭，就会自动删除此 issue 

## 后记

其实个人觉得这个项目做成 Telegram bot 可能实用性更好一些，能更直观追自己喜欢的漫画。只可惜本人不太懂 TG 的 API，也没有相关的开发经验。。。

