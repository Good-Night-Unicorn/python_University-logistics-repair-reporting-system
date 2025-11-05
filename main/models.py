#coding:utf-8
from django.db import models

from .model import BaseModel

from datetime import datetime



class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='zhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='zhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    zhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='账号' )
    xingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='姓名' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    '''
    zhanghao=VARCHAR
    xingming=VARCHAR
    mima=VARCHAR
    xingbie=VARCHAR
    shouji=VARCHAR
    touxiang=Text
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'
class weixiurenyuan(BaseModel):
    __doc__ = u'''weixiurenyuan'''
    __tablename__ = 'weixiurenyuan'

    __loginUser__='weixiuzhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='weixiuzhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    weixiuzhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='维修账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    weixiuxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='维修姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    lianxifangshi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系方式' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    '''
    weixiuzhanghao=VARCHAR
    mima=VARCHAR
    weixiuxingming=VARCHAR
    xingbie=VARCHAR
    lianxifangshi=VARCHAR
    touxiang=Text
    '''
    class Meta:
        db_table = 'weixiurenyuan'
        verbose_name = verbose_name_plural = '维修人员'
class shenpiyuan(BaseModel):
    __doc__ = u'''shenpiyuan'''
    __tablename__ = 'shenpiyuan'

    __loginUser__='shenpizhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='shenpizhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shenpizhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='审批账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    shenpixingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='审批姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    lianxishouji=models.CharField ( max_length=255,null=False, unique=False, verbose_name='联系手机' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    '''
    shenpizhanghao=VARCHAR
    mima=VARCHAR
    shenpixingming=VARCHAR
    xingbie=VARCHAR
    lianxishouji=VARCHAR
    touxiang=Text
    '''
    class Meta:
        db_table = 'shenpiyuan'
        verbose_name = verbose_name_plural = '审批员'
class baoxiuleixing(BaseModel):
    __doc__ = u'''baoxiuleixing'''
    __tablename__ = 'baoxiuleixing'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    baoxiuleixing=models.CharField ( max_length=255, null=True,unique=True, verbose_name='报修类型' )
    '''
    baoxiuleixing=VARCHAR
    '''
    class Meta:
        db_table = 'baoxiuleixing'
        verbose_name = verbose_name_plural = '报修类型'
class baoxiushenqing(BaseModel):
    __doc__ = u'''baoxiushenqing'''
    __tablename__ = 'baoxiushenqing'



    __authTables__={'zhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    baoxiudanhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='报修单号' )
    baoxiumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='报修名称' )
    baoxiuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='报修类型' )
    fengmian=models.TextField   (  null=True, unique=False, verbose_name='封面' )
    baoxiudidian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='报修地点' )
    jinjichengdu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='紧急程度' )
    shenqingshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='申请时间' )
    guzhangmiaoshu=models.TextField   (  null=True, unique=False, verbose_name='故障描述' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    shenpizhuangtai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='审批状态' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='待审核', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    baoxiudanhao=VARCHAR
    baoxiumingcheng=VARCHAR
    baoxiuleixing=VARCHAR
    fengmian=Text
    baoxiudidian=VARCHAR
    jinjichengdu=VARCHAR
    shenqingshijian=DateTime
    guzhangmiaoshu=Text
    zhanghao=VARCHAR
    xingming=VARCHAR
    shouji=VARCHAR
    shenpizhuangtai=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'baoxiushenqing'
        verbose_name = verbose_name_plural = '报修申请'
class baoxiushenpi(BaseModel):
    __doc__ = u'''baoxiushenpi'''
    __tablename__ = 'baoxiushenpi'



    __authTables__={'zhanghao':'yonghu','shenpizhanghao':'shenpiyuan',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    baoxiudanhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='报修单号' )
    baoxiumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='报修名称' )
    baoxiuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='报修类型' )
    fengmian=models.TextField   (  null=True, unique=False, verbose_name='封面' )
    baoxiudidian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='报修地点' )
    jinjichengdu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='紧急程度' )
    shenqingshijian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='申请时间' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    jieshouzhuangtai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='接收状态' )
    shenheshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='审核时间' )
    shenhejieguo=models.CharField ( max_length=255, null=True, unique=False, verbose_name='审核结果' )
    shenheyijian=models.TextField   (  null=True, unique=False, verbose_name='审核意见' )
    shenpizhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='审批账号' )
    shenpixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='审批姓名' )
    '''
    baoxiudanhao=VARCHAR
    baoxiumingcheng=VARCHAR
    baoxiuleixing=VARCHAR
    fengmian=Text
    baoxiudidian=VARCHAR
    jinjichengdu=VARCHAR
    shenqingshijian=VARCHAR
    zhanghao=VARCHAR
    xingming=VARCHAR
    shouji=VARCHAR
    jieshouzhuangtai=VARCHAR
    shenheshijian=DateTime
    shenhejieguo=VARCHAR
    shenheyijian=Text
    shenpizhanghao=VARCHAR
    shenpixingming=VARCHAR
    '''
    class Meta:
        db_table = 'baoxiushenpi'
        verbose_name = verbose_name_plural = '报修审批'
class jieshouweixiu(BaseModel):
    __doc__ = u'''jieshouweixiu'''
    __tablename__ = 'jieshouweixiu'



    __authTables__={'zhanghao':'yonghu','weixiuzhanghao':'weixiurenyuan',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    baoxiudanhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='报修单号' )
    baoxiumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='报修名称' )
    baoxiuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='报修类型' )
    fengmian=models.TextField   (  null=True, unique=False, verbose_name='封面' )
    baoxiudidian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='报修地点' )
    shenqingshijian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='申请时间' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    jieshoushijian=models.DateTimeField  (  null=True, unique=False, verbose_name='接收时间' )
    weixiuzhuangtai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='维修状态' )
    weixiuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='维修账号' )
    weixiuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='维修姓名' )
    lianxifangshi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系方式' )
    '''
    baoxiudanhao=VARCHAR
    baoxiumingcheng=VARCHAR
    baoxiuleixing=VARCHAR
    fengmian=Text
    baoxiudidian=VARCHAR
    shenqingshijian=VARCHAR
    zhanghao=VARCHAR
    xingming=VARCHAR
    shouji=VARCHAR
    jieshoushijian=DateTime
    weixiuzhuangtai=VARCHAR
    weixiuzhanghao=VARCHAR
    weixiuxingming=VARCHAR
    lianxifangshi=VARCHAR
    '''
    class Meta:
        db_table = 'jieshouweixiu'
        verbose_name = verbose_name_plural = '接收维修'
class weixiujieguo(BaseModel):
    __doc__ = u'''weixiujieguo'''
    __tablename__ = 'weixiujieguo'



    __authTables__={'zhanghao':'yonghu','weixiuzhanghao':'weixiurenyuan',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    baoxiudanhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='报修单号' )
    baoxiumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='报修名称' )
    baoxiuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='报修类型' )
    fengmian=models.TextField   (  null=True, unique=False, verbose_name='封面' )
    baoxiudidian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='维修地点' )
    shenqingshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='申请时间' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    wanchengshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='完成时间' )
    weixiushizhang=models.IntegerField  (  null=True, unique=False, verbose_name='维修时长' )
    weixiuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='维修账号' )
    weixiuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='维修姓名' )
    lianxifangshi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系方式' )
    weixiujieguo=models.TextField   (  null=True, unique=False, verbose_name='维修结果' )
    '''
    baoxiudanhao=VARCHAR
    baoxiumingcheng=VARCHAR
    baoxiuleixing=VARCHAR
    fengmian=Text
    baoxiudidian=VARCHAR
    shenqingshijian=DateTime
    zhanghao=VARCHAR
    xingming=VARCHAR
    shouji=VARCHAR
    wanchengshijian=DateTime
    weixiushizhang=Integer
    weixiuzhanghao=VARCHAR
    weixiuxingming=VARCHAR
    lianxifangshi=VARCHAR
    weixiujieguo=Text
    '''
    class Meta:
        db_table = 'weixiujieguo'
        verbose_name = verbose_name_plural = '维修结果'
class syslog(BaseModel):
    __doc__ = u'''syslog'''
    __tablename__ = 'syslog'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    username=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户名' )
    operation=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户操作' )
    method=models.CharField ( max_length=255, null=True, unique=False, verbose_name='请求方法' )
    params=models.TextField   (  null=True, unique=False, verbose_name='请求参数' )
    time=models.BigIntegerField  (  null=True, unique=False, verbose_name='请求时长(毫秒)' )
    ip=models.CharField ( max_length=255, null=True, unique=False, verbose_name='IP地址' )
    '''
    username=VARCHAR
    operation=VARCHAR
    method=VARCHAR
    params=Text
    time=BigInteger
    ip=VARCHAR
    '''
    class Meta:
        db_table = 'syslog'
        verbose_name = verbose_name_plural = '系统日志'
class newstype(BaseModel):
    __doc__ = u'''newstype'''
    __tablename__ = 'newstype'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    typename=models.CharField ( max_length=255,null=False, unique=False, verbose_name='分类名称' )
    '''
    typename=VARCHAR
    '''
    class Meta:
        db_table = 'newstype'
        verbose_name = verbose_name_plural = '公告信息分类'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    __thumbsUp__='是'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='是'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    typename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='分类名称' )
    name=models.CharField ( max_length=255, null=True, unique=False, verbose_name='发布人' )
    headportrait=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    clicktime=models.DateTimeField  (auto_now=True,  null=True, unique=False, verbose_name='最近点击时间' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    typename=VARCHAR
    name=VARCHAR
    headportrait=Text
    clicknum=Integer
    clicktime=DateTime
    thumbsupnum=Integer
    crazilynum=Integer
    storeupnum=Integer
    picture=Text
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '公告信息'
class storeup(BaseModel):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    refid=models.BigIntegerField  (  null=True, unique=False, verbose_name='商品id' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='表名' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='名称' )
    picture=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    type=models.CharField ( max_length=255, null=True, unique=False,default='1', verbose_name='类型' )
    inteltype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='推荐类型' )
    remark=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    '''
    userid=BigInteger
    refid=BigInteger
    tablename=VARCHAR
    name=VARCHAR
    picture=Text
    type=VARCHAR
    inteltype=VARCHAR
    remark=VARCHAR
    '''
    class Meta:
        db_table = 'storeup'
        verbose_name = verbose_name_plural = '收藏表'
