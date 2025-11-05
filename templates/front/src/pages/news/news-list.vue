<template>
	<div>
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="'·'">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index"><a>{{item.name}}</a></el-breadcrumb-item>
			</el-breadcrumb>
		</div>
	
		<div class="news-preview-pv">
			<el-form :inline="true" :model="formSearch" class="list-form-pv">
				<el-form-item class="search-item">
					<el-input v-model="title" placeholder="标题"></el-input>
				</el-form-item>
				<el-button class="search-btn" type="primary" @click="getNewsList(1)">
					<span class="icon iconfont icon-chakan14"></span>
					搜索
				</el-button>
			</el-form>
			
			<!-- category -->
			<div class="category-list">
				<div class="item" @click="categoryClick(0)" :class="categoryIndex == 0 ? 'active' : ''">全部</div>
				<div v-for="(item,index) in categoryList" @click="categoryClick(index+1)" :key="index" class="item" :class="categoryIndex == index+1 ? 'active' : ''">{{item.typename}}</div>
			</div>
			<!-- 样式二 -->
			<div class="list2 index-pv1">
				<div v-for="item in newsList" :key="item.id" @click="toNewsDetail(item)" class="list-item animation-box">
					<img :src="baseUrl + item.picture" >
					<div class="infoBox">
						<div class="name">{{item.title}}</div>
						<div class="desc">{{item.introduction}}</div>
						<div class="time_item">
							<span class="icon iconfont icon-shijian21"></span>
							<span class="label">发布时间：</span>
							<span class="text">{{item.addtime.split(' ')[0]}}</span>
						</div>
						<div class="publisher_item">
							<span class="icon iconfont icon-geren16"></span>
							<span class="label">发布人：</span>
							<span class="text">{{item.name}}</span>
						</div>
						<div class="like_item">
							<span class="icon iconfont icon-zan10"></span>
							<span class="label">点赞数：</span>
							<span class="text">{{item.thumbsupnum}}</span>
						</div>
						<div class="collect_item">
							<span class="icon iconfont icon-shoucang10"></span>
							<span class="label">收藏量：</span>
							<span class="text">{{item.storeupnum}}</span>
						</div>
						<div class="view_item">
							<span class="icon iconfont icon-chakan9"></span>
							<span class="label">点击量：</span>
							<span class="text">{{item.clicknum}}</span>
						</div>
					</div>
				</div>
			</div>
		
			<el-pagination
				background
				id="pagination" class="pagination"
				:pager-count="7"
				:page-size="pageSize"
				:page-sizes="pageSizes"
				prev-text="上一页"
				next-text="下一页"
				:hide-on-single-page="true"
				:layout='["prev","pager","next"].join()'
				:total="total"
				@current-change="curChange"
				@prev-click="prevClick"
				@next-click="nextClick"
				></el-pagination>

			<!-- 热门信息 -->
			<div class="hot">
				<div class="hot-title">热门信息</div>
				<div class="hot-list">
					<div class="hot-item" v-for="item in hotList" :key="item.id" @click="toNewsDetail(item)">
						<img :src="baseUrl + item.picture" alt="">
						<div class="hot-name">{{ item.title }}</div>
						<div class="hot-time">{{item.addtime}}</div>
					</div>
				</div>
			</div>
			<!-- 最新动态 -->
			<div class="news">
				<div class="news-title">最新动态</div>
				<div class="news-list">
					<div class="news-item" v-for="item in recommendList" :key="item.id" @click="toNewsDetail(item)">
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
				baseUrl: this.$config.baseUrl,
				breadcrumbItem: [
				  {
					name: '公告信息'
				  }
				],
				newsList: [],
				total: 1,
				pageSize: 10,
				pageSizes: [],
				totalPage: 1,
				layouts: '',
				title: '',
				categoryIndex: 0,
				categoryList: [],
				hotList: [],
				recommendList: [],
			}
		},
		created() {
			this.getCategoryList()
			
			this.getHotList()
			this.getRecommendList()
		},
		watch:{
			$route(newValue){
				this.getCategoryList()
			}
		},
		//方法集合
		methods: {
			getCategoryList(){
				this.$http.get('newstype/list', {}).then(res => {
					if (res.data.code == 0) {
						this.categoryList = res.data.data.list;
						if(this.$route.query.homeFenlei){
							for(let i=0;i<this.categoryList.length;i++) {
								if(this.$route.query.homeFenlei == this.categoryList[i].typename) {
									this.categoryIndex = i + 1;
									const currentRoute = this.$route;
									const routeWithoutQuery = { ...currentRoute };
									delete routeWithoutQuery.query;
									this.$router.replace(routeWithoutQuery)
									break;
								}
							}
						}
						this.getNewsList(1);
					}
				});
			},
			categoryClick(index) {
				this.categoryIndex = index
				this.getNewsList()
			},
			getNewsList(page) {
				let params = {page, limit: this.pageSize,sort:'addtime',order:'desc'};
				let searchWhere = {};
				if(this.title != '') searchWhere.title = '%' + this.title + '%';
				if(this.categoryIndex!=0){
					searchWhere.typename = this.categoryList[this.categoryIndex - 1].typename
				}
				this.$http.get('news/list', {params: Object.assign(params, searchWhere)}).then(res => {
					if (res.data.code == 0) {
						this.newsList = res.data.data.list;
						this.total = res.data.data.total;
						this.pageSize = Number(res.data.data.pageSize);
						this.totalPage = res.data.data.totalPage;
						if(this.pageSizes.length==0){
							this.pageSizes = [this.pageSize, this.pageSize*2, this.pageSize*3, this.pageSize*5];
						}
					}
				});
			},
			getHotList(){
				let params = {page:1, limit: 4,sort:'addtime',order:'desc'};
				this.$http.get('news/autoSort', {params: params}).then(res => {
					if (res.data.code == 0) {
						this.hotList = res.data.data.list;
					}
				});
			},
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
			curChange(page) {
				this.getNewsList(page);
			},
			prevClick(page) {
				this.getNewsList(page);
			},
			nextClick(page) {
				this.getNewsList(page);
			},
			toNewsDetail(item) {
				this.$router.push({path: '/index/newsDetail', query: {id: item.id}});
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.news-preview-pv {
				padding: 0 16%;
				margin: 10px auto;
				background: none;
				width: 100%;
				position: relative;
				.list-form-pv {
						padding: 10px;
						background: none;
						display: flex;
						width: 100%;
						justify-content: center;
						align-items: center;
						flex-wrap: wrap;
						height: auto;
						.search-item {
								margin: 0 10px;
								.el-input {
										width: 100%;
									}
				.el-input /deep/ .el-input__inner {
										border: 1px solid #7D9E38;
										border-radius: 8px;
										padding: 0 10px;
										margin: 0;
										outline: none;
										color: #7D9E38;
										width: 200px;
										font-size: 14px;
										line-height: 42px;
										height: 42px;
									}
			}
			.search-btn {
								cursor: pointer;
								border: 0;
								border-radius: 4px;
								padding: 0px 15px;
								margin: 0 10px 0 0;
								outline: none;
								color: #fff;
								background: #7D9E38;
								width: auto;
								font-size: 14px;
								line-height: 42px;
								height: 42px;
								.icon {
										margin: 0 10px 0 0;
										color: #fff;
										font-size: 14px;
									}
			}
		}
		.category-list {
						padding: 10px;
						background: #fff;
						display: flex;
						width: 100%;
						height: auto;
						.item {
								cursor: pointer;
								border-radius: 4px;
								margin: 0 10px 0 0;
								color: #757575;
								background: #DEDEDE;
								width: 72px;
								font-size: 14px;
								line-height: 36px;
								text-align: center;
							}
			
			.item:hover {
								color: #fff;
								background: #7D9E38;
							}
			
			.item.active {
								color: #fff;
								background: #7D9E38;
							}
		}
		.list2 {
						padding: 0;
						background: #fff;
						display: flex;
						width: 100%;
						flex-wrap: wrap;
						height: auto;
						.list-item {
								padding: 20px 30px;
								box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
								margin: 10px;
								background: url(http://codegen.caihongy.cn/20250110/80f24d8dda5a45c3ad84df141cafef08.png) center center/100% 100%;
								display: flex;
								width: 100%;
								font-size: 0;
								position: relative;
								height: auto;
								img {
										object-fit: cover;
										display: inline-block;
										width: 52%;
										height: 250px;
									}
				.infoBox {
										padding: 0 40px;
										overflow: hidden;
										display: flex;
										width: 50%;
										align-items: center;
										flex-wrap: wrap;
										height: 250px;
										.name {
												overflow: hidden;
												color: #638518;
												white-space: nowrap;
												font-weight: bold;
												width: 100%;
												font-size: 16px;
												line-height: 32px;
												text-overflow: ellipsis;
											}
					.desc {
												overflow: hidden;
												color: #638518;
												white-space: nowrap;
												width: 100%;
												font-size: 14px;
												line-height: 21px;
												text-overflow: ellipsis;
											}
					.time_item {
												padding: 0;
												width: 100%;
												.icon {
														margin: 0 5px 0 0;
														color: #7D9E38;
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
														color: #7D9E38;
														font-size: 14px;
														line-height: 25px;
													}
					}
					.publisher_item {
												padding: 0;
												width: 100%;
												.icon {
														margin: 0 5px 0 0;
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
														line-height: 25px;
													}
					}
					.like_item {
												padding: 0 20px 0 0;
												.icon {
														margin: 0 5px 0 0;
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
												padding: 0 20px 0 0;
												.icon {
														margin: 0 5px 0 0;
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
												.icon {
														margin: 0 5px 0 0;
														color: #1E508D;
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
														color: #1E508D;
														font-size: 14px;
														line-height: 25px;
													}
					}
				}
			}
		}
		.hot {
						box-shadow: 0 0px 0px rgba(0,0,0,.1);
						padding: 0 0 20px;
						background: #fff;
						width: 100%;
						height: auto;
						order: 3;
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
										width: 18%;
										justify-content: space-between;
										position: relative;
										flex-wrap: wrap;
										height: auto;
										img {
												object-fit: cover;
												display: block;
												width: 100%;
												height: 70px;
											}
					.hot-name {
												padding: 4px 5px 0;
												color: #638518;
												width: 100%;
												font-size: 16px;
												line-height: 40px;
											}
					.hot-time {
												padding: 0 5px;
												color: #638518;
												font-size: 12px;
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
												padding: 0 10px;
												color: #7D9E38;
												font-weight: bold;
												width: 50%;
												font-size: 16px;
												line-height: 32px;
												text-align: center;
											}
					.news-time {
												padding: 0 10px;
												color: #7D9E38;
												width: 50%;
												font-size: 14px;
												line-height: 30px;
												text-align: center;
											}
				}
			}
		}
	}
	
	.index-pv1 .animation-box {
		transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
		z-index: initial;
	}
	
	.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1.2) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
	}
	
	.index-pv1 .animation-box img {
		transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
	}
	
	.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(0.8) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
</style>
