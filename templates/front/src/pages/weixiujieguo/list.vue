<template>
	<div>
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="'·'">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index"><a>{{item.name}}</a></el-breadcrumb-item>
			</el-breadcrumb>
		</div>
		<div v-if="centerType" class="back_box">
			<el-button class="backBtn" size="mini" @click="backClick">
				<span class="icon iconfont icon-jiantou33"></span>
				<span class="text">返回</span>
			</el-button>
		</div>
		<div class="list-preview">
			<el-form :inline="true" :model="formSearch" class="list-form-pv">
				<el-form-item class="list-item">
					<div class="lable">报修单号：</div>
					<el-input v-model="formSearch.baoxiudanhao" placeholder="报修单号" @keydown.enter.native="getList(1, curFenlei)" clearable></el-input>
				</el-form-item>
				<el-form-item class="list-item">
					<div class="lable">报修名称：</div>
					<el-input v-model="formSearch.baoxiumingcheng" placeholder="报修名称" @keydown.enter.native="getList(1, curFenlei)" clearable></el-input>
				</el-form-item>
				<el-form-item class="list-item">
					<div class="lable">姓名：</div>
					<el-input v-model="formSearch.xingming" placeholder="姓名" @keydown.enter.native="getList(1, curFenlei)" clearable></el-input>
				</el-form-item>
				<el-button class="list-search-btn" v-if=" true " type="primary" @click="getList(1, curFenlei)">
					<i class="el-icon-search"></i>
					查询
				</el-button>
				<el-button class="list-add-btn" v-if="btnAuth('weixiujieguo','新增')" type="primary" @click="add('/index/weixiujieguoAdd')">
					<i class="el-icon-circle-plus-outline"></i>
					添加
				</el-button>
			</el-form>
			<div class="select2">
				<div class="select2-list" v-for="(item,index) in selectOptionsList" :key="item">
					<div class="label">{{item.name}}：</div>
					<div class="item-body">
						<div class="item" @click="selectClick2(item,-1)" :class="item.check ==-1 ? 'active' : ''">全部</div>
						<div class="item" @click="selectClick2(item,index1)" :class="item.check == index1 ? 'active' : ''" v-for="item1,index1 in item.list" :key="item1">{{item1}}</div>
					</div>
				</div>
			</div>
			<div class="list">
				<!-- 样式二 -->
				<div class="list2 index-pv1">
					<div v-for="(item, index) in dataList" :key="index" class="list-item animation-box" @click.stop="toDetail(item)">
						<div class="img">
							<img @click.stop="imgPreView(item.fengmian)" v-if="item.fengmian && item.fengmian.substr(0,4)=='http'&&item.fengmian.split(',w').length>1" :src="item.fengmian" class="image" />
							<img @click.stop="imgPreView(item.fengmian.split(',')[0])" v-else-if="item.fengmian && item.fengmian.substr(0,4)=='http'" :src="item.fengmian.split(',')[0]" class="image" />
							<img @click.stop="imgPreView(baseUrl + (item.fengmian?item.fengmian.split(',')[0]:''))" v-else :src="baseUrl + (item.fengmian?item.fengmian.split(',')[0]:'')" class="image" />
						</div>
						<div class="item-info">
							<div class="name">{{item.baoxiumingcheng}}</div>
							<div class="time_item">
								<span class="icon iconfont icon-shijian21"></span>
								<span class="label">发布时间：</span>
								<span class="text">{{item.addtime.split(' ')[0]}}</span>
							</div>
							<div class="publisher_item">
								<span class="icon iconfont icon-geren16"></span>
								<span class="label">发布人：</span>
								<span class="text">{{item.weixiuzhanghao}}</span>
							</div>
							<div class="more_btn">
							  查看详情
							</div>
						</div>
					</div>
				</div>
			</div>

	
			<el-pagination
				background
				id="pagination"
				class="pagination"
				:pager-count="7"
				:page-size="pageSize"
				prev-text="上一页"
				next-text="下一页"
				:hide-on-single-page="true"
				:layout='["prev","pager","next"].join()'
				:total="total"
				:page-sizes="pageSizes"
				@current-change="curChange"
				@size-change="sizeChange"
				@prev-click="prevClick"
				@next-click="nextClick"
				></el-pagination>
		</div>
		<el-dialog title="预览图" :visible.sync="previewVisible" width="50%">
			<img :src="previewImg" alt="" style="width: 100%;">
		</el-dialog>
	</div>
