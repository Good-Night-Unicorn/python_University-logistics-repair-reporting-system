import Vue from 'vue';
//配置路由
import VueRouter from 'vue-router'
Vue.use(VueRouter);
//1.创建组件
import Index from '@/views/index'
import Home from '@/views/home'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import pay from '@/views/pay'
import register from '@/views/register'
import center from '@/views/center'
	import news from '@/views/modules/news/list'
	import weixiurenyuan from '@/views/modules/weixiurenyuan/list'
	import baoxiuleixing from '@/views/modules/baoxiuleixing/list'
	import yonghu from '@/views/modules/yonghu/list'
	import baoxiushenqing from '@/views/modules/baoxiushenqing/list'
	import jieshouweixiu from '@/views/modules/jieshouweixiu/list'
	import baoxiushenpi from '@/views/modules/baoxiushenpi/list'
	import weixiujieguo from '@/views/modules/weixiujieguo/list'
	import syslog from '@/views/modules/syslog/list'
	import config from '@/views/modules/config/list'
	import shenpiyuan from '@/views/modules/shenpiyuan/list'
	import newstype from '@/views/modules/newstype/list'


//2.配置路由   注意：名字
export const routes = [{
	path: '/',
	name: '系统首页',
	component: Index,
	children: [{
		// 这里不设置值，是把main作为默认页面
		path: '/',
		name: '系统首页',
		component: Home,
		meta: {icon:'', title:'center', affix: true}
	}, {
		path: '/updatePassword',
		name: '修改密码',
		component: UpdatePassword,
		meta: {icon:'', title:'updatePassword'}
	}, {
		path: '/pay',
		name: '支付',
		component: pay,
		meta: {icon:'', title:'pay'}
	}, {
		path: '/center',
		name: '个人信息',
		component: center,
		meta: {icon:'', title:'center'}
	}
	,{
		path: '/news',
		name: '公告信息',
		component: news
	}
	,{
		path: '/weixiurenyuan',
		name: '维修人员',
		component: weixiurenyuan
	}
	,{
		path: '/baoxiuleixing',
		name: '报修类型',
		component: baoxiuleixing
	}
	,{
		path: '/yonghu',
		name: '用户',
		component: yonghu
	}
	,{
		path: '/baoxiushenqing',
		name: '报修申请',
		component: baoxiushenqing
	}
	,{
		path: '/jieshouweixiu',
		name: '接收维修',
		component: jieshouweixiu
	}
	,{
		path: '/baoxiushenpi',
		name: '报修审批',
		component: baoxiushenpi
	}
	,{
		path: '/weixiujieguo',
		name: '维修结果',
		component: weixiujieguo
	}
	,{
		path: '/syslog',
		name: '系统日志',
		component: syslog
	}
	,{
		path: '/config',
		name: '轮播图管理',
		component: config
	}
	,{
		path: '/shenpiyuan',
		name: '审批员',
		component: shenpiyuan
	}
	,{
		path: '/newstype',
		name: '公告信息分类',
		component: newstype
	}
	]
	},
	{
		path: '/login',
		name: 'login',
		component: Login,
		meta: {icon:'', title:'login'}
	},
	{
		path: '/register',
		name: 'register',
		component: register,
		meta: {icon:'', title:'register'}
	},
	{
		path: '*',
		component: NotFound
	}
]
//3.实例化VueRouter  注意：名字
const router = new VueRouter({
	mode: 'hash',
	/*hash模式改为history*/
	routes // （缩写）相当于 routes: routes
})
const originalPush = VueRouter.prototype.push
//修改原型对象中的push方法
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}
export default router;
