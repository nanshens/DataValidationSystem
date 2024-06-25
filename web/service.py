# todo 1. 定义表结构
# todo 1. crud 表结构
# todo 1. 定义枚举
# todo 1. controller 和service
# todo 添加验证策略 curd
# todo 为策略添加subject 和column 和rule, 修复rule
# todo: 执行策略 记录log
# todo: 生成结果 自动修改, 生成对比文件
# todo  查看历史结果
# todo: 导入文件有备份

new_user = User(username=data['username'], email=data['email'])
db.session.add(new_user)
db.session.commit()

user = User.query.get(user_id)

user = User.query.get(user_id)
if user:
    data = request.get_json()
    user.username = data['username']
    user.email = data['email']
    db.session.commit()