</template>
<script>
	export default {
		//数据集合
		data() {
			return {
				selectIndex2: 0,
				selectOptionsList: [],
				layouts: '',
				swiperIndex: -1,
				baseUrl: '',
				breadcrumbItem: [
					{
						name: '维修结果'
					}
				],
				formSearch: {
					baoxiudanhao: '',
					baoxiumingcheng: '',
					xingming: '',
				},
				fenlei: [],
				feileiColumn: '',
				dataList: [],
				total: 1,
				pageSize: 12,
				pageSizes: [],
				totalPage: 1,
				curFenlei: '全部',
				isPlain: false,
				indexQueryCondition: '',
				timeRange: [],
				centerType:false,
				previewImg: '',
				previewVisible: false,
				sortType: 'id',
				sortOrder: 'desc',
			}
		},
		async created() {
			if(this.$route.query.centerType&&this.$route.query.centerType!=0){
				this.centerType = true
			}
			this.baseUrl = this.$config.baseUrl;
			await this.getFenlei();
			let fenlei = '全部'
			if(this.$route.query.homeFenlei){
				fenlei = this.$route.query.homeFenlei
			}
			this.getList(1, fenlei);
		},
		watch:{
			$route(newValue){
				this.getList(1, newValue.query.homeFenlei);
			}
		},
		//方法集合
		methods: {
			selectClick2(row,index) {
				row.check = index
				if(index == -1){
					this.formSearch[row.tableName] = ''
				}else {
					this.formSearch[row.tableName] = row.list[index]
				}
				this.getList()
			},
			add(path) {
				let query = {}
				if(this.centerType){
					query.centerType = 1
				}
				this.$router.push({path: path,query:query});
			},
			async getFenlei() {
			},
			getList(page, fenlei, ref = '') {
				let params = {
					page,
					limit: this.pageSize,
				};
				let searchWhere = {};
				if (this.formSearch.baoxiudanhao != '') searchWhere.baoxiudanhao = '%' + this.formSearch.baoxiudanhao + '%';
				if (this.formSearch.baoxiumingcheng != '') searchWhere.baoxiumingcheng = '%' + this.formSearch.baoxiumingcheng + '%';
				if (this.formSearch.xingming != '') searchWhere.xingming = '%' + this.formSearch.xingming + '%';
				let user = JSON.parse(localStorage.getItem('sessionForm'))
				if (this.sortType) searchWhere.sort = this.sortType
				if (this.sortOrder) searchWhere.order = this.sortOrder
				this.$http.get(`weixiujieguo/${this.centerType?'page':'list'}`, {params: Object.assign(params, searchWhere)}).then(res => {
					if (res.data.code == 0) {
						this.dataList = res.data.data.list;
						this.total = Number(res.data.data.total);
						this.pageSize = Number(res.data.data.pageSize);
						this.totalPage = res.data.data.totalPage;
						if(this.pageSizes.length==0){
							this.pageSizes = [this.pageSize, this.pageSize*2, this.pageSize*3, this.pageSize*5];
						}
					}
				});
			},
			curChange(page) {
				this.getList(page);
			},
			prevClick(page) {
				this.getList(page);
			},
			sizeChange(size){
				this.pageSize = size
				this.getList(1);
			},
			nextClick(page) {
				this.getList(page);
			},
			imgPreView(url){
				this.previewImg = url
				this.previewVisible = true
			},
			toDetail(item) {
				let params = {
					id: item.id
				}
				if(this.centerType){
					params.centerType = 1
				}
				this.$router.push({path: '/index/weixiujieguoDetail', query: params});
			},
			btnAuth(tableName,key){
				if(this.centerType){
					return this.isBackAuth(tableName,key)
				}else{
					return this.isAuth(tableName,key)
				}
			},
			backClick() {
				this.$router.push({path: '/index/center'});
			},
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.list-preview {
		padding: 0 16%;
		margin: 10px auto;
		background: #fff;
		display: flex;
		width: 100%;
		position: relative;
		flex-wrap: wrap;
		.list-form-pv {
			padding: 10px 0;
			background: #fff;
			display: flex;
			width: 100%;
			justify-content: flex-start;
			align-items: center;
			flex-wrap: wrap;
			height: auto;
			order: 1;
			.list-item {
				margin: 0 1% 10px;
				width: 48%;
				/deep/.el-form-item__content {
					display: flex;
				}
				.lable {
					padding: 0 10px;
					flex: 1;
					display: inline-block;
					width: 120px;
					line-height: 42px;
				}
				.el-input {
					width: calc(100% - 120px);
				}
				.datetimerange {
					border: 1px solid #7D9E38;
					border-radius: 0;
					padding: 3px 10px;
					box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
					outline: none;
					background: #fff;
					width: calc(100% - 120px);
					justify-content: center;
				}
				.el-input /deep/ .el-input__inner {
					border: 1px solid #7D9E38;
					border-radius: 0;
					padding: 0 10px;
					box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
					margin: 0;
					outline: none;
					color: #333;
					width: 100%;
					font-size: 14px;
					line-height: 42px;
					height: 42px;
				}
				.el-select {
					width: 100%;
				}
				.el-select /deep/ .el-input__inner {
				}
				.el-date-editor {
					width: calc(100% - 120px);
				}
				.el-date-editor /deep/ .el-input__inner {
					border: 1px solid #7D9E38;
					border-radius: 0;
					padding: 0 30px;
					box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
					margin: 0;
					outline: none;
					color: #333;
					width: 100%;
					font-size: 14px;
					line-height: 42px;
					height: 42px;
				}
			}
			.list-search-btn {
				cursor: pointer;
				border: 0;
				border-radius: 0;
				padding: 0px 15px;
				margin: 0 10px 0 0;
				outline: none;
				color: #fff;
				background: #7D9E38;
				width: auto;
				font-size: 14px;
				line-height: 42px;
				height: 42px;
				i {
					margin: 0 10px 0 0;
					color: #fff;
					font-size: 14px;
				}
			}
			.list-add-btn {
				cursor: pointer;
				border: 0;
				border-radius: 0;
				padding: 0px 15px;
				margin: 0 10px 0 0;
				outline: none;
				color: #fff;
				background: #7D9E38;
				width: auto;
				font-size: 14px;
				line-height: 42px;
				height: 42px;
				i {
					margin: 0 10px 0 0;
					color: #fff;
					font-size: 14px;
				}
			}
		}
		.select2 {
			padding: 20px 0;
			background: #fff;
			width: 100%;
			height: auto;
			order: 2;
			.select2-list {
				padding: 20px 0;
				box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
				margin: 0 0 20px;
				background: #fff;
				display: flex;
				width: 100%;
				border-color: #7D9E38;
				border-width: 0 0 1px;
				align-items: center;
				position: relative;
				border-style: solid;
				height: auto;
				.label {
					padding: 0 10px;
					color: #7D9E38;
					white-space: nowrap;
					flex: 1;
					display: inline-block;
					font-size: 14px;
					line-height: 32px;
				}
				.item-body {
					display: flex;
					width: 100%;
					flex-wrap: wrap;
					height: auto;
					.item {
						border-radius: 0;
						padding: 0 20px;
						margin: 0 5px;
						color: #333;
						background: none;
						font-size: 14px;
						line-height: 32px;
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
			}
		}
		.list {
			margin: 0 0 10px;
			background: #fff;
			order: 5;
			.index-pv1 .animation-box {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				z-index: initial;
			}
				
			.index-pv1 .animation-box:hover {
				transform: rotate(0) scale(1.2) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
			}
				
			.index-pv1 .animation-box img {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
			}
			
			.index-pv1 .animation-box img:hover {
				transform: rotate(0) scale(0.8) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
			.list2 {
				padding: 0;
				background: #fff;
				display: flex;
				width: 100%;
				justify-content: space-between;
				flex-wrap: wrap;
				height: auto;
				order: 5;
				.list-item {
					padding: 20px;
					box-shadow: 0px 4px 8px 0px rgba(0, 0, 0, 0.25);
					margin: 0 0 15px;
					color: #000;
					background: url(http://codegen.caihongy.cn/20250110/80f24d8dda5a45c3ad84df141cafef08.png) center center/100% 100%;
					display: flex;
					width: 49%;
					font-size: 0;
					position: relative;
					height: auto;
					.img {
						object-fit: cover;
						display: inline-block;
						width: 50%;
						height: 170px;
						.image {
							object-fit: cover;
							display: block;
							width: 100%;
							transition: all 0.4s;
							height: 100%;
						}
					}
					.item-info {
						padding: 0 20px;
						overflow: hidden;
						display: flex;
						width: 50%;
						justify-content: space-between;
						flex-wrap: wrap;
						height: auto;
						.name {
							padding: 0 10px;
							color: inherit;
							width: 100%;
							font-size: 18px;
							line-height: 1.5;
						}
						.price {
							padding: 0 10px;
							color: #C13800;
							width: 100%;
							font-size: 14px;
							line-height: 2;
						}
						.time_item {
							padding: 0 10px;
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
							padding: 0 10px;
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
							padding: 0 10px;
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
							padding: 0 10px;
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
							padding: 0 10px;
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
						.more_btn {
							border-radius: 20px;
							margin: 5px 0 0;
							color: #fff;
							background: linear-gradient(155deg,#7D9E38 10%,#2e89ff);
							display: block;
							width: 108px;
							font-size: 14px;
							line-height: 32px;
							transition: all .4s ease;
							text-align: center;
							height: 32px;
						}
					}
				}
				.list-item::before {
					border: 5px solid #7D9E38;
					transform: scale3d(0, 1, 1);
					top: 0;
					left: 0;
					width: 100%;
					border-width: 5px 0;
					position: absolute;
					transform-origin: left;
					box-sizing: inherit;
					content: "";
					height: 100%;
				}
				.list-item::after {
					border: 5px solid #7D9E38;
					transform: scale3d(1, 0, 1);
					top: 0;
					left: 0;
					width: 100%;
					border-width: 0 5px;
					position: absolute;
					transform-origin: bottom;
					box-sizing: inherit;
					content: "";
					height: 100%;
				}
				.list-item:hover {
					background: #fff;
					.img {
						.image {
							transform: scale(1.05);
						}
					}
					.item-info {
						.name {
							color: #7D9E38;
							font-weight: bold;
						}
						.more_btn {
							background: linear-gradient(-155deg,#7D9E38 10%,#2e89ff);
						}
					}
				}
				.list-item:hover::before {
					transform: scale3d(1, 1, 1);
					transition: transform 0.4s;
				}
				.list-item:hover::after {
					transform: scale3d(1, 1, 1);
					transition: transform 0.4s;
				}
			}
		}
	}
</style>
