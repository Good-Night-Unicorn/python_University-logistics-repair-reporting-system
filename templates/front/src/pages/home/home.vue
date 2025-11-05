<template>
	<div class="home-preview">




		<!-- 新闻资讯 -->
		<div id="animate_newsnews" class="news animate__animated">
			<div class="news_title_box">
				<span class="news_title">公告信息</span>
				<span class="news_subhead">{{'news'.toUpperCase()}}</span>
			</div>
			<div v-if="newsList.length" class="list list18 index-pv1">
				<div class="left">
					<div class="list-body">
						<template v-for="(item,index) in newsList">
							<div v-if="index < 6" @click="toDetail('newsDetail', item)" @mouseenter="newsMouseove18(index)" class="list-item" :class="index == newsIndex18 ? 'active' : ''">
								<div class="name">{{item.title}}</div>
							</div>
						</template>
					</div>
					<div class="imgs">
						<template v-for="(item,index) in newsList">
							<img v-if="index < 6" v-show="index == newsIndex18" :src="baseUrl + item.picture" alt="">
						</template>
					</div>
				</div>
				<div class="right">
					<div v-if="newsList.length > 6" class="list-item-top animation-box" @click="toDetail('newsDetail', newsList[6])">
						<img :src="baseUrl + newsList[6].picture">
						<div class="infoBox">
							<div class="name">{{newsList[6].title}}</div>
						</div>
					</div>
					<div v-if="newsList.length > 7" class="list-body">
						<template v-for="(item,index) in newsList">
							<div v-if="index > 6" class="list-item" @click="toDetail('newsDetail', item)">
								<div class="dian"></div>
								<div class="name" >{{item.title}}</div>
								<div class="time">
									<span class="icon iconfont icon-shijian21"></span>
									<span class="text">{{item.addtime.split(' ')[0]}}</span>
								</div>
							</div>
						</template>
					</div>
				</div>
			</div>
			<div class="moreBtn" @click="moreBtn('news')">
				<span class="text">查看更多</span>
				<i class="icon iconfont icon-gengduo1"></i>
			</div>
		</div>
		<!-- 新闻资讯 -->
	</div>
</template>

