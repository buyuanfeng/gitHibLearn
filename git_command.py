$ mkdir learngit
$ cd learngit
$ pwd
#通过git init命令把这个目录变成Git可以管理的仓库
$ git init
#git status命令可以让我们时刻掌握仓库当前的状态
$ git status
#git diff能看看具体修改了什么内容
$ git diff readme.txt 
#提交修改和提交新文件是一样的两步，第一步是git add
$ git add readme.txt
#第二步git commit
$ git commit -m "add distributed"
#版本控制系统肯定有某个命令可以告诉我们历史记录，在Git中，我们用git log命令查看
$ git log
$ git log --pretty=oneline
#回退版本Git必须知道当前版本是哪个版本，用HEAD表示当前版本，上一个版本就是HEAD^，
#上上一个版本就是HEAD^^，当然往上100个版本写100个^比较容易数不过来，所以写成HEAD~100。
$ git reset --hard HEAD^
#回退到指定版本
$ git reset --hard 3628164
#Git提供了一个命令git reflog用来记录你的每一次命令
