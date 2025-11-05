<template>
	<div class="news-detail-box">
		<div class="back_box">
			<el-button class="backBtn" size="mini" @click="backClick">
				<span class="icon iconfont icon-jiantou33"></span>
				<span class="text">返回</span>
			</el-button>
		</div>
		<div class="news-detail-view">
			<div class="title-box">
				<div>公告信息</div>
			</div>
			<div class="news-detail">
				<div class="detail-title">{{detail.title}}</div>
				<div class="infoBox">
					<div class="time_item">
						<span class="icon iconfont icon-shijian21"></span>
						<span class="label">发布时间：</span>
						<span class="text">{{detail.addtime}}</span>
					</div>
					<div class="publisher_item">
						<span class="icon iconfont icon-geren16"></span>
						<span class="label">发布人：</span>
						<span class="text">{{detail.name}}</span>
					</div>
					<div class="like_item">
						<span class="icon iconfont icon-zan10"></span>
						<span class="label">点赞数：</span>
						<span class="text">{{detail.thumbsupnum}}</span>
					</div>
					<div class="collect_item">
						<span class="icon iconfont icon-shoucang10"></span>
						<span class="label">收藏量：</span>
						<span class="text">{{detail.storeupnum}}</span>
					</div>
					<div class="view_item">
						<span class="icon iconfont icon-chakan9"></span>
						<span class="label">点击量：</span>
						<span class="text">{{detail.clicknum}}</span>
					</div>
				</div>
				<div class="operate">
					<div class="zan-btn" @click="zanClick" >
						<span class="icon iconfont" :class="zanType?'icon-guanzhu-zhihui':'icon-guanzhu-zhihui'" ></span>
						<span class="text" >{{zanType?'取消点赞':'点赞'}}</span>
					</div>
					<div class="collect-btn" @click="collectClick" >
						<span class="icon iconfont" :class="collectType?'icon-shoucang10':'icon-shoucang10'" ></span>
						<span class="text" >{{collectType?'取消收藏':'收藏'}}</span>
					</div>
				</div>
				
				<div class="content-detail ql-snow ql-editor" v-html="detail.content"></div>
			</div>
			<!-- option -->
			<div class="option-box">
				<div class="prev-btn" @click="prepDetailClick">
					<span class="text">上一篇：prev</span>
					<span class="icon iconfont icon-jiantou08"></span>
				</div>
				<div class="next-btn" @click="nextDetailClick">
					<span class="text">下一篇：next</span>
					<span class="icon iconfont icon-jiantou09"></span>
				</div>
			</div>

			<!-- 热门文章 -->
			<div class="hot">
				<div class="hot-title">热门文章</div>
				<div class="hot-list">
					<div class="hot-item" v-for="item in hotList" :key="item.id" @click="toDetail(item.id)">
						<img :src="baseUrl + item.picture" alt="">
						<div class="hot-name">{{ item.title }}</div>
						<div class="hot-time">{{item.addtime}}</div>
					</div>
				</div>
			</div>
			<!-- 推荐文章 -->
			<div class="news">
				<div class="news-title">推荐文章</div>
				<div class="news-list">
					<div class="news-item" v-for="item in recommendList" :key="item.id" @click="toDetail(item.id)">
						<img :src="baseUrl + item.picture" alt="">
						<div class="news-name">{{ item.title }}</div>
						<div class="news-time">{{item.addtime}}</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		//数据集合
		data() {
			return {
				id: 0,
				detail: {},
				zanType: false,
				zanForm: {},
				collectType:false,
				collectForm: {},
				baseUrl:'',
				hotList: [],
				recommendList: [],
				categoryList: [],
				currentIndex: 0,
				allList: [],
				storeupType: false,
			}
		},
		created() {
			if(this.$route.query.storeupType&&this.$route.query.storeupType!=0) {
				this.storeupType = true
			}
			this.id = this.$route.query.id
			this.baseUrl = this.$config.baseUrl;
			this.getCategoryList()
			this.getDetail()
			this.getNewsList()
			this.getHotList()
			this.getRecommendList()
		},
		watch:{
			$route(newValue) {
				this.id = this.$route.query.id
			    this.getDetail()
			}
		},
		methods: {
			backClick() {
				if(this.storeupType){
					history.back()
				}else {
					this.$router.push({path: '/index/news'});
				}
			},
			getNewsList() {
				let params = {page:1, limit: 100,sort:'addtime',order:'desc'};
				this.$http.get('news/list', {params: params}).then(res => {
					if (res.data.code == 0) {
						for(let x in res.data.data.list){
							if(res.data.data.list[x].id == this.id){
								this.currentIndex = Number(x)
								break
							}
						}
						this.allList = res.data.data.list
					}
				});
			},
			// 上一篇
			prepDetailClick(){
				if(this.currentIndex == 0){
					this.$message.error('已经是第一篇了')
					return false
				}
				this.currentIndex--
				this.$router.push({path: '/index/newsDetail', query: {id: this.allList[this.currentIndex].id}});
			},
			// 下一篇
			nextDetailClick(){
				if(this.currentIndex == this.allList.length - 1){
					this.$message.error('已经是最后一篇了')
					return false
				}
				this.currentIndex++
				this.$router.push({path: '/index/newsDetail', query: {id: this.allList[this.currentIndex].id}});
			},
			getCategoryList(){
				this.$http.get('newstype/list', {}).then(res => {
					if (res.data.code == 0) {
						this.categoryList = res.data.data;
					}
				});
			},
			// 获取热门列表
			getHotList(){
				let params = {page:1, limit: 4,sort:'addtime',order:'desc'};
				this.$http.get('news/autoSort', {params: params}).then(res => {
					if (res.data.code == 0) {
						this.hotList = res.data.data.list;
					}
				});
			},
			// 获取推荐列表
			getRecommendList(){
				let url = 'news/autoSort'
				if(localStorage.getItem('frontToken')){
					url = 'news/autoSort2'
				}
				let params = {page:1, limit: 4,sort:'addtime',order:'desc'};
				this.$http.get(url, {params: params}).then(res => {
					if (res.data.code == 0) {
						this.recommendList = res.data.data.list;
					}
				});
			},
			// 跳转详情
			toDetail(id){
				this.$router.push({path: '/index/newsDetail', query: {id: id}});
			},
			getDetail(){
				this.$http.get(`news/detail/${this.id}`,{}).then(res=>{
					if(res.data&&res.data.code==0){
						this.detail = res.data.data
						window.scrollTo(0, 100)
						this.getZan()
						this.getCollect()
					}
				})
			},
			getZan() {
				this.$http.get('storeup/list', {
					params: {
						page: 1,
						limit: 1,
						type: '21',
						userid: Number(localStorage.getItem('frontUserid')),
						tablename: 'news',
						refid: this.id
					}
				}).then(res=>{
					if(res.data&&res.data.code==0){
						if(res.data.data.list.length){
							this.zanType = true
							this.zanForm = res.data.data.list[0]
						}else{
							this.zanType = false
						}
					}
				})
			},
			getCollect(){
				this.$http.get('storeup/list', {
					params: {
						page: 1,
						limit: 1,
						type: '1',
						userid: Number(localStorage.getItem('frontUserid')),
						tablename: 'news',
						refid: this.id
					}
				}).then(res=>{
					if(res.data&&res.data.code==0){
						if(res.data.data.list.length){
							this.collectType = true
							this.collectForm = res.data.data.list[0]
						}else{
							this.collectType = false
						}
					}
				})
			},
			zanClick() {
				if(this.zanType){
					this.$http.post('storeup/delete', [this.zanForm.id]).then(res => {
						if (res.data && res.data.code == 0) {
							this.$message.success('取消成功')
							this.detail.thumbsupnum--
							this.$http.post('news/update',this.detail).then(obj=>{})
							this.getZan()
						}
					})
				}else{
					let data = {
						name: this.detail.title,
						picture: this.detail.picture,
						refid: this.detail.id,
						type: '21',
						tablename: 'news',
						userid: Number(localStorage.getItem('frontUserid')),
					}
					this.$http.post('storeup/add', data).then(res => {
						if (res.data && res.data.code == 0) {
							this.$message.success('点赞成功')
							this.detail.thumbsupnum++
							this.$http.post('news/update',this.detail).then(obj=>{})
							this.getZan()
						}
					})
				}
			},
			collectClick(){
				if(this.collectType){
					this.$http.post('storeup/delete', [this.collectForm.id]).then(res => {
						if (res.data && res.data.code == 0) {
							this.$message.success('取消成功')
							this.detail.storeupnum--
							this.$http.post('news/update',this.detail).then(obj=>{})
							this.getCollect()
						}
					})
				}else{
					let data = {
						name: this.detail.title,
						picture: this.detail.picture,
						refid: this.detail.id,
						type: '1',
						tablename: 'news',
						userid: Number(localStorage.getItem('frontUserid')),
					}
					this.$http.post('storeup/add', data).then(res => {
						if (res.data && res.data.code == 0) {
							this.detail.storeupnum++
							this.$http.post('news/update',this.detail).then(obj=>{})
							this.$message.success('收藏成功')
							this.getCollect()
						}
					})
				}
			},
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	
	.news-detail-box {
				padding: 0 16%;
				margin: 10px auto;
				background: #fff;
				width: 100%;
				position: relative;
				.news-detail-view {
						border-radius: 10px;
						box-shadow: 0 -4px 8px rgba(0,0,0,.3);
						padding: 20px;
						width: 100%;
						.title-box {
								background: #E8E8E8;
								width: 100%;
								height: auto;
								div {
										margin: 10px 0 0;
										color: #000;
										background: none;
										font-size: 20px;
										line-height: 54px;
										text-align: center;
									}
			}
			.news-detail {
								padding: 10px;
								width: 100%;
								position: relative;
								.detail-title {
										color: #000;
										font-size: 18px;
										line-height: 40px;
										text-align: center;
									}
				.infoBox {
										padding: 0 0 10px;
										display: flex;
										width: 100%;
										border-color: #C4C4C4;
										border-width: 0 0 1px;
										justify-content: center;
										align-items: center;
										border-style: solid;
										.time_item {
												padding: 0;
												display: none;
												.icon {
														margin: 0 2px 0 0;
														color: #666;
														font-size: 12px;
														line-height: 1.5;
													}
						.label {
														color: #666;
														font-size: 12px;
														line-height: 1.5;
													}
						.text {
														color: #666;
														font-size: 12px;
														line-height: 1.5;
													}
					}
					.publisher_item {
												padding: 0 20px;
												.icon {
														margin: 0 2px 0 0;
														color: #687FC8;
														font-size: 14px;
														line-height: 25px;
													}
						.label {
														color: #666;
														display: none;
														font-size: 12px;
														line-height: 1.5;
													}
						.text {
														color: #687FC8;
														font-size: 14px;
														line-height: 25px ;
													}
					}
					.like_item {
												padding: 0 20px;
												.icon {
														margin: 0 2px 0 0;
														color: #C13800;
														font-size: 14px;
														line-height: 25px;
													}
						.label {
														color: #666;
														display: none;
														font-size: 12px;
														line-height: 1.5;
													}
						.text {
														color: #C13800;
														font-size: 14px;
														line-height: 25px;
													}
					}
					.collect_item {
												padding: 0 20px;
												.icon {
														margin: 0 2px 0 0;
														color: #F6D742;
														font-size: 14px;
														line-height: 25px;
													}
						.label {
														color: #666;
														display: none;
														font-size: 12px;
														line-height: 1.5;
													}
						.text {
														color: #F6D742;
														font-size: 14px;
														line-height: 25px;
													}
					}
					.view_item {
												padding: 0;
												display: none;
												.icon {
														margin: 0 2px 0 0;
														color: #666;
														font-size: 12px;
														line-height: 1.5;
													}
						.label {
														color: #666;
														font-size: 12px;
														line-height: 1.5;
													}
						.text {
														color: #666;
														font-size: 12px;
														line-height: 1.5;
													}
					}
				}
				.operate {
										padding: 10px 0;
										display: flex;
										width: 100%;
										justify-content: space-between;
										align-items: center;
										.zan-btn {
												padding: 0 15px;
												background: #C13800;
												display: flex;
												justify-content: center;
												align-items: center;
												.icon {
														margin: 0 2px 0 0;
														color: #fff;
														font-size: 14px;
														line-height: 30px;
													}
						.text {
														color: #fff;
														font-size: 14px;
														line-height: 30px;
													}
					}
					.zan-btn:hover {
												background: #C1380080;
												.icon {
														color: #fff;
													}
						.text {
														color: #fff;
													}
					}
					.collect-btn {
												padding: 0 15px;
												background: #F6D742;
												display: flex;
												justify-content: center;
												align-items: center;
												.icon {
														margin: 0 2px 0 0;
														color: #fff;
														font-size: 14px;
														line-height: 30px;
													}
						.text {
														color: #fff;
														font-size: 14px;
														line-height: 30px;
													}
					}
					.collect-btn:hover {
												background: #F6D74280;
												.icon {
														color: #fff;
													}
						.text {
														color: #fff;
													}
					}
				}
				.content-detail {
										width: 100%;
										line-height: 1.5;
										height: auto;
									}
			}
			.option-box {
								padding: 0 20px;
								flex-direction: column;
								display: flex;
								width: 100%;
								justify-content: space-between;
								align-items: center;
								height: auto;
								.prev-btn {
										padding: 0 10px;
										background: #E8E8E8;
										width: 30%;
										text-align: center;
										.text {
												color: #6E6E6E;
												font-size: 14px;
												line-height: 40px;
											}
					.icon {
												color: #6E6E6E;
												font-size: 14px;
												line-height: 40px;
											}
				}
				.prev-btn:hover {
										opacity: 0.7;
										.text {
												color: #6E6E6E;
											}
					.icon {
												color: #6E6E6E;
											}
				}
				.next-btn {
										padding: 0 10px;
										margin: 10px 0;
										background: #7D9E38;
										width: 30%;
										text-align: center;
										.text {
												color: #fff;
												font-size: 14px;
												line-height: 40px;
											}
					.icon {
												color: #fff;
												font-size: 14px;
												line-height: 40px;
											}
				}
				.next-btn:hover {
										opacity: 0.7;
										.text {
												color: #fff;
											}
					.icon {
												color: #fff;
											}
				}
			}
			.hot {
								box-shadow: 0 0px 0px rgba(0,0,0,.1);
								padding: 0 0 20px;
								background: #fff;
								width: 100%;
								height: auto;
								order: 9;
								.hot-title {
										margin: 10px auto;
										flex-direction: column;
										color: #7D9E38;
										background: url(http://codegen.caihongy.cn/20250109/81fff2a86ca447b9b35a496b2956a83e.png) center center/100% 100%;
										font-weight: bold;
										display: flex;
										width: 400px;
										font-size: 28px;
										line-height: 120px;
										text-align: center;
									}
				.hot-list {
										padding: 0 0 5px 0;
										background: #fff;
										display: flex;
										width: 100%;
										flex-wrap: wrap;
										height: auto;
										.hot-item {
												padding: 10px 20px;
												box-shadow: 0px 4px 8px 0px rgba(0, 0, 0, 0.25);
												margin: 0 1%;
												color: #000;
												background: url(http://codegen.caihongy.cn/20250110/fb61c0ccc0b04364888c7be767b3e681.png) center center/100% 100%;
												display: flex;
												width: 23%;
												justify-content: space-between;
												position: relative;
												flex-wrap: wrap;
												height: auto;
												img {
														object-fit: cover;
														display: block;
														width: 100%;
														height: 120px;
													}
						.hot-name {
														padding: 4px 5px 0;
														overflow: hidden;
														color: #638518;
														white-space: nowrap;
														width: 100%;
														font-size: 15px;
														line-height: 40px;
														text-overflow: ellipsis;
													}
						.hot-time {
														padding: 0 5px;
														color: #638518;
														display: none;
														font-size: 13px;
														line-height: 30px;
														text-align: right;
													}
					}
				}
			}
			.news {
								box-shadow: 0 0px 0px rgba(0,0,0,.1);
								padding: 0 0 20px;
								background: #fff;
								width: 100%;
								height: auto;
								order: 3;
								.news-title {
										margin: 10px auto;
										flex-direction: column;
										color: #7D9E38;
										background: url(http://codegen.caihongy.cn/20250109/81fff2a86ca447b9b35a496b2956a83e.png) center center/100% 100%;
										font-weight: bold;
										display: flex;
										width: 400px;
										font-size: 28px;
										line-height: 120px;
										text-align: center;
									}
				.news-list {
										padding: 0;
										background: #fff;
										display: flex;
										width: 100%;
										justify-content: space-between;
										flex-wrap: wrap;
										height: auto;
										order: 5;
										.news-item {
												padding: 20px;
												margin: 0 1% 15px;
												color: #000;
												display: flex;
												font-size: 0;
												flex-wrap: wrap;
												box-shadow: 0px 4px 8px 0px rgba(0, 0, 0, 0.25);
												flex-direction: column;
												background: url(http://codegen.caihongy.cn/20250110/80f24d8dda5a45c3ad84df141cafef08.png) center center/100% 100%;
												width: 23%;
												justify-content: center;
												position: relative;
												height: 140px;
												img {
														object-fit: cover;
														display: inline-block;
														width: 50%;
														height: 100px;
													}
						.news-name {
														padding: 4px 5px 0;
														overflow: hidden;
														color: #638518;
														white-space: nowrap;
														width: 50%;
														font-size: 15px;
														line-height: 40px;
														text-overflow: ellipsis;
														text-align: center;
													}
						.news-time {
														padding: 0 10px;
														color: #7D9E38;
														display: none;
														width: 50%;
														font-size: 13px;
														line-height: 30px;
														text-align: center;
													}
					}
				}
			}
		}
	}
</style>