<script>
import 'animate.css'
import Swiper from "swiper";

	export default {
		//数据集合
		data() {
			return {
				baseUrl: '',
				newsList: [],


				newsIndex18: 0,



			}
		},
		created() {
			this.baseUrl = this.$config.baseUrl;
			this.getNewsList();
			this.getList();
		},
		mounted() {
			window.addEventListener('scroll', this.handleScroll)
			setTimeout(()=>{
				this.handleScroll()
			},100)
			
			this.swiperChanges()
		},
		beforeDestroy() {
			window.removeEventListener('scroll', this.handleScroll)
		},
		//方法集合
		methods: {
			swiperChanges() {
				setTimeout(()=>{
				},750)
			},
			newsMouseove18(index) {
				this.newsIndex18 = index
			},


			handleScroll() {
				let arr = [
					{id:'about',css:'animate__bounce'},
					{id:'system',css:'animate__bounce'},
					{id:'animate_newsnews',css:'animate__bounce'},
				]
			
				for (let i in arr) {
					let doc = document.getElementById(arr[i].id)
					if (doc) {
						let top = doc.offsetTop
						let win_top = window.innerHeight + window.pageYOffset
						// console.log(top,win_top)
						if (win_top > top && doc.classList.value.indexOf(arr[i].css) < 0) {
							// console.log(doc)
							doc.classList.add(arr[i].css)
						}
					}
				}
			},
			preHttp(str) {
				return str && str.substr(0,4)=='http';
			},
			preHttp2(str) {
				return str && str.split(',w').length>1;
			},
			getNewsList() {
				let data = {
					page: 1,
					limit: 12,
					sort: 'addtime',
					order: 'desc'
				}
				this.$http.get('news/list', {params: data}).then(res => {
					if (res.data.code == 0) {
						this.newsList = res.data.data.list;
					
					}
				});
			},
			getList() {
				let autoSortUrl = "";
				let data = {}
			
			},
			toDetail(path, item) {
				this.$router.push({path: '/index/' + path, query: {id: item.id}});
			},
			moreBtn(path) {
				this.$router.push({path: '/index/' + path});
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.home-preview {
		margin: 0px auto;
		flex-direction: column;
		display: flex;
		width: 100%;
		position: relative;
		.news {
			padding: 50px 16%;
			margin: 0;
			background: url(http://codegen.caihongy.cn/20250109/9f2a54e864404d27835768df2d9ef3bb.png) center center/100% 100%;
			width: 100%;
			order: 1;
			.news_title_box {
				margin: 10px auto;
				flex-direction: column;
				background: url(http://codegen.caihongy.cn/20250109/81fff2a86ca447b9b35a496b2956a83e.png) center center/100% 100%;
				display: flex;
				width: 400px;
				line-height: 54px;
				text-align: center;
				.news_title {
					color: #7D9E38;
					font-weight: bold;
					width: 100%;
					font-size: 28px;
					line-height: 50px;
				}
				.news_subhead {
					margin: 0 0 10px;
					color: #7D9E38;
					font-weight: bold;
					width: 100%;
					font-size: 20px;
					line-height: 60px;
					text-align: center;
				}
			}
			.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 10px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
			.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(1.1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list18 {
				padding: 10px 0;
				background: none;
				display: flex;
				width: 100%;
				justify-content: space-between;
				height: auto;
				.left {
					background: #fff;
					display: flex;
					width: 60%;
					justify-content: space-between;
					height: auto;
					.list-body {
						padding: 30px;
						flex-direction: column;
						background: url(http://codegen.caihongy.cn/20250110/0fd4c14995eb4ddfb16ca084a3d9a7f6.png) center center/100% 100%;
						display: flex;
						width: 47%;
						justify-content: space-between;
						height: auto;
						.list-item {
							cursor: pointer;
							padding: 0 15px;
							margin: 0 0 10px;
							background: #fff;
							width: 100%;
							height: 60px;
							.name {
								overflow: hidden;
								color: #333;
								white-space: nowrap;
								font-size: 18px;
								line-height: 60px;
								text-overflow: ellipsis;
							}
						}
						.list-item:hover {
							background: #fff;
							.name {
								color: #7D9E38;
								font-weight: bold;
							}
						}
					}
					.imgs {
						padding: 20px 30px 30px;
						background: url(http://codegen.caihongy.cn/20250110/0fd4c14995eb4ddfb16ca084a3d9a7f6.png) center center/100% 100%;
						width: 47%;
						height: 670px;
						img {
							object-fit: cover;
							display: block;
							width: 100%;
							height: 100%;
						}
					}
				}
				.right {
					padding: 30px 30px 10px;
					background: url(http://codegen.caihongy.cn/20250110/66692b09ff8543bb92ba395b99b7897e.png) center center/100% 100%;
					width: 36%;
					height: auto;
					.list-item-top {
						width: 100%;
						position: relative;
						height: auto;
						img {
							object-fit: cover;
							display: block;
							width: 100%;
							height: 230px;
						}
						.infoBox {
							left: 0;
							bottom: 0;
							background: rgba(0,0,0,.7);
							width: 100%;
							position: absolute;
							.name {
								padding: 0 10px;
								color: #fff;
								font-size: 18px;
								line-height: 44px;
							}
						}
					}
					.list-body {
						.list-item {
							.dian {
								border-radius: 100%;
								margin: 0 6px;
								background: #fff;
								width: 4px;
								height: 4px;
							}
							.name {
								overflow: hidden;
								color: #fff;
								white-space: nowrap;
								flex: 1;
								font-size: 16px;
								line-height: 24px;
								text-overflow: ellipsis;
								transition: 0.3s;
							}
							.time {
								padding: 0 6px;
								width: 50%;
								text-align: right;
								.icon {
									color: #fff;
									font-size: 12px;
									line-height: 24px;
								}
								.text {
									color: #fff;
									font-size: 12px;
									line-height: 1.5;
								}
							}
						}
						.bottom.list-item:hover {
							.dian {
								background: red;
							}
							.title {
								color: red;
							}
							.time {
								.icon {
									color: red;
								}
								.text {
								}
							}
						}
					}
				}
			}
			.moreBtn {
				border: 0;
				padding: 0 0 0 30px;
				margin: 30px auto;
				background: url(http://codegen.caihongy.cn/20250110/60676ea1f545428593323f433fc5fce8.png) center center/100% 100%;
				font-weight: bold;
				display: block;
				width: 170px;
				line-height: 50px;
				text-align: left;
				.text {
					color: #7D9E38;
					font-size: 18px;
				}
				.icon {
					color: #7D9E38;
					display: none;
					font-size: 12px;
				}
			}
		}
	}
</style>
