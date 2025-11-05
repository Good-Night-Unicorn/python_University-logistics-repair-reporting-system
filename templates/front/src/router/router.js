import VueRouter from 'vue-router'
//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import Storeup from '../pages/storeup/list'
import News from '../pages/news/news-list'
import NewsDetail from '../pages/news/news-detail'
import payList from '../pages/pay'

import yonghuList from '../pages/yonghu/list'
import yonghuDetail from '../pages/yonghu/detail'
import yonghuAdd from '../pages/yonghu/add'
import weixiurenyuanList from '../pages/weixiurenyuan/list'
import weixiurenyuanDetail from '../pages/weixiurenyuan/detail'
import weixiurenyuanAdd from '../pages/weixiurenyuan/add'
import shenpiyuanList from '../pages/shenpiyuan/list'
import shenpiyuanDetail from '../pages/shenpiyuan/detail'
import shenpiyuanAdd from '../pages/shenpiyuan/add'
import baoxiuleixingList from '../pages/baoxiuleixing/list'
import baoxiuleixingDetail from '../pages/baoxiuleixing/detail'
import baoxiuleixingAdd from '../pages/baoxiuleixing/add'
import baoxiushenqingList from '../pages/baoxiushenqing/list'
import baoxiushenqingDetail from '../pages/baoxiushenqing/detail'
import baoxiushenqingAdd from '../pages/baoxiushenqing/add'
import baoxiushenpiList from '../pages/baoxiushenpi/list'
import baoxiushenpiDetail from '../pages/baoxiushenpi/detail'
import baoxiushenpiAdd from '../pages/baoxiushenpi/add'
import jieshouweixiuList from '../pages/jieshouweixiu/list'
import jieshouweixiuDetail from '../pages/jieshouweixiu/detail'
import jieshouweixiuAdd from '../pages/jieshouweixiu/add'
import weixiujieguoList from '../pages/weixiujieguo/list'
import weixiujieguoDetail from '../pages/weixiujieguo/detail'
import weixiujieguoAdd from '../pages/weixiujieguo/add'
import syslogList from '../pages/syslog/list'
import syslogDetail from '../pages/syslog/detail'
import syslogAdd from '../pages/syslog/add'
import newstypeList from '../pages/newstype/list'
import newstypeDetail from '../pages/newstype/detail'
import newstypeAdd from '../pages/newstype/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'pay',
					component: payList,
				},
				{
					path: 'storeup',
					component: Storeup
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'yonghu',
					component: yonghuList
				},
				{
					path: 'yonghuDetail',
					component: yonghuDetail
				},
				{
					path: 'yonghuAdd',
					component: yonghuAdd
				},
				{
					path: 'weixiurenyuan',
					component: weixiurenyuanList
				},
				{
					path: 'weixiurenyuanDetail',
					component: weixiurenyuanDetail
				},
				{
					path: 'weixiurenyuanAdd',
					component: weixiurenyuanAdd
				},
				{
					path: 'shenpiyuan',
					component: shenpiyuanList
				},
				{
					path: 'shenpiyuanDetail',
					component: shenpiyuanDetail
				},
				{
					path: 'shenpiyuanAdd',
					component: shenpiyuanAdd
				},
				{
					path: 'baoxiuleixing',
					component: baoxiuleixingList
				},
				{
					path: 'baoxiuleixingDetail',
					component: baoxiuleixingDetail
				},
				{
					path: 'baoxiuleixingAdd',
					component: baoxiuleixingAdd
				},
				{
					path: 'baoxiushenqing',
					component: baoxiushenqingList
				},
				{
					path: 'baoxiushenqingDetail',
					component: baoxiushenqingDetail
				},
				{
					path: 'baoxiushenqingAdd',
					component: baoxiushenqingAdd
				},
				{
					path: 'baoxiushenpi',
					component: baoxiushenpiList
				},
				{
					path: 'baoxiushenpiDetail',
					component: baoxiushenpiDetail
				},
				{
					path: 'baoxiushenpiAdd',
					component: baoxiushenpiAdd
				},
				{
					path: 'jieshouweixiu',
					component: jieshouweixiuList
				},
				{
					path: 'jieshouweixiuDetail',
					component: jieshouweixiuDetail
				},
				{
					path: 'jieshouweixiuAdd',
					component: jieshouweixiuAdd
				},
				{
					path: 'weixiujieguo',
					component: weixiujieguoList
				},
				{
					path: 'weixiujieguoDetail',
					component: weixiujieguoDetail
				},
				{
					path: 'weixiujieguoAdd',
					component: weixiujieguoAdd
				},
				{
					path: 'syslog',
					component: syslogList
				},
				{
					path: 'syslogDetail',
					component: syslogDetail
				},
				{
					path: 'syslogAdd',
					component: syslogAdd
				},
				{
					path: 'newstype',
					component: newstypeList
				},
				{
					path: 'newstypeDetail',
					component: newstypeDetail
				},
				{
					path: 'newstypeAdd',
					component: newstypeAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
	]
})
