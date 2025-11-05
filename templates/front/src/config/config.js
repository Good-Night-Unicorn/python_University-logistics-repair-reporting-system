export default {
	baseUrl: 'http://localhost:8080/django79tvn57g/',
	name: '/django79tvn57g',
	indexNav: [
		{
			name: '报修申请',
			url: '/index/baoxiushenqing',
		},
		{
			name: '公告信息',
			url: '/index/news'
		},
	],
	cateList: [
		{
			name: '公告信息',
			refTable: 'newstype',
			refColumn: 'typename',
		},
	]
}